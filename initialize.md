# Initialize and Run the Vertex AI TFX Pipeline

This guide will help you initialize and run the AutoML training pipeline for Demo3. Please ensure you have set up your GCP account with the necessary permissions before proceeding.

## Steps to Initialize and Run the Pipeline

1. Install requirements
```
pip install -r  requirements.txt
```

2. Create Bigquery dataset
Run the bq_dataset_preprocess.py script to create the preprocessed bigquery dataset.

```
python gcp-mlspecialization-demo3/bq_dataset_preprocess.py
```

3. Initialize and run the pipeline

Run the automl_training.py script to initialize and run the automl pipeline with the necessary configurations.
```
python gcp-mlspecialization-demo3/automl_training.py
```

4. Deploy the model

Run the model_deployment.py script to deploy the registered model in a vertex ai enpoint

```
python gcp-mlspecialization-demo3/model_deployment.py
```

## Monitoring and Logs
You can monitor the progress and logs of your pipeline run through the Vertex AI console on GCP. Navigate to the Vertex AI section and select Pipelines to see the status and details of your pipeline runs.
