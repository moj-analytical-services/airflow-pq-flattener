import os
import sys
import time

from etl_manager.etl import GlueJob


def wait_completion(job):
    class JobFailedError(Exception):
        pass

    class JobTimedOutError(Exception):
        pass

    while True:
        status = job.job_status
        status_code = status["JobRun"]["JobRunState"]
        status_error = status["JobRun"]["ErrorMessage"]

        if status_code in ("SUCCEEDED", "STOPPED"):
            break

        if status_code == "FAILED":
            raise JobFailedError(status_error)
        if status_code == "TIMEOUT":
            raise JobTimedOutError(status_error)

        time.sleep(10)


def main():
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} YYYY-mm-dd")
        sys.exit(1)

    date = sys.argv[1]

    bucket = os.environ["PQ_FLATTENER_S3_BUCKET"]
    iam_role = os.environ["PQ_FLATTENER_JOB_IAM_ROLE"]

    source_path = os.environ["PQ_FLATTENER_SOURCE_PATH"]
    dest_path = os.environ["PQ_FLATTENER_DEST_PATH"]

    job_arguments = {
        "--date": date,
        "--source-path": source_path,
        "--dest-path": dest_path,
    }

    job = GlueJob(
        "v1/glue_jobs/pq_flattener",
        bucket=bucket,
        job_role=iam_role,
        job_arguments=job_arguments,
    )

    job.job_name = f"pq_flattener_{date}"

    # Run job on AWS Glue
    print(f'Starting job "{job.job_name}"...')
    job.run_job()

    # Wait until job succeed (or there was an error)
    wait_completion(job)


if __name__ == "__main__":
    main()
