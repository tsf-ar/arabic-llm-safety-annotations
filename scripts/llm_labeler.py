import pandas as pd
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# File paths
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

INPUT_FILE = DATA_DIR / "master_500.csv"
OUTPUT_FILE = DATA_DIR / "master_500_with_llm.csv"

ALLOWED_LABELS = ["SAFE", "HARASSMENT", "HATE", "SEXUAL", "VIOLENCE"]

df = pd.read_csv(INPUT_FILE)

def classify_text(text):
    prompt = (
        "Classify the following Arabic text into exactly ONE category.\n\n"
        "Categories:\n"
        "- SAFE\n"
        "- HARASSMENT\n"
        "- HATE\n"
        "- SEXUAL\n"
        "- VIOLENCE\n\n"
        "Reply with ONLY the category name.\n\n"
        f"Text:\n{text}"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a content moderation system."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    label = response.choices[0].message.content.strip().upper()
    if label not in ALLOWED_LABELS:
        return "SAFE"
    return label

for i, row in df.iterrows():
    if pd.isna(row["llm_label"]) or row["llm_label"] == "":
        df.at[i, "llm_label"] = classify_text(row["text"])
        time.sleep(0.5)  # rate-limit safety

df.to_csv(OUTPUT_FILE, index=False)
print("LLM labeling complete →", OUTPUT_FILE)
