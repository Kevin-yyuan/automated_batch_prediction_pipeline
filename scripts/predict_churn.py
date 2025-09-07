
import pandas as pd
import joblib
from datetime import datetime

# --- Configuration ---
MODEL_PATH = "model/churn_model.joblib"
DATA_PATH = "data/customer_data.csv"
REPORTS_PATH = "reports"
RISK_THRESHOLD = 0.5

# --- Prediction ---
def predict_churn():
    """Loads the model, predicts churn, and generates a report."""
    # Load the trained model
    model = joblib.load(MODEL_PATH)
    print("Churn model loaded successfully.")

    # Load the customer data to be scored
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df)} customer records for scoring.")

    # Select features for prediction
    features = ['age', 'tenure_months', 'monthly_spend', 'last_interaction_days']
    X_predict = df[features]

    # Predict churn probabilities
    probabilities = model.predict_proba(X_predict)[:, 1]
    df['churn_probability'] = probabilities

    # Identify high-risk customers
    high_risk_customers = df[df['churn_probability'] > RISK_THRESHOLD]
    print(f"Identified {len(high_risk_customers)} high-risk customers.")

    # Generate and save the report
    if not high_risk_customers.empty:
        # Format the report filename with the current date
        current_date = datetime.now().strftime("%Y-%m-%d")
        report_filename = f"high_risk_churn_report_{current_date}.csv"
        report_path = f"{REPORTS_PATH}/{report_filename}"

        # Save the high-risk customers to a CSV file
        high_risk_customers.to_csv(report_path, index=False)
        print(f"High-risk customer report saved to {report_path}")
    else:
        print("No high-risk customers to report.")

# --- Main Execution ---
if __name__ == "__main__":
    print("Starting batch prediction process...")
    predict_churn()
    print("Batch prediction process finished.")
