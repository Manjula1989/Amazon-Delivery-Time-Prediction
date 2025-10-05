# create_new_orders.py
import pandas as pd
import os

# Path to save the new orders file
DATA_FOLDER = "Data"
NEW_ORDERS_FILE = "new_orders.csv"
NEW_ORDERS_PATH = os.path.join(DATA_FOLDER, NEW_ORDERS_FILE)

# Sample data - you can add more rows if needed
data = [
    {
        "Agent_Age": 30,
        "Agent_Rating": 4.5,
        "Store_Latitude": 12.9716,
        "Store_Longitude": 77.5946,
        "Customer_Latitude": 12.9352,
        "Customer_Longitude": 77.6245,
        "Distance": 5.0,
        "Vehicle": "scooter",
        "Area": "Urban",
        "Category": "Electronics"
    },
    {
        "Agent_Age": 25,
        "Agent_Rating": 4.2,
        "Store_Latitude": 12.9143,
        "Store_Longitude": 77.6100,
        "Customer_Latitude": 12.9500,
        "Customer_Longitude": 77.6200,
        "Distance": 7.5,
        "Vehicle": "motorcycle",
        "Area": "Semi-Urban",
        "Category": "Clothing"
    }
]

# Create DataFrame
df_new_orders = pd.DataFrame(data)

# Make sure the Data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Save CSV
df_new_orders.to_csv(NEW_ORDERS_PATH, index=False)
print(f"✅ new_orders.csv created at: {NEW_ORDERS_PATH}")
