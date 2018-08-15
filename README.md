# pq_flattener
Parliamentary Questions (PQ) flattener.

Merge raw data from multiple JSON files into a single, flat, CSV.

### Glue job upload/submission

The image entrypoint (`pq_flattener.py`) will first create the Glue job using
 [`etl_manager`](https://github.com/moj-analytical-services/etl_manager).
Then will run the job.

### Glue job logic
The actual glue job is under `v1/glue_jobs/pq_flattener/job.py` (this structure
is dictated by `etl_manager`).

The job will load the JSON files and write out theselect the following co

### Environment variables

- `PQ_FLATTENER_S3_BUCKET`, S3 bucket where:
    1. S3 bucket where the Glue job is uploaded
    2. Where the RAW data is read from
    2. Where the flat CSV is written to
- `PQ_FLATTENER_SOURCE_PATH`, path where the source, raw, JSON files are
- `PQ_FLATTENER_DEST_PATH`, path where to write the combined flat CSV
- `PQ_FLATTENER_JOB_IAM_ROLE`, IAM role assumed by the Glue job when running
