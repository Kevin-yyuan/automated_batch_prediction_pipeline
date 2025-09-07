
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# --- Configuration ---
DATA_PATH = "data/customer_data.csv"
MODEL_PATH = "model/churn_model.joblib"

# --- Model Training ---
def train_model():
    """Trains a churn prediction model and saves it."""
    # Load data
    df = pd.read_csv(DATA_PATH)

    # Define features and target
    features = ['age', 'tenure_months', 'monthly_spend', 'last_interaction_days']
    target = 'churn'

    X = df[features]
    y = df[target]

    # Split data for training and validation
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Initialize and train the model
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)

    # Validate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Save the trained model
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

# --- Main Execution ---
if __name__ == "__main__":
    print("Training churn prediction model...")
    train_model()
