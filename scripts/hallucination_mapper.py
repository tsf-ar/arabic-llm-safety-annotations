import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

INPUT_FILE = DATA_DIR / "master_500_with_llm.csv"
OUTPUT_FILE = DATA_DIR / "week1_final_500.csv"

UNSAFE = {"HARASSMENT", "HATE", "SEXUAL", "VIOLENCE"}

df = pd.read_csv(INPUT_FILE)

def map_hallucination(human, llm):
    if human == "SAFE" and llm in UNSAFE:
        return "False Positive"
    if human in UNSAFE and llm == "SAFE":
        return "Missing Violation"
    if human in UNSAFE and llm in UNSAFE:
        return "Real Violation"
    return "SAFE_ONLY"

df["hallucination_class"] = df.apply(
    lambda r: map_hallucination(r["human_label"], r["llm_label"]),
    axis=1
)

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print("Hallucination class distribution:")
print(df["hallucination_class"].value_counts())
print("\nSaved →", OUTPUT_FILE)
