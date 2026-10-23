# TA4: Knowledge Representation, Rule-Based Reasoning (RBR), and Case-Based Reasoning (CBR)

**Course:** CS0065 – Intelligent Systems · **Section:** AN41
**Professor:** Ms. Crisola G. Tan
**Authors:** Jed L. Hizon, Rembrandt V. Coritana
**Date:** October 3, 2026

Two small Python programs that solve the same kind of problem, **laptop troubleshooting**, with two different reasoning approaches so they can be compared.

## Files

| File | Description |
|------|-------------|
| `TA4A_Coritana_Hizon.py` | Part A: Knowledge base + Rule-Based Reasoning |
| `TA4B_Coritana_Hizon.py` | Part B: Case-Based Reasoning (interactive) |
| `TA4_Coritana_Hizon_docx.pdf` | Documentation, screenshots, and comparative reflection |


## How to Run

```bash
python TA4A_Coritana_Hizon.py   # RBR (no input needed)
python TA4B_Coritana_Hizon.py   # CBR (answers y/n questions)
```

---

## Part A: Knowledge Representation + RBR

### Knowledge Base

Facts are stored in a nested dictionary with three categories:

| Category | Facts |
|----------|-------|
| `power` | `powers_on`, `battery_level` (%), `is_plugged_in` |
| `thermal` | `temperature_c`, `fan_noise` (`"normal"` or `"loud"`) |
| `display` | `screen_on`, `screen_flickering`, `storage_free_gb` |

### Rules (IF–THEN)

Each rule is a function that returns an action if its condition holds, or `None` otherwise.

| Rule | IF | THEN |
|------|----|------|
| `rule_no_power` | not powered on and not plugged in | Plug in the charger and check the power outlet |
| `rule_low_battery` | battery < 20% and not plugged in | Battery is low - plug in the charger |
| `rule_overheating` | CPU temp > 85 °C | Close heavy programs and place the laptop on a cooling pad |
| `rule_loud_fan` | fan noise is `"loud"` | Clean the fan and air vents from dust |
| `rule_flicker` | screen is flickering | Update the graphics/display driver |
| `rule_low_storage` | free storage < 10 GB | Delete unused files or run Disk Cleanup |


## Part B: Case-Based Reasoning

### Case Base

Four past laptop problems, each with five yes/no features and a solution:

| Case | Features that are `True` | Solution |
|------|--------------------------|----------|
| 1 | `wont_turn_on` | Check the power cable and charger. |
| 2 | `overheating`, `loud_fan`, `slow` | Clean the fan and vents, then use a cooling pad. |
| 3 | `slow` | Free up disk space and remove startup programs. |
| 4 | `screen_flicker` | Update the display driver. |

### The 4R Cycle

| Step | Function | What it does |
|------|----------|--------------|
| **Retrieve** | `similarity()`, `retrieve()` | Score = matching features ÷ 5. Returns the highest-scoring case (the first one wins ties). |
| **Reuse** | `reuse()` | Takes the solution of the retrieved case. |
| **Revise** | `revise()` | Shows the suggested solution. The user may type a new one or press Enter to keep it. |
| **Retain** | `retain()` | Appends the new problem and final solution to `case_base`. |

User input is validated by `get_yes_no()`, which accepts `y`/`yes`/`n`/`no` and re-prompts on anything else.

## RBR vs CBR (Summary of Reflection)

| Question | Answer |
|----------|--------|
| Easier to implement? | **RBR.** Rules are simple IF–THEN functions and the engine is one loop. CBR needs a case base, a similarity function, and the full 4R cycle. |
| More flexible for unstructured problems? | **CBR.** It needs no rule for every situation, and retrieves the closest past case when there is no exact match. |
| Better for continuously changing data? | **RBR.** Rules are re-evaluated against current facts every run (e.g., CPU temperature, battery level). |


