import pandas as pd

def load_data():
    df = pd.read_excel("output/cleaned_companies.xlsx")
    return df

def main():
    df = load_data()
    print("Financial Intelligence Report")
    print("-"*40)
    print(df.head())
    
    print("\nTotal Records:",len(df))
    print("Total Columns:",len(df.columns))
    print("column Names:")
    print(df.columns.tolist())

    print("\nDataset Summary")
    print("_"*40)
    print(df.describe())

    print("\nHighest ROE Company")
    print("_"*40)
    top_roe = df.loc[df["roe_percentage"].idxmax()]
    print("Company:", top_roe["company_name"])
    print("ROE:",top_roe["roe_percentage"])

    print("\nHighest ROCE Company")
    print("_"*40)
    top_roce=df.loc[df["roce_percentage"].idxmax()]
    print("Company:",top_roce["company_name"])
    print("ROCE",top_roce["roce_percentage"])

    print("\nHighest Book Value Company")
    print("_"*40)
    top_book=df.loc[df["book_value"].idxmax()]
    print("Company:",top_book["company_name"])
    print("Book Value:",top_book["book_value"])

import sqlite3

def generate_financial_report(conn):

    query = """
    SELECT
        c.company_name,
        f.company_id,
        f.net_profit_margin,
        f.operating_profit_margin,
        f.roe,
        f.roa,
        f.debt_to_equity,
        f.asset_turnover
    FROM financial_ratios f
    JOIN companies c
    ON f.company_id = c.id
    """

    df = pd.read_sql_query(query, conn)

    df.to_csv(
        "output/financial_report.csv",
        index=False
    )

    print("\nFinancial Report CSV Generated Successfully!")

if __name__=="__main__":
    main()