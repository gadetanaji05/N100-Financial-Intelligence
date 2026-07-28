import pandas as pd


def compare_peers(df, company_id):

    company = df[df["company_id"] == company_id]

    if company.empty:
        raise ValueError(f"{company_id} not found.")

    df = df.sort_values(
    by="composite_quality_score",
    ascending=False).reset_index(drop=True)

    df["rank"] = df.index + 1

    selected_score = company.iloc[0]["composite_quality_score"]

    df["score_difference"] = (
    df["composite_quality_score"] - selected_score).round(2)

    return df

    return df.sort_values(
        by="composite_quality_score",
        ascending=False
    )

def export_peer_comparison(df, filename="output/peer_comparison.xlsx"):

    import os

    os.makedirs("output", exist_ok=True)

    df.to_excel(filename, index=False)

    print(f"Peer comparison exported to {filename}")