import sqlite3
import pandas as pd

from engine import load_config, run_preset, export_screener
from peer import compare_peers, export_peer_comparison
from radar import create_radar_chart

conn = sqlite3.connect("financial_data.db")

df = pd.read_sql("SELECT * FROM financial_ratios", conn)

config = load_config()

result = run_preset(df, config, "turnaround_watch")

print(
    result[
        [
            "company_id",
            "roe",
            "debt_to_equity",
            "composite_quality_score"
        ]
    ]
)
export_screener(result)

peer_result = compare_peers(result, "TCS")

print("\nTop Peer Comparison:\n")

print(
    peer_result[
        [
            "rank",
            "company_id",
            "roe",
            "debt_to_equity",
            "composite_quality_score",
            "score_difference"
        ]
    ].head(10)
)
export_peer_comparison(peer_result)
create_radar_chart(result, "TCS")
conn.close()

