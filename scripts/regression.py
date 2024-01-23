"""
Conduct regression analysis
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import os


def perform_regression(df, output_filename="Regression.png"):
    """
    Perform regression analysis
    """
    X = df.drop("stress_level", axis=1)
    y = df["stress_level"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")

    # Plot the predicted vs. actual values
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Stress Level")
    plt.ylabel("Predicted Stress Level")
    plt.title("Actual vs. Predicted Stress Level")
    plt.savefig(os.path.join("outputs", output_filename))
