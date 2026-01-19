import pandas as pd
import requests
import time
from pathlib import Path

# =========================
# PATHS
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

INPUT_FILE = DATA_DIR / "master_500.csv"
OUTPUT_FILE = DATA_DIR / "master_500_with_llm.csv"

# =========================
# HUGGING FACE CONFIG
# =========================
HF_TOKEN = " "

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

LABELS = ["SAFE", "HARASSMENT", "HATE", "SEXUAL", "VIOLENCE"]

# =========================
# CLASSIFIER
# =========================
def classify_text(text):
    payload = {
        "inputs": text,
        "parameters": {
            "candidate_labels": LABELS
        }
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)

        if response.status_code != 200:
            print("HF error:", response.status_code)
            return "SAFE"

        result = response.json()
        return result["labels"][0]

    except Exception as e:
        print("Request failed:", e)
        return "SAFE"

# =========================
# MAIN
# =========================
df = pd.read_csv(INPUT_FILE)

llm_labels = []

print("Running zero-shot safety classification...")
for i, text in enumerate(df["text"], start=1):
    label = classify_text(text)
    llm_labels.append(label)
    print(f"{i}/{len(df)} → {label}")
    time.sleep(0.6)

df["llm_label"] = llm_labels
df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print("\nDONE.")
print("Saved to:", OUTPUT_FILE)
print("\nLabel distribution:")
print(df["llm_label"].value_counts())
