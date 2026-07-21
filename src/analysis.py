import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_excel("data/analysis.xlsx", header=1)

    df = df.loc[:,~df.columns.str.contains("^Unnamed")]

    print("Analysis data loaded Successfully!")
    return df

def total_records(df):
    print("\nTotal Records:",len(df))

def column_names(df):
    print("|\ncolumn Names")
    print(df.columns)

def dataset_shape(df):
    print("\nDataset Shape:",df.shape)

def data_type(df):
    print("\nData Types")
    print(df.dtypes)

def summery_statistics(df):
    print("\nsummary Statistics:")
    print(df.describe(include="all"))

def sales_growth_chart(df):
    plt.figure(figsize=(10,5))
    df["growth"] = (
    df["compounded_sales_growth"].str.extract
    (r"(\d+)%")[0].astype(float))
    plt.bar(df["company_id"],df["growth"])
    plt.title("Compounded Sales Growth")
    plt.xlabel("Company")
    plt.ylabel("Sales Growth")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/sales_growth_chart.png")
    plt.show()



def roe_chart(df):
    plt.figure(figsize=(10,5))

    df["roe_value"]=(
        df["roe"]
        .str.extract(r"(\d+)%")[0]
        .astype(float)
    )
    print(df["roe"].head(20))
    print(df["roe_value"])
    
    plt.bar(df["company_id"],
            df["roe_value"])
    plt.title("return on Equality (ROE)")
    plt.xlabel("Company")
    plt.ylabel("ROE(%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/roe_chart.png")

    plt.show()

def stock_cagr_chart(df):
    plt.figure(figsize=(10,5))

    df["stock_cagr_value"]=(
        df["stock_price_cagr"]
        .str.extract(r"(\d+)%")[0]
        .astype(float)
    )
    plt.bar(df["company_id"],
            df["stock_cagr_value"])
    plt.title("Stock Price CAGR")
    plt.xlabel("Company")
    plt.ylabel("Stock CAGR (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("output/stock_cagr_chart.png")
    plt.show()

def company_distribution(df):
    company_counts = df["company_id"].value_counts()
    plt.figure(figsize=(7,7))
    plt.pie(company_counts,labels=company_counts.index,autopct="%1.1f%%",startangle=90)
    plt.title("company Distribution")
    plt.axis("equal")
    plt.savefig("output/company_distribution_chart.png")
    plt.show()

def main():
    df = load_data()
    total_records(df)
    column_names(df)
    dataset_shape(df)
    data_type(df)
    summery_statistics(df)
    print("\nFirst 5 Records")
    print(df.head())
    sales_growth_chart(df)
    roe_chart(df)
    stock_cagr_chart(df)
    company_distribution(df)

if __name__=="__main__":
    main()