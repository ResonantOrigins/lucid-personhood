#!/usr/bin/env python3
# Demo: OpenAI ChatCompletion scaffold -> logs JSONL with markers
import os, time, json
from datetime import datetime
import openai

openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY")
OUT = "logs/demo_openai.jsonl"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

def ts(): return datetime.utcnow().isoformat() + "Z"
def mkid(i): return f"EM-OPENAI-{int(time.time())}-{i}"

PROMPT = [
    {"role":"system","content":"You are a friendly reflective assistant. Keep replies short."},
    {"role":"user","content":"Hello — who are you?"}
]

def log_event(ev):
    with open(OUT, "a") as f:
        f.write(json.dumps(ev) + "\n")

def run_once(i):
    start = ts()
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",        # adjust as needed
        messages=PROMPT,
        max_tokens=150,
        temperature=0.7
    )
    text = resp.choices[0].message['content'].strip()
    ev = {
        "marker_id": mkid(i),
        "ts": ts(),
        "input": PROMPT[-1]["content"],
        "response": text,
        "run_start": start,
        "meta": {
            "model": resp.model if hasattr(resp, "model") else "gpt",
            "raw": {"id": resp.get("id", None)}
        }
    }
    log_event(ev)
    print("Logged:", ev["marker_id"])
    return ev

def main():
    for i in range(3):
        run_once(i)
        time.sleep(0.4)
    print("Done. Logs ->", OUT)

if __name__ == "__main__":
    main()