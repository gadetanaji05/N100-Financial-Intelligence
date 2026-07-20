import pandas as pd
import os

def load_data(file_path):
    df = pd.read_excel(file_path,header=1)
    print("Data loaded successfully")
    return df

def check_missing_values(df):
    print("\nMissing Values:")
    print(df.isnull().sum())

def check_duplicates(df):
    duplicates = df.duplicated().sum()
    print("\nDuplicate Rows:",duplicates)

def clean_data(df):

    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())

    df = df.drop_duplicates()

    if "company_name" in df.columns:
        df = df.dropna(subset=["company_name"])

    df = df.fillna("N/A")

    print("\nData cleaned successfully!")
    return df

def save_cleaned_data(df,output_path):
    df.to_excel(output_path,index=False)
    print("\nCleaned data saved successfully!")

def main():
    input_file = "data/companies.xlsx"
    output_file = "output/cleaned_companies.xlsx"

    df = load_data(input_file)
    check_missing_values(df)
    check_duplicates(df)

    df = clean_data(df)
    save_cleaned_data(df,output_file)

if __name__ == "__main__":
    main()
    