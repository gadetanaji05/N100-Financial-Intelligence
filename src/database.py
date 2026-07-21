import pandas as pd
import sqlite3

def create_connection():
    conn = sqlite3.connect("financial_data.db")
    print("Database connected successfully!")
    return conn

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY,
        company_name TEXT,
        website TEXT
    )
    """)
    cursor.execute("""
CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER,
    company_id TEXT,               
    compounded_sales_growth REAL,
    compounded_profit_growth REAL,
    stock_price_cagr REAL,
    roe REAL
)
""")

    cursor.execute("""
CREATE TABLE IF NOT EXISTS balancesheet (
    company_id TEXT,
    year INTEGER,
    equity_capital REAL,
    reserves REAL,
    borrowings REAL,
    total_assets REAL
)
""")

    cursor.execute("""
CREATE TABLE IF NOT EXISTS cashflow (
    company_id TEXT,
    year INTEGER,
    operating_activity REAL,
    investing_activity REAL,
    financing_activity REAL,
    net_cash_flow REAL
)
""")

    cursor.execute("""
                   
CREATE TABLE IF NOT EXISTS profitandloss (
    company_id TEXT,
    year INTEGER,
    sales REAL,
    expenses REAL,
    operating_profit REAL,
    net_profit REAL,
    eps REAL
)
""")

    cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER,
    company_id TEXT,
    year INTEGER,
    annual_report TEXT
)
""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS prosandcons (
    company_id TEXT,
    pros TEXT,
    cons TEXT
)
""")
    conn.commit()
    print("Table created successfully!")

    

def load_analysis(conn):
    df = pd.read_excel("output/analysis_cleaned.xlsx")
    df = df.drop(columns=["id"],
                 errors="ignore")

    df.to_sql(
        "analysis",
        conn,
        if_exists="append",
        index=False
    )

    print("Analysis data loaded successfully!")

def load_balancesheet(conn):
    df = pd.read_excel("data/balancesheet.xlsx", header=1)
    df.to_sql("balancesheet", conn, if_exists="replace", index=False)
    print("Balance Sheet data loaded successfully!")

def load_cashflow(conn):
    df = pd.read_excel("data/cashflow.xlsx", header=1)
    df.to_sql("cashflow", conn, if_exists="replace", index=False)
    print("Cashflow data loaded successfully!")

def load_profitandloss(conn):
    df = pd.read_excel("data/profitandloss.xlsx", header=1)
    df.to_sql("profitandloss", conn, if_exists="replace", index=False)
    print("Profit and Loss data loaded successfully!")

def load_documents(conn):
    df = pd.read_excel("data/documents.xlsx", header=1)
    df.columns = ["id", "company_id", "year", "annual_report"]
    df.to_sql("documents", conn, if_exists="replace", index=False)
    print("Documents data loaded successfully!")

def load_prosandcons(conn):
    df = pd.read_excel("data/prosandcons.xlsx", header=1)
    df.columns = ["id", "company_id", "pros", "cons"]
    df = df[["company_id", "pros", "cons"]]
    df.to_sql("prosandcons", conn, if_exists="replace", index=False)
    print("Pros and Cons data loaded successfully!")

import pandas as pd

def load_companies(conn):
    df = pd.read_excel("data/companies.xlsx", header=1)

    df = df[["id", "company_name", "website"]]

    df.to_sql(
        "companies",
        conn,
        if_exists="replace",
        index=False
    )

    print("Companies data loaded successfully!")


def view_companies(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM companies LIMIT 5")

    rows = cursor.fetchall()

    print("\nFirst 5 Records:")
    for row in rows:
        print(row)

def show_columns(conn):
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(analysis)")
    columns = cursor.fetchall()

    print("\nColumns in companies table:")
    for col in columns:
        print(col)

def highest_roe(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT company_id, roe
        FROM analysis
        ORDER BY roe DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    print("\nHighest ROE Company")
    print("----------------------")
    print("Company:", result[0])
    print("ROE:", result[1])

def highest_stock_cagr(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT company_id, stock_price_cagr
        FROM analysis
        ORDER BY stock_price_cagr DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    print("\nHighest Stock Price CAGR")
    print("--------------------------")
    print("Company:", result[0])
    print("Stock CAGR:", result[1])

def highest_profit_growth(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT company_id, compounded_profit_growth
        FROM analysis
        ORDER BY compounded_profit_growth DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    print("\nHighest Profit Growth Company")
    print("------------------------------")
    print("Company:", result[0])
    print("Profit Growth:", result[1])

def main():
    conn = create_connection()
    create_tables(conn)

    load_companies(conn)
    load_analysis(conn)
    load_balancesheet(conn)
    load_cashflow(conn)
    load_profitandloss(conn)
    load_documents(conn)
    load_prosandcons(conn)
    view_companies(conn)
    show_columns(conn)
    highest_roe(conn)
    highest_stock_cagr(conn)
    highest_profit_growth(conn)

    conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()