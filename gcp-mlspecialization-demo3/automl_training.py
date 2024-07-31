from google.cloud import aiplatform
from google.cloud import storage
import os
import dotenv

# Load the environment variables
dotenv.load_dotenv()


project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
dataset_id = os.getenv('BIGQUERY_DATASET_NAME')
table_id = os.getenv('BIGQUERY_TABLE_NAME')
region = os.getenv('GOOGLE_CLOUD_REGION')
gcs_bucket = os.getenv('GCS_BUCKET_NAME')
transformations_file = os.getenv('TRANSFORMATIONS_FILE_NAME')
vertexai_dataset_name = os.getenv('VERTEXAI_DATASET_NAME')
model_display_name = os.getenv('VERTEXAI_MODEL_NAME')


# Upload the transformations file to GCS
transformations_file_path = f'gs://{gcs_bucket}/{transformations_file}'
source_file_path = 'gcp-mlspecialization-demo3/transforms.json'

storage_client = storage.Client()

# Get the bucket object
bucket = storage_client.bucket(gcs_bucket)

# Create a new blob and upload the file's content.
blob = bucket.blob(transformations_file)
blob.upload_from_filename(source_file_path)

target_column = 'fare'

PipelineJob = aiplatform.PipelineJob(
    display_name = 'pipeline-job',
    template_path = 'https://us-kfp.pkg.dev/ml-pipeline/google-cloud-registry/automl-tabular/sha256:8670157cf7c37d7001d44a3816fb234be7acc6d9c1e6b7c4d55ef24ff7c0410d',
    
    project = project_id,
    location = region,
    parameter_values = {
        "root_dir": "gs://automl_bucket_demo3",
        "project" : project_id,
        "location" : region,
        "optimization_objective" : "minimize-rmse",
        "prediction_type" : "regression",
        "data_source_bigquery_table_path" :f'bq://{project_id}.{dataset_id}.{table_id}',
        "transformations" : transformations_file_path,
        "target_column" : target_column,
        "training_fraction": 0.8,
        "validation_fraction": 0.1,
        "test_fraction": 0.1,
        "train_budget_milli_node_hours" : 3000,
        "model_display_name" : model_display_name,
        "run_evaluation" : True   
    }
)

# run the pipeline
PipelineJob.submit()


