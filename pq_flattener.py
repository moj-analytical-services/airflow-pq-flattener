import os
import sys
import time

from etl_manager.etl import GlueJob


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
        "--s3_source": f"s3://{bucket}/{source_path}",
        "--s3_dest": f"s3://{bucket}/{dest_path}",
    }

    job = GlueJob(
        "v1/glue_jobs/pq_flattener",
        bucket=bucket,
        job_role=iam_role,
        job_arguments=job_arguments,
    )

    job.job_name = f"pq_flattener"

    # Run job on AWS Glue
    print(f'Starting job "{job.job_name}"...')

    try:
        job.run_job()
        job.wait_for_completion()
    finally:
        job.cleanup()


if __name__ == "__main__":
    main()
