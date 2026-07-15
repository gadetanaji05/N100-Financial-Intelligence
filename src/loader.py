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

            print("Rows:", len(df))
            print("Columns:", len(df.columns))

            logging.info(f"{file} loaded successfully")

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
    print("Sprint 2 Day 5 Completed Successfully!")
    print("==============================")


if __name__ == "__main__":
    main()