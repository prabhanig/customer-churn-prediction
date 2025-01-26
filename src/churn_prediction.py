
import pandas as pd
import joblib

def predict_churn(input_file, model_file, output_file):
    # Load the data and model
    data = pd.read_csv('data/cleaned_data.csv')
    model = joblib.load('model/random_forest_model.pkl')
    
    # Make predictions
    predictions = model.predict(data)
    data['Churn Prediction'] = predictions
    
    # Save results
    data.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")

if __name__ == "__main__":
    predict_churn('../data/cleaned_data.csv', '../model/random_forest_model.pkl', '../data/predictions.csv')
