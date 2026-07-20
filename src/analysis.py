import pandas as pd

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

def main():
    df = load_data()
    total_records(df)
    column_names(df)
    dataset_shape(df)
    data_type(df)
    summery_statistics(df)
    print("\nFirst 5 Records")
    print(df.head())

if __name__=="__main__":
    main()