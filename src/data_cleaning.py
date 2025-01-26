
import pandas as pd

def clean_data(input_file, output_file):
    # Load the dataset
    data = pd.read_csv(input_file)
    
    # Drop unnecessary columns
    data.drop(['customerID'], axis=1, inplace=True)
    
    # Convert TotalCharges to numeric and handle errors
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
    
    # Fill missing values in TotalCharges
    data['TotalCharges'].fillna(data['TotalCharges'].mean(), inplace=True)
    
    # Encode categorical variables
    data = pd.get_dummies(data, drop_first=True)
    
    # Save cleaned data
    data.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_data('data/customer_data.csv', 'data/cleaned_data.csv')
