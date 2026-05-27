import time
import json
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# ==============================================================================
# T2SAIM GILT MONITOR — EVENT-STUDY ENGINE v1.0
# Decision: Tarco | Veritas Per Se.
# ==============================================================================

GILT_URL = "https://markets.ft.com/data/bonds/tearsheet/summary?s=UK10YG"
JSON_PATH = r"E:\T2SAIM_GITHUB\UK-2026-elections\gilt_event_study.json"

def get_gilt_yield():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(GILT_URL, headers=headers, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # The yield is typically in a specific data-value or class
            yield_span = soup.find("span", {"class": "mod-ui-data-list__value"})
            if yield_span:
                return float(yield_span.text.strip().replace("%", ""))
    except Exception as e:
        print(f"Error fetching Gilt yield: {e}")
    return None

def update_study_engine(current_yield):
    if not os.path.exists(JSON_PATH): return
    
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    new_event = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event_type": "POLLING_DATA",
        "description": "Automated yield capture for Event-Study Engine.",
        "yield_10y": current_yield
    }
    
    data["events"].append(new_event)
    
    # Check threshold
    if current_yield > 5.25:
        data["engine_id"] = "Gilt_Yield_Event_Study_v1.0_CRITICAL"
        print(f"CRITICAL: Policy Error Threshold breached! Yield: {current_yield}")
    
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    print("Gilt Event-Study Engine Active. Polling every 600s...")
    while True:
        y = get_gilt_yield()
        if y:
            update_study_engine(y)
            print(f"[{datetime.now()}] Yield updated: {y}")
        time.sleep(600)
