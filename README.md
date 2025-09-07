
# Automated Batch Prediction Pipeline for Customer Churn

## Project Goal

To operationalize a machine learning model for predicting customer churn. This project demonstrates an automated pipeline that runs on a schedule, scores a list of current customers, and generates a CSV report of high-risk clients. This showcases MLOps fundamentals, automation with GitHub Actions, model serialization, and reliable Python scripting for production environments.

## Architecture Diagram

The following diagram illustrates the automated workflow:

```
+---------------------------+
|   GitHub Actions Workflow |
| (Scheduled Cron Job)      |
+-------------+-------------+
              |
              v
+-------------+-------------+
|   Set up Python Env       |
|   Install Dependencies    |
+-------------+-------------+
              |
              v
+-------------+-------------+
|   Run predict_churn.py    |
+-------------+-------------+
              |
              v
+-------------+-------------+
| 1. Load Churn Model       |
|    (model/churn_model.joblib) |
+-------------+-------------+
              |
              v
+-------------+-------------+
| 2. Load Customer Data     |
|    (data/customer_data.csv)   |
+-------------+-------------+
              |
              v
+-------------+-------------+
| 3. Score Customers &      |
|    Generate Predictions   |
+-------------+-------------+
              |
              v
+-------------+-------------+
| 4. Save High-Risk Report  |
|    (reports/high_risk_*.csv) |
+-------------+-------------+
              |
              v
+-------------+-------------+
| 5. Upload Report as       |
|    an Artifact            |
+---------------------------+

```

## How to Set Up and Run

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd automated_batch_prediction_pipeline
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Generate sample data:**
    ```bash
    python scripts/generate_data.py
    ```

4.  **Train the model:**
    ```bash
    python scripts/train_model.py
    ```

5.  **Run a batch prediction:**
    ```bash
    python scripts/predict_churn.py
    ```

**Note:** For this project, you might choose to commit the data files for simplicity, but in a real-world scenario, data and large model files are stored elsewhere, like S3 or a database.

## Case Study

This project serves as a practical example of MLOps in action. By automating the prediction process, we eliminate the need for manual intervention, reducing the risk of human error and ensuring that the business always has access to the latest insights on customer churn. The use of GitHub Actions for scheduling and execution makes the pipeline reliable and easy to monitor. The serialized model ensures that the same model is used for every prediction, guaranteeing consistency. Finally, the generated CSV report provides a clear and actionable list of high-risk customers that the business can then target with retention strategies.
