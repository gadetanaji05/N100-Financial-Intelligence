import os
import matplotlib.pyplot as plt


def create_radar_chart(df, company_id):

    company = df[df["company_id"] == company_id]

    if company.empty:
        raise ValueError(f"{company_id} not found.")

    company = company.iloc[0]

    labels = [
        "ROE",
        "Net Profit",
        "Operating Profit",
        "Debt/Equity"
    ]

    values = [
        company["roe"],
        company["net_profit_margin"],
        company["operating_profit_margin"],
        company["debt_to_equity"]
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)

    os.makedirs("output", exist_ok=True)

    plt.title(f"{company_id} Financial Snapshot")
    plt.savefig(f"output/{company_id}_financial_chart.png")
    plt.close()

    print(f"{company_id} chart exported successfully.")