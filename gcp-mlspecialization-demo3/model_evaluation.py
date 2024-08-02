import os

import dotenv
from google.cloud import aiplatform

# Load the environment variables
dotenv.load_dotenv()

project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
model_id = "6254137587510804480"
region = os.getenv("GOOGLE_CLOUD_REGION")

aiplatform.Model.list()
my_model = aiplatform.Model(
    model_name=f"projects/{project_id}/locations/{region}/models/{model_id}"
)

my_evaluation = my_model.get_model_evaluation()

rmse = my_evaluation.to_dict()["metrics"]["rootMeanSquaredError"]
mae = my_evaluation.to_dict()["metrics"]["meanAbsoluteError"]
r2 = my_evaluation.to_dict()["metrics"]["rSquared"]
mape = my_evaluation.to_dict()["metrics"]["meanAbsolutePercentageError"]

print(f"RMSE: {rmse}")
print(f"MAE: {mae}")
print(f"R^2: {r2}")
print(f"MAPE: {mape}")
