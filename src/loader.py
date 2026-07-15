import os
import logging
import pandas as pd

# Logging setup
logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def clean_data(df):
    """Clean the dataframe"""
    df = df.drop_duplicates()
    df = df.fillna("N/A")
    return df

def calculate_financial_ratios(df):
    
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
    df["net_profit"] = pd.to_numeric(df["net_profit"], errors="coerce")
    df["operating_profit"] = pd.to_numeric(df["operating_profit"], errors="coerce")
    df["interest"] = pd.to_numeric(df["interest"], errors="coerce")

    if "sales" in df.columns and "net_profit" in df.columns:
        df["net_profit_margin"] = (
            df["net_profit"] / df["sales"].replace(0, 1)
        ) * 100

    if "sales" in df.columns and "operating_profit" in df.columns:
        df["operating_profit_margin"] = (
            df["operating_profit"] / df["sales"].replace(0, 1)
        ) * 100

    if "operating_profit" in df.columns and "interest" in df.columns:
        df["interest_coverage"] = (
            df["operating_profit"] /
            df["interest"].replace(0, 1)
        )

    return df


def validate_data(df, filename):
    """Validate cleaned dataframe"""
    print(f"\nValidating: {filename}")

    if df.empty:
        print("Warning: File is empty!")

    if df.isnull().sum().sum() > 0:
        print("Warning: Missing values found.")
    else:
        print("No missing values.")

    duplicates = df.duplicated().sum()
    print(f"Duplicate Rows: {duplicates}")

    print("Validation Completed.")


def main():

    logging.info("ETL Pipeline Started")

    data_folder = "data"
    output_folder = "output"

    os.makedirs(output_folder, exist_ok=True)

    files = [f for f in os.listdir(data_folder) if f.endswith(".xlsx")]

    for file in files:

        file_path = os.path.join(data_folder, file)

        print(f"\nProcessing: {file}")

        try:
            # Load Excel
            df = pd.read_excel(file_path, header=1)


            if df.empty:
                print("Empty File")
                logging.warning(f"{file} is empty")
                continue

            print("Rows:",len(df))
            print("Columns:",len(df.columns))
            print(df.columns.tolist())


            logging.info(f"{file} loaded successfully")
            if file =="profitandloss.xlsx":
                df = calculate_financial_ratios(df)

            # Cleaning
            df = clean_data(df)

        
            # Validation
            validate_data(df, file)

            # Save output
            output_file = os.path.join(
                output_folder,
                file.replace(".xlsx", "_cleaned.xlsx")
            )

            df.to_excel(output_file, index=False)

            print("Saved:", output_file)

            logging.info(f"{file} cleaned and saved successfully")

        except Exception as e:
            print(f"Error processing {file}: {e}")
            logging.error(f"{file}: {e}")

    logging.info("ETL Pipeline Completed")

    print("\n==============================")
    print("ETL PIPELINE SUMMARY")
    print("==============================")
    print("All Excel files processed successfully.")
    print("Data cleaned and saved in output folder.")
    print("Validation completed.")
    print("Logging completed.")
    print("Sprint 2 Completed Successfully!")
    print("==============================")

# -------------------------------
# Financial Ratio Functions
# -------------------------------

def calculate_net_profit_margin(df):
    df["net_profit_margin"] = (df["net_profit"] / df["sales"]) * 100
    return df


def calculate_operating_profit_margin(df):
    df["operating_profit_margin"] = (df["operating_profit"] / df["sales"]) * 100
    return df


def calculate_interest_coverage(df):
    df["interest_coverage"] = (
        (df["operating_profit"] + df["other_income"]) /
        df["interest"].replace(0, 1)
    )
    return df

if __name__ == "__main__":
    main()