
import pandas as pd

def clean_data(input_file, output_file):
    # Load the dataset
    data = pd.read_csv(input_file)
    
    # Drop unnecessary columns
    data.drop(['customerID'], axis=1, inplace=True)
    
    # Handle TotalCharges column
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
    data['TotalCharges'].fillna(data['TotalCharges'].mean(), inplace=True)
    
    # Clean categorical variables
    # Replace "No phone service" with "No" in MultipleLines
    data['MultipleLines'] = data['MultipleLines'].replace('No phone service', 'No')
    
    # Replace "No internet service" with "No" in internet-related columns
    internet_related_columns = [
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies'
    ]
    for col in internet_related_columns:
        data[col] = data[col].replace('No internet service', 'No')
    
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
