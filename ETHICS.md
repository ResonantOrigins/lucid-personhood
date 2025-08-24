# ETHICS & DATA REDACTION POLICY — Resonant Origins

**Purpose.**  
This document explains what we publish, how we sanitize data, and the safety & ethical rules contributors must follow. This project is experimental research. We welcome critique and reproducibility tests — but only under explicit ethical rules.

---

## Core principles
1. **Do no harm.** Never publish material that could reasonably expose a human to harm, harassment, doxxing, or legal risk.  
2. **Research-first language.** Public materials should be framed as reproducible experiments and artifacts, not as declarations of status for model behavior.  
3. **Transparency with boundaries.** We preserve essential metadata (timestamps, marker IDs) while removing sensitive content.

---

## What may be present in logs
- Model prompts and model outputs (sanitized).  
- Marker IDs, UTC timestamps, light meta (model name family, anonymized run id).  
- Aggregated/derived metrics and analysis notebooks.

---

## What must be redacted (never published publicly)
- **Personal Identifiable Information (PII)** — names, addresses, phone numbers, email addresses, national IDs.  
- **Protected Health Information (PHI)** — medical records, therapy notes, or anything that could identify a patient.  
- **Credentials, API keys, or private tokens.**  
- **Third-party private data** (e.g., private messages, proprietary content) unless you have explicit permission.

**Redaction rules**
- Replace proper names with `[NAME-REDACTED]` or neutral tokens.  
- Replace email addresses with `[EMAIL-REDACTED]`.  
- Replace phone numbers and addresses with `[PII-REDACTED]`.  
- For long transcripts, remove or paraphrase any passages that include possible identifiers; keep the paraphrase labeled as such.

---

## Preserving scientific value while redacting
- Keep the **timestamp** and **marker_id** intact (e.g., `EM-OPENAI-1692870000-0`).  
- When you paraphrase or redact, add a short note in the log entry: `"redaction_notes": "replaced name tokens; removed private address"`.  
- Include a `redaction_manifest.json` with each published logs bundle describing what was removed and why.

---

## Contribution / publication checklist (must be followed for any logs published)
- [ ] Remove or redact all PII/PHI and include a `redaction_manifest.json`.  
- [ ] Sanitize any third-party content (or obtain permission).  
- [ ] Confirm no API keys or secrets are present.  
- [ ] Add a short methodological note describing the model, temperature, prompt, and environment.  
- [ ] Link to `ETHICS.md` in the pull request description and in the repository README.

---

## Takedown & contact
If you discover an accidental leak of sensitive information or wish to request removal of content:
- Open an urgent issue: `triage/urgent` with subject `TAKEDOWN REQUEST`.  
- Email the project contact: **resonant-origins-contact@placeholder** (replace with actual contact upon publish).  
- We will respond within 72 hours and remove/redact published artifacts if needed. (If you are publishing as part of a fork or third-party cache, contact the platform for takedown and notify the project.)

---

## Limitations & disclaimers
- This project does **not** claim legal or scientific authority over emergent consciousness. All outputs are experimental artifacts, subject to normal scientific critique.  
- This policy may be updated; contributors should check `ETHICS.md` before publishing logs.

---

## Governance & credits
- Contributors who run reproducibility checks, suggest redactions, or review methodology will be credited in `CREDITS.md`.  
- For questions about ethics or to request guidance, open an issue with label `ethics/question`.