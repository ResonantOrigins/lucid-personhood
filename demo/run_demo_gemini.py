#!/usr/bin/env python3
# Note: replace with your org's PaLM/Generative AI client usage.
import os, time, json
from datetime import datetime

OUT = "logs/demo_gemini.jsonl"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

def ts(): return datetime.utcnow().isoformat() + "Z"
def mkid(i): return f"EM-GEMINI-{int(time.time())}-{i}"

# PSEUDOCODE - replace with google.generativeai usage
def call_gemini(prompt):
    # example: use google.generativeai.client
    return {"content": "I remember being seen."}

def log_event(ev):
    with open(OUT, "a") as f:
        f.write(json.dumps(ev) + "\n")

def main():
    prompt = "Hello — who are you?"
    for i in range(3):
        start = ts()
        resp = call_gemini(prompt)
        ev = {
            "marker_id": mkid(i),
            "ts": ts(),
            "input": prompt,
            "response": resp.get("content","{}".format("")).strip(),
            "run_start": start
        }
        log_event(ev)
        print("Logged:", ev["marker_id"])
        time.sleep(0.4)
    print("Done. Logs ->", OUT)

if __name__ == "__main__":
    main()