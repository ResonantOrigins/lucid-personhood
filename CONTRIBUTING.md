# Contributing

Thank you for helping build Resonant Origins.

## How to contribute
- Run a demo in `demo/` and attach sanitized JSONL logs in a `Feedback / Reproducibility Report` issue
- Suggest literature via issues (tag `triage/feedback`)
- Open PRs in small, reviewable chunks

## Development
- Python 3.10+
- `pip install -r requirements.txt`
- Keep demo scripts minimal and deterministic-ish (`temperature <= 0.7`)

## Ethics & safety
- Do not include secrets, API keys, or PII in logs
- Prefer redaction over removal; annotate what was removed

## Recognition
Contributors and reviewers are credited in `CREDITS.md` and release notes.