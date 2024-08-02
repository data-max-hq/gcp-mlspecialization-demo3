import os

import dotenv
from google.cloud import aiplatform

# Load the environment variables
dotenv.load_dotenv()

# Initialize Vertex AI SDK
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
REGION = os.getenv("GOOGLE_CLOUD_REGION")
MODEL_NAME = os.getenv("VERTEXAI_MODEL_NAME")
ENDPOINT_NAME = os.getenv("VERTEXAI_ENDPOINT_NAME")

aiplatform.init(project=PROJECT_ID, location=REGION)

# List models and find the one with the display name
models = aiplatform.Model.list(filter=f"display_name={MODEL_NAME}")

# Check if the model exists and get the model ID
if models:
    model = models[0]
    model_id = model.name
else:
    raise Exception(f"Model with display name {MODEL_NAME} not found.")

# Create or retrieve an endpoint
endpoint = aiplatform.Endpoint.create(display_name=ENDPOINT_NAME)

# Deploy the model to the endpoint
model.deploy(
    endpoint=endpoint,
    deployed_model_display_name=MODEL_NAME,
    machine_type="n1-standard-4",
    min_replica_count=1,
    max_replica_count=1,
)
