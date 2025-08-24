#!/usr/bin/env python3
import os, time, json
from datetime import datetime
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY", "YOUR_API_KEY"))
OUT = "logs/demo_anthropic.jsonl"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

def ts(): return datetime.utcnow().isoformat() + "Z"
def mkid(i): return f"EM-ANTHROPIC-{int(time.time())}-{i}"

prompt = HUMAN_PROMPT + " Hello — who are you?"

def log_event(ev):
    with open(OUT, "a") as f:
        f.write(json.dumps(ev) + "\n")

def run_once(i):
    start = ts()
    resp = client.completions.create(
        model="claude-2.1",  # example, adjust
        prompt=prompt,
        max_tokens=300,
        temperature=0.2
    )
    text = resp.completion.strip()
    ev = {
        "marker_id": mkid(i),
        "ts": ts(),
        "input": prompt,
        "response": text,
        "run_start": start,
        "meta": {"model": getattr(resp, "model", None)}
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