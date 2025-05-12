import pandas as pd

# Load your files
customers = pd.read_csv("UX-Metrics-Data-Gathering-All-customers.csv")
lost = pd.read_csv("UX-Metrics-Data-Gathering-All-Closed-Customers-Lost-SF.csv")
productboard = pd.read_csv("UX-Metrics-Data-Gathering-Productboard.csv")

# Add source labels
customers["Source"] = "Salesforce Customers"
lost["Source"] = "Salesforce Lost"
productboard["Source"] = "Productboard"

# Combine files
merged = pd.concat([customers, lost, productboard], ignore_index=True)

# Save merged file
merged.to_csv("Combined_Customer_Data.csv", index=False)
