import yaml
import pandas as pd


def load_config(path="config/screener_config.yaml"):
    with open(path, "r") as file:
        return yaml.safe_load(file)

def calculate_composite_score(df):

    df = df.copy()

    df["composite_quality_score"] = (
        (df["roe"].fillna(0) * 0.40)
        + (df["net_profit_margin"].fillna(0) * 0.30)
        + (df["operating_profit_margin"].fillna(0) * 0.20)
        + ((1 - df["debt_to_equity"].fillna(0)) * 10)
    )

    return df.sort_values(
        by="composite_quality_score",
        ascending=False
    )


def apply_filters(df, filters):

    result = df.copy()

    if "roe_min" in filters:
        result = result[result["roe"] >= filters["roe_min"]]

    if "debt_to_equity_max" in filters:
        result = result[result["debt_to_equity"] <= filters["debt_to_equity_max"]]

    if "net_profit_margin_min" in filters:
        result = result[
            result["net_profit_margin"] >= filters["net_profit_margin_min"]
        ]

    if "operating_profit_margin_min" in filters:
        result = result[
            result["operating_profit_margin"] >= filters["operating_profit_margin_min"]
        ]

    return result

def run_preset(df, config, preset_name):

    if preset_name not in config:
        raise ValueError(f"Preset '{preset_name}' not found.")

    result = apply_filters(df, config[preset_name])
    result = calculate_composite_score(result)

    return result

def export_screener(df, filename="output/screener_output.xlsx"):

    import os

    os.makedirs("output", exist_ok=True)

    df.to_excel(filename, index=False)

    print(f"Screener exported to {filename}")