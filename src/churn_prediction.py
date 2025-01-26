
import pandas as pd
import joblib

def predict_churn(input_file, model_file, output_file):
    # Load the data and model
    data = pd.read_csv(input_file)
    model = joblib.load(model_file)
    
    # Make predictions
    predictions = model.predict(data)
    data['Churn Prediction'] = predictions
    
    # Save results
    data.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")

if __name__ == "__main__":
    # Paths
    input_file = 'data/cleaned_data.csv'  # Path to cleaned data
    model_file = 'model/random_forest_model.pkl'  # Path to trained model
    output_file = 'data/predictions.csv'  # Path to save predictions

    predict_churn(input_file, model_file, output_file)

