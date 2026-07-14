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