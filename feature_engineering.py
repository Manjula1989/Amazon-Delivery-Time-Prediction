# feature_engineering.py
import pandas as pd
import numpy as np
import os

# -------------------------------
# Paths
# -------------------------------
DATA_PATH = "Data/amazon_delivery.csv"
PROCESSED_PATH = "Data/amazon_delivery_processed.csv"

# -------------------------------
# Load dataset
# -------------------------------
df = pd.read_csv(DATA_PATH)
print("✅ Original data loaded!")
print(df.head())

# -------------------------------
# Drop unnecessary columns
# -------------------------------
if 'Order_ID' in df.columns:
    df = df.drop('Order_ID', axis=1)

# Drop high-cardinality columns (Order_Time_*)
high_card_cols = [col for col in df.columns if col.startswith("Order_Time_")]
df = df.drop(columns=high_card_cols, errors='ignore')

# -------------------------------
# Time-based features
# -------------------------------
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Hour'] = df['Order_Date'].dt.hour
df['Weekday'] = df['Order_Date'].dt.weekday

# Drop the original Order_Date
df = df.drop('Order_Date', axis=1)

# -------------------------------
# Haversine distance calculation
# -------------------------------
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlambda = np.radians(lon2 - lon1)
    a = np.sin(dphi/2)**2 + np.cos(phi1)*np.cos(phi2)*np.sin(dlambda/2)**2
    return 2 * R * np.arcsin(np.sqrt(a))

df['Distance_km'] = haversine(df['Store_Latitude'], df['Store_Longitude'],
                              df['Drop_Latitude'], df['Drop_Longitude'])

# Drop original latitude/longitude columns
cols_to_drop = ['Store_Latitude', 'Store_Longitude', 'Drop_Latitude', 'Drop_Longitude']
df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

# -------------------------------
# Fill numeric missing values
# -------------------------------
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

# -------------------------------
# Save processed data
# -------------------------------
os.makedirs("Data", exist_ok=True)
df.to_csv(PROCESSED_PATH, index=False)
print(f"✅ Feature engineering done. Processed data saved at {PROCESSED_PATH}")
