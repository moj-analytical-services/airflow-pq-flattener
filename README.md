[![Docker Repository on Quay](https://quay.io/repository/mojanalytics/pq_flattener/status "Docker Repository on Quay")](https://quay.io/repository/mojanalytics/pq_flattener)

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

- `PQ_FLATTENER_GLUE_JOB_BUCKET`, S3 bucket where the Glue job is
  uploaded
- `PQ_FLATTENER_SOURCE_PATH`, S3 URL pointing to the RAW JSON files
- `PQ_FLATTENER_DEST_PATH`, S3 URL pointing to where to write the
  combined, flat, CSV output
- `PQ_FLATTENER_JOB_IAM_ROLE`, IAM role assumed by the Glue job when running
