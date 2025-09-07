
import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# --- Configuration ---
NUM_CUSTOMERS = 1000
FILE_PATH = "data/customer_data.csv"

# --- Generate Data ---
def generate_customer_data(num_customers):
    """Generates a DataFrame of synthetic customer data."""
    data = []
    for _ in range(num_customers):
        data.append({
            "customer_id": fake.uuid4(),
            "age": random.randint(18, 70),
            "tenure_months": random.randint(1, 60),
            "monthly_spend": round(random.uniform(20.0, 300.0), 2),
            "last_interaction_days": random.randint(0, 90),
            # Target variable: 1 for churn, 0 for not churn
            "churn": random.choices([0, 1], weights=[0.8, 0.2], k=1)[0]
        })
    return pd.DataFrame(data)

# --- Main Execution ---
if __name__ == "__main__":
    print(f"Generating {NUM_CUSTOMERS} synthetic customer records...")
    customer_df = generate_customer_data(NUM_CUSTOMERS)
    
    # Save to CSV
    customer_df.to_csv(FILE_PATH, index=False)
    print(f"Data successfully saved to {FILE_PATH}")

