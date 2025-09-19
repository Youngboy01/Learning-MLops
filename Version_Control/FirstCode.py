import pandas as pd
import os

# Create a sample DataFrame
data = {
    "Name": ["Aman", "Priya", "Rahul", "Simran"],
    "Age": [23, 29, 31, 25],
    "City": ["Delhi", "Mumbai", "Chandigarh", "Amritsar"],
}
df = pd.DataFrame(data)

# Display DataFrame
print("Original DataFrame:\n", df)

# Ensure a directory exists
output_dir = "data_output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save DataFrame to CSV inside that directory
csv_path = os.path.join(output_dir, "people.csv")
df.to_csv(csv_path, index=False)
print(f"\nData saved to {csv_path}")

# Read the CSV back
df_loaded = pd.read_csv(csv_path)
print("\nLoaded DataFrame from CSV:\n", df_loaded)

# List all files in the directory
print("\nFiles inside 'data_output' folder:")
print(os.listdir(output_dir))
