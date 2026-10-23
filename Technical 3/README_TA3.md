# TA3: Case-Based Reasoning (CBR) Disaster Response Decision Support System

**Course:** CS0065 – Intelligent Systems · **Section:** AN41
**Professor:** Ms. Crisola G. Tan
**Authors:** Jed L. Hizon, Rembrandt Coritana
**Date:** October 2, 2026

## Case Study

**Case Study 1: Disaster Response Decision Support System (DSS)**

New event: a typhoon with expected flooding in an urban area (population 200,000).

## Files

| File | Description |
|------|-------------|
| `TA3_Hizon_Coritana.py` | The full CBR program |
| `TA3_Coritana_Hizon_docx.pdf` | Documentation, screenshot, and pair reflection |

## Requirements

- Python 3.6+ (uses f-strings)
- No third-party packages (only the built-in `math` module)

## How to Run

```bash
python TA3_Hizon_Coritana.py
```

The program takes no input. The new problem is defined inside `main()`.

## How It Works

The program follows the CBR cycle: **Retrieve → Reuse (adapt) → Retain**.

### 1. Case Base

Four past disasters, each stored as a dictionary with a `name`, `problem`, and `solution`:

| Case | Type | Area | Population |
|------|------|------|-----------|
| Typhoon Ursula (2019) | typhoon | urban | 120,000 |
| Typhoon Odette (2021) | typhoon | coastal | 250,000 |
| Metro Flood (2012) | flood | urban | 300,000 |
| Bohol Earthquake (2013) | earthquake | rural | 80,000 |

### 2. Retrieve: Weighted Similarity

`similarity(new, old)` returns a score from 0 to 1:

| Attribute | Weight | Rule |
|-----------|--------|------|
| Disaster type | 0.5 | all-or-nothing match |
| Area type | 0.3 | all-or-nothing match |
| Population | up to 0.2 | `0.2 × min(pop) / max(pop)` |

All cases are ranked by score and the highest is selected.

### 3. Reuse: Adaptation

`adapt(new, old_case)`:

1. Evacuees = new population × the old case's `evacuee_percent`
2. Shelters needed = `ceil(evacuees / shelter_capacity)`
3. If the area is `urban`, append `"; add vertical evacuation and rescue boats"` to the strategy


