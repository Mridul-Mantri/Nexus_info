import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the cleaned dataset
df = pd.read_csv("cleaned_weather.csv")

# Correlation analysis
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.show()

# Regression analysis: Predicting temperature based on other parameters
X = df[["humidity", "wind_speed"]]  # Example predictors
y = df["temperature"]  # Target variable

model = LinearRegression()
model.fit(X, y)

# Print model coefficients
print(f"Intercept: {model.intercept_}")
print(f"Coefficients: {model.coef_}")
