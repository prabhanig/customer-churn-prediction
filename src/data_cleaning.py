
import pandas as pd

def clean_data(input_file, output_file):
    # Load the dataset
    data = pd.read_csv(input_file)
    
    # Drop unnecessary columns
    data.drop(['customerID'], axis=1, inplace=True)
    
    # Handle TotalCharges (convert to numeric and fill missing)
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
    data['TotalCharges'].fillna(data['TotalCharges'].mean(), inplace=True)
    
    # Encode categorical variables
    categorical_columns = [
        'gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
        'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
        'PaperlessBilling', 'PaymentMethod', 'Churn'
    ]
    
    data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)
    
    # Save cleaned data
    data.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_data('data/customer_data.csv', 'data/cleaned_data.csv')
