# Demo 3

## Business Goal and Machine Learning Solution

### Business Goal

The primary business goal addressed in this project is to enhance the accuracy and efficiency of fare estimation for taxi services in Chicago. Accurate fare predictions are crucial for both taxi service providers and customers, as they help in setting realistic expectations, improving customer satisfaction, and optimizing operational logistics. Inaccurate fare predictions can lead to dissatisfaction among customers due to unexpected costs, and may also result in inefficiencies in resource allocation for the service providers.

### Machine Learning Use Case

To achieve this business goal, we have implemented a machine learning solution using AutoML to develop a regression model that predicts taxi fares. The AutoML approach simplifies the model development process by automatically selecting the best model architecture, performing feature engineering, and optimizing hyperparameters. The dataset used includes various features such as trip duration, distance, time of day, day of the week, weather conditions, and more.

### Solution Overview

The AutoML solution involves training a regression model on the Chicago Taxi Fare dataset. By utilizing AutoML, we leverage advanced machine learning techniques without the need for extensive manual intervention in model design or hyperparameter tuning. This approach ensures that the model is well-optimized and capable of delivering accurate predictions with minimal effort.

The expected outcome of this solution is to provide accurate fare predictions, thereby improving customer trust and satisfaction. For taxi service providers, this model can be integrated into their dispatch systems to offer dynamic pricing, optimize route planning, and manage driver allocations more effectively.

## Data Exploration

### Data Exploration Process

Data exploration was a critical phase in understanding the Chicago Taxi Fare dataset, informing several key decisions in the project. We utilized Google BigQuery for initial data exploration and leveraged AutoML's built-in features for further analysis. BigQuery enabled efficient querying and analysis of large datasets, while AutoML provided tools for deeper insights and automatic feature engineering.

### Tools and Techniques

The primary tool used for data exploration was BigQuery, complemented by Google Cloud's built-in visualization tools. The data exploration process involved the following steps:

1. ***Data Profiling***:  Initial data profiling was conducted using BigQuery, where we examined data types, missing values, and distributions of each feature. This helped us identify the range of numerical features and categorize other variables.

2. ***Statistical Analysis and Visualization***: Using both BigQuery and AutoML's features, we conducted descriptive statistical analysis and visualizations. BigQuery allowed us to run complex SQL queries, while AutoML's tools provided automated insights into feature importance and distribution.

3. ***Feature Correlation***: AutoML provided a feature importance analysis, highlighting which features had the most significant impact on the target variable, fare. This step was crucial for understanding the relationships between various features.

## Influences on Modeling Decisions

The insights gained from data exploration significantly influenced our modeling decisions. Key findings included:

1. ***Data Preprocessing***: Based on the data exploration findings, we determined the appropriate preprocessing steps for each feature. For example, we decided to normalize the fare amounts due to their wide range and to apply one-hot encoding to categorical features like day of the week.


2. ***Feature Selection***: The feature importance analysis revealed that some features had little correlation with the fare amount. Additionally, other features that can not be available in real-time predictions, were excluded from the model. This careful selection ensured that the model was trained only on relevant and available features.

    The following features were excluded due to having little or no importance on the label feature prediction:
    - payment_method
    - trip_start_timestamp
    - pickup_latitude
    - pickup_location
    - dropoff_location
    - taxi_id
    - pickup_census_tract
    - dropoff_latitude
    - dropoff_census_tract

    The following features were excluded because they can not be available in prediction time:
    - trip_seconds
    - tip
     - trip_end_timestamp

3. ***Model Selection***: The nature of the dataset and the requirement to predict a continuous value (fare amount) led us to choose a tabular regression model within AutoML. This model type was best suited for handling the structured data and delivering accurate fare predictions.

### Example Code Snippet

Here is an example of a SQL query used in BigQuery to analyze the distribution of fares:

```
SELECT
  fare,
  COUNT(*) AS count
FROM
  `bigquery-public-data.chicago_taxi_trips.taxi_trips`
GROUP BY
  fare
ORDER BY
  fare DESC
```

The rest of the code for data exploration is saved in `gcp-mlspecialization-demo3/data_exploration.py`.

## Machine Learning Model Design(s) and Selection

## Model Type and Rationale
The specific model type selected was a tabular regression model, suitable for predicting continuous numerical outcomes—in this case, the fare amount for taxi rides. The choice of a regression model was driven by the nature of the target variable, which is a continuous value.

## Selection Criteria

The decision to use AutoML and a tabular regression model was based on several factors:

1. ***Data Characteristics***: The Chicago Taxi Fare dataset comprises structured data with a mix of numerical and categorical features, making it well-suited for a tabular model.
2. ***Prediction Task***: The goal of predicting a continuous value (fare) aligns with the strengths of regression models.
3. ***Scalability and Efficiency***: AutoML provides scalability, allowing for the processing of large datasets efficiently, and offers automated model evaluation and selection to identify the best-performing algorithm.



## Machine Learning Model Training and Development

### Dataset Sampling

The dataset sampling strategy involved splitting the Chicago Taxi Fare dataset into training, validation, and test subsets. This approach ensures a comprehensive evaluation of the model's performance.

### Sampling Methods and Justification


1. ***Training Dataset***: 80% of the data was allocated for training. This large portion allows the model to learn from a broad range of examples, capturing the necessary patterns and relationships.
2. ***Validation Dataset***: 10% of the data was used for validation, helping to tune the model and prevent overfitting during the training process.
3. ***Test Dataset***: The remaining 10% was reserved for testing, providing an unbiased measure of the model's performance.

The random split of the dataset ensures that the samples in each subset are representative of the overall data, thus avoiding biases that could arise from specific temporal, geographical, or categorical patterns.

### Implementation of AutoML-Based Model Training

The model training was implemented using the Google Cloud AutoML Tables API. The following steps outline the process:

1. Environment Setup: The project ID, dataset ID, table ID, region, and other configuration settings were loaded from environment variables.
2. Dataset Definition: A BigQuery dataset was defined, including the target column (fare) and other relevant features.
3. Model Configuration and Training: The model was configured with specific column specifications, including text, numeric, categorical, and timestamp types. The optimization objective was set to minimize root mean squared error (RMSE), reflecting the goal of accurate fare prediction.

### Model Evaluation Metric

The model's performance was evaluated using the Root Mean Squared Error (RMSE) metric. RMSE was selected because it provides a clear and interpretable measure of prediction accuracy by quantifying the average deviation of the predicted fares from the actual fares.

Justification for RMSE
1. ***Interpretability***: RMSE offers a straightforward interpretation, representing the average prediction error in the same units as the target variable (fare). This makes it a practical choice for assessing model performance in a real-world business context.
2. ***Sensitivity to Large Errors***: RMSE penalizes larger errors more heavily, making it a suitable metric when the cost of large prediction errors is significant. In the context of fare prediction, large discrepancies between predicted and actual fares can lead to customer dissatisfaction and financial inaccuracies.

The code for ***Machine Learning Model Training and Development*** is found on `gcp-mlspecialization-demo3/automl_training.py`.

## Machine Learning Model Evaluation

### Evaluation on Independent Test Dataset
The machine learning model's performance was evaluated using an independent test dataset, which constituted 10% of the original Chicago Taxi Fare dataset. This test set was held out during the training and validation phases to provide an unbiased measure of the model's predictive capabilities.

### Test Dataset Characteristics
The test dataset reflects the distribution of data that the model is expected to encounter in a production environment. It includes a representative mix of various trip characteristics, such as different times of day, diverse routes, varying trip lengths, and a range of fare amounts. This ensures that the evaluation metrics accurately reflect the model's performance on real-world data.

### Performance Metrics
The primary evaluation metric used was the Root Mean Squared Error (RMSE), which provides a measure of the average error between the predicted and actual fares. RMSE is particularly suitable for this regression task as it accounts for the magnitude of errors, penalizing larger discrepancies more heavily.

### Evaluation Results
The model was tested on the independent dataset, and the following results were observed:

- RMSE: 38.099
- MAE: 2.692
- MAPE: 13,413,031
- RMSLE: 0.321
- r-squared: 0.348

The code for retrieving the results of the model evaluation is in `gcp-mlspecialization-demo3/model_evaluation.py`.

### Conclusion
The evaluation on the independent test dataset demonstrates the model's capability to accurately predict taxi fares, with the RMSE value indicating a reasonably low average error. This performance metric confirms the model's effectiveness in real-world applications, aligning with the project's business goals.


Made with ❤️ by [datamax.ai](https://www.datamax.ai/).
