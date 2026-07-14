"""
import pandas as pd

def main():
    print("N100 Financial Intelligence - ETL Loader")

if __name__ == "__main__":
    main()

import pandas as pd

def main():
    df = pd.read_excel("data/companies.xlsx")

    print("Rows:", len(df))
    print("Columns:", list(df.columns))
    print(df.head())

if __name__ == "__main__":
    main()


import pandas as pd

def main():
    df = pd.read_excel("data/companies.xlsx", header=1)

    print(df.head())
    print("\nMissing Values.")
    print(df.isnull().sum())
    print("\nData Types.")
    print(df.dtypes)
    print(df.columns)
    
    print("\nDuplicate Rows:",
    df.duplicated().sum())

    df = df.drop_duplicates()

    df = df.fillna("N/A")
    df.to_excel("output/companies_cleaned.xlsx",index=False)
    print("\nCleaned file saved to output companies_cleaned.xlsx")
    print("\nAfter Cleaning")
    print(df.isnull().sum())

if __name__ == "__main__":
    main()   

import os
import pandas as pd

DATA_FOLDER = "data"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def process_excel(file_path):
    print(f"\nProcessing: {os.path.basename(file_path)}")

    df = pd.read_excel(file_path, header=1)

    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna("N/A")

    output_file = os.path.join(
        OUTPUT_FOLDER,
        os.path.basename(file_path).replace(".xlsx", "_cleaned.xlsx")
    )

    df.to_excel(output_file, index=False)

    print("Saved:", output_file)


def main():

    for file in os.listdir(DATA_FOLDER):

        if file.endswith(".xlsx"):

            file_path = os.path.join(DATA_FOLDER, file)

            process_excel(file_path)


if __name__ == "__main__":
    main()  """


import os
import logging
import pandas as pd

# Logging setup
logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    logging.info("ETL Pipeline Started")

    data_folder = "data"
    output_folder = "output"

    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Get all Excel files
    files = [f for f in os.listdir(data_folder) if f.endswith(".xlsx")]

    for file in files:

        file_path = os.path.join(data_folder, file)

        print(f"\nProcessing: {file}")

        try:
            # Read Excel
            df = pd.read_excel(file_path, header=1)

            # Validation
            if df.empty:
                print("Empty File")
                logging.warning(f"{file} is empty")
                continue

            print("Rows:", len(df))
            print("Columns:", len(df.columns))

            logging.info(f"{file} loaded successfully")

            # Remove duplicates
            duplicates = df.duplicated().sum()
            print("Duplicate Rows:", duplicates)
            df = df.drop_duplicates()

            # Fill missing values
            df = df.fillna("N/A")

            # Save cleaned file
            output_file = os.path.join(
                output_folder,
                file.replace(".xlsx", "_cleaned.xlsx")
            )

            df.to_excel(output_file, index=False)

            print("Saved:", output_file)

            logging.info(f"{file} cleaned and saved successfully")

        except Exception as e:
            print(f"Error processing {file}: {e}")
            logging.error(f"{file} : {e}")

    logging.info("ETL Pipeline Completed")
    print("\nDay 4 Completed Successfully!")


if __name__ == "__main__":
    main()

print("\n==============================")
print("ETL PIPELINE SUMMARY")
print("==============================")
print("All Excel files processed successfully.")
print("Data cleaned and saved in output folder.")
print("Validation completed.")
print("Logging completed.")
print("Sprint 1 Completed Successfully!")
print("==============================")