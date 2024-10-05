import pandas as pd

# Load the weather dataset
df = pd.read_csv("path/to/weather.csv")

# Handle missing values
df.fillna(method="ffill", inplace=True)

# Remove outliers (if any)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

# Export cleaned dataset
df.to_csv("cleaned_weather.csv", index=False)
print("Data cleaned and saved.")
