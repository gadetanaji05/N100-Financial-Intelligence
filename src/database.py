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
    company_id primary key,               
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

    cursor.execute("""
CREATE TABLE IF NOT EXISTS prosandcons (
    company_id TEXT,
    pros TEXT,
    cons TEXT
)
""")

    cursor.execute("""
CREATE TABLE IF NOT EXISTS financial_ratios (
    company_id TEXT PRIMARY KEY,

    net_profit_margin REAL,
    operating_profit_margin REAL,
    roe REAL,
    roce REAL,
    roa REAL,

    debt_to_equity REAL,
    interest_coverage_ratio REAL,
    net_debt REAL,
    asset_turnover REAL,

    revenue_cagr REAL,
    profit_cagr REAL,
    eps_cagr REAL,

    free_cash_flow REAL,
    cfo_quality_score REAL,
    capex_intensity REAL,
    fcf_conversion REAL,
    capital_allocation_ratio REAL
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

def load_financial_ratios(conn):

    analysis = pd.read_sql("SELECT * FROM analysis", conn)
    balancesheet = pd.read_sql("SELECT * FROM balancesheet", conn)
    cashflow = pd.read_sql("SELECT * FROM cashflow", conn)
    profitandloss = pd.read_sql("SELECT * FROM profitandloss", conn)

    print("Analysis Shape:", analysis.shape)
    print("Balance Sheet Shape:", balancesheet.shape)
    print("Cashflow Shape:", cashflow.shape)
    print("Profit & Loss Shape:", profitandloss.shape)

    # Merge Tables
    df = profitandloss.merge(
        balancesheet,
        on=["company_id", "year"],
        how="inner"
    )

    df = df.merge(
        cashflow,
        on=["company_id", "year"],
        how="inner"
    )

    print("Merged Shape:", df.shape)
    print(df.head())

    # Calculate Financial Ratios
    df["net_profit_margin"] = (
        df["net_profit"] / df["sales"]
    ) * 100

    df["operating_profit_margin"] = (
        df["operating_profit"] / df["sales"]
    ) * 100

    df["roe"] = (
        df["net_profit"] /
        (df["equity_capital"] + df["reserves"])
    ) * 100

    df["roa"] = (
        df["net_profit"] /
        df["total_assets"]
    ) * 100

    df["debt_to_equity"] = (
        df["borrowings"] /
        (df["equity_capital"] + df["reserves"])
    )

    print(
        df[
            [
                "company_id",
                "year",
                "net_profit_margin",
                "operating_profit_margin",
                "roe",
                "roa",
                "debt_to_equity"
            ]
        ].head()
    )

    # Create Financial Ratio DataFrame
    ratio_df = df[
        [
            "company_id",
            "net_profit_margin",
            "operating_profit_margin",
            "roe",
            "roa",
            "debt_to_equity"
        ]
    ].copy()

    ratio_df = ratio_df.groupby("company_id").last().reset_index()

    # Remaining columns
    ratio_df["interest_coverage_ratio"] = None
    ratio_df["net_debt"] = None
    ratio_df["asset_turnover"] = None
    ratio_df["revenue_cagr"] = None
    ratio_df["profit_cagr"] = None
    ratio_df["eps_cagr"] = None
    ratio_df["free_cash_flow"] = None
    ratio_df["cfo_quality_score"] = None
    ratio_df["capex_intensity"] = None
    ratio_df["fcf_conversion"] = None
    ratio_df["capital_allocation_ratio"] = None

    # Save into SQLite
    ratio_df.to_sql(
        "financial_ratios",
        conn,
        if_exists="replace",
        index=False
    )

    print("Financial Ratios loaded successfully!")
    
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

def view_financial_ratios(conn):

    cursor = conn.cursor()

    print("\nFinancial Ratios Table")
    print("-" * 30)

    cursor.execute("""
        SELECT company_id,
               net_profit_margin,
               operating_profit_margin,
               roe,
               roa,
               debt_to_equity
        FROM financial_ratios
        LIMIT 5
    """)

    for row in cursor.fetchall():
        print(row)

def generate_ratio_edge_cases(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            company_id,
            roe,
            debt_to_equity
        FROM financial_ratios
    """)

    rows = cursor.fetchall()

    with open("ratio_edge_cases.log", "w") as file:

        file.write("Ratio Edge Cases Report\n")
        file.write("=" * 40 + "\n\n")

        for row in rows:

            company = row[0]
            roe = row[1]
            debt = row[2]

            financial_companies = [
                "HDFCBANK",
                "SBIN",
                "ICICIBANK",
                "KOTAKBANK",
                "AXISBANK",
                "INDUSINBK",
                "BANKBARODA",
                "PNB",
                "SBILIFE",
                "HDFCLIFE"
            ]
            if company in financial_companies:
                file.write(f"{company} -> Financial Sector (Special Handling)\n")
                continue

            if roe is None:
                file.write(f"{company} -> Missing ROE\n")

            elif roe < 0:
                file.write(f"{company} -> Negative ROE\n")

            if debt is not None and debt > 5:
                file.write(f"{company} -> High Debt To Equity ({debt:.2f})\n")

    print("ratio_edge_cases.log generated successfully!")

def verify_roe(conn):

    cursor = conn.cursor()

    cursor.execute("""
        select
        f.company_id,
        round(f.roe,2),
        MAX(a.roe)
    from financial_ratios f
    join analysis a
    on f.company_id=a.company_id
    group by f.company_id
    limit 10
    """)

    rows = cursor.fetchall()

    print("\nROE Verification")
    print("-" * 35)

    for row in rows[:10]:

        print(
            f"{row[0]} | "
            f"Calculated: {row[1]} | "
            f"Analysis: {row[2]}"
        )

def verify_ratio_count(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM financial_ratios
    """)

    total = cursor.fetchone()[0]

    print("\nFinancial Ratios Count")
    print("-" * 30)
    print("Total Records :", total)

def verify_high_roe(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT company_id, roe
        FROM financial_ratios
        WHERE roe > 15
        ORDER BY roe DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    print("\nHigh ROE Companies")
    print("-" * 30)

    for row in rows:
        print(row)

def verify_low_debt(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT company_id, debt_to_equity
        FROM financial_ratios
        WHERE debt_to_equity < 1
        ORDER BY debt_to_equity
        LIMIT 10
    """)

    rows = cursor.fetchall()

    print("\nLow Debt Companies")
    print("-" * 30)

    for row in rows:
        print(row)

def sprint2_summary(conn):

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM financial_ratios")
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM financial_ratios
        WHERE roe > 15
    """)
    high_roe = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM financial_ratios
        WHERE debt_to_equity < 1
    """)
    low_debt = cursor.fetchone()[0]

    print("\nSprint 2 Summary")
    print("-" * 35)
    print("Financial Ratio Records :", total)
    print("ROE > 15% :", high_roe)
    print("Debt/Equity < 1 :", low_debt)

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
    load_financial_ratios(conn)
    view_companies(conn)
    show_columns(conn)
    highest_roe(conn)
    highest_stock_cagr(conn)
    highest_profit_growth(conn)
    view_financial_ratios(conn)
    generate_ratio_edge_cases
    verify_roe(conn)
    verify_roe(conn)
    verify_ratio_count(conn)
    verify_high_roe(conn)
    verify_low_debt(conn)
    sprint2_summary(conn)

    conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    main()