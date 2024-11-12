# Initialize and Run the Vertex AI TFX Pipeline

This guide will help you initialize and run the AutoML training pipeline for Demo3. Please ensure you have set up your GCP account with the necessary permissions before proceeding.

## Steps to Initialize and Run the Pipeline

1. **Install Git**  
   Install Git if it's not already available on your system:
   ```bash
   sudo apt install -y git
   ```

2. **Clone the Repository**  
   Clone the `gcp-mlspecialization-demo3` repository:
   ```bash
   git clone https://github.com/data-max-hq/gcp-mlspecialization-demo3
   cd gcp-mlspecialization-demo3
   ```

3. **Install Requirements**  
   Navigate into the cloned repository and install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create BigQuery Dataset**  
   Run the `bq_dataset_preprocess.py` script to create the preprocessed BigQuery dataset:
   ```bash
   python gcp-mlspecialization-demo3/bq_dataset_preprocess.py
   ```

5. **Initialize and Run the Pipeline**  
   Run the `automl_training.py` script to initialize and run the AutoML pipeline with the necessary configurations:
   ```bash
   python gcp-mlspecialization-demo3/automl_training.py
   ```

6. **Deploy the Model**  
   Use the `model_deployment.py` script to deploy the registered model in a Vertex AI endpoint:
   ```bash
   python gcp-mlspecialization-demo3/model_deployment.py
   ```

## Monitoring and Logs
You can monitor the progress and logs of your pipeline run through the Vertex AI console on GCP. Navigate to the Vertex AI section and select **Pipelines** to see the status and details of your pipeline runs.
