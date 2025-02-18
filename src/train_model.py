import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def train_model(input_file, model_file):
    # Ensure the model directory exists
    model_dir = os.path.dirname(model_file)
    os.makedirs(model_dir, exist_ok=True)

    # Load cleaned data
    data = pd.read_csv(input_file)
    
    # Separate features and target variable
    X = data.drop('Churn_Yes', axis=1)
    y = data['Churn_Yes']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    # Save the model
    joblib.dump(model, model_file)
    print(f"Model saved to {model_file}")

if __name__ == "__main__":
    # Paths
    input_file = 'data/cleaned_data.csv'  # Path to cleaned data
    model_file = 'model/random_forest_model.pkl'  # Path to save trained model

    train_model(input_file, model_file)

