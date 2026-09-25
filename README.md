# Early Warning Tool

A KNIME Analytics Platform workflow that predicts whether a student is **"At Risk"** or **"Not At Risk"** of falling behind, based on attendance and academic performance data.

## Overview

This tool uses classic supervised machine learning to flag students who may need academic intervention early in the term. It reads student performance data, normalizes the features, trains three different classification models in parallel, and scores each model's predictions against a held-out test set so the results can be compared side by side.

## Dataset

**File:** `student_performance_knime.csv`

| Column | Description |
|---|---|
| `student_id` | Unique student identifier |
| `attendance` | Attendance percentage |
| `quiz_score` | Average quiz score |
| `assignment_score` | Average assignment score |
| `exam_score` | Exam score |
| `risk_status` | Target label — `At Risk` or `Not At Risk` |

## Workflow Structure

**File:** `DemoEarlyWarningTool.knwf`

```
CSV Reader → Column Filter → Normalizer → Table Partitioner
                                                 │
                        ┌────────────────────────┼────────────────────────┐
                        ▼                        ▼                        ▼
              Decision Tree Learner   Logistic Regression Learner   Random Forest Learner
                        │                        │                        │
                        ▼                        ▼                        ▼
             Decision Tree Predictor  Logistic Regression Predictor  Random Forest Predictor
                        │                        │                        │
                        ▼                        ▼                        ▼
                     Scorer                   Scorer                   Scorer
```

1. **CSV Reader** – loads the raw student data.
2. **Column Filter** – removes non-predictive columns (e.g. `student_id`) before modeling.
3. **Normalizer** – scales numeric features to a common range.
4. **Table Partitioner** – splits the data into training and test sets.
5. **Three parallel model branches** – Decision Tree, Logistic Regression, and Random Forest are each trained on the same partitioned data so their performance can be compared.
6. **Scorer nodes** – compare each model's predictions against the true `risk_status` labels and output a confusion matrix and accuracy statistics.

## Results

On the held-out test partition, the models correctly separated the two classes, as shown in the confusion matrix output from the Scorer nodes:

| | Predicted: Not At Risk | Predicted: At Risk |
|---|---|---|
| **Actual: Not At Risk** | 3 | 0 |
| **Actual: At Risk** | 0 | 3 |

Full node-by-node outputs and screenshots are documented in `EarlyWarningTool_Evidence_.pdf`.

## Files in this Repo

| File | Description |
|---|---|
| `DemoEarlyWarningTool.knwf` | The exported KNIME workflow (importable into KNIME Analytics Platform) |
| `student_performance_knime.csv` | Sample dataset used to train/test the models |
| `EarlyWarningTool_Evidence_.pdf` | Screenshots of the executed workflow and results |

## How to Run

1. Install [KNIME Analytics Platform](https://www.knime.com/downloads).
2. In KNIME, go to **File → Import KNIME Workflow...** and select `DemoEarlyWarningTool.knwf`.
3. Open the **CSV Reader** node and point it to `student_performance_knime.csv` on your machine.
4. Right-click the workflow and select **Execute All**.
5. Click on any **Scorer** node and open its **Confusion Matrix** / **Accuracy Statistics** view to inspect results.

## Notes

- This is a small demo dataset (30 rows), intended to illustrate the workflow and modeling approach rather than to produce a production-grade model.
- Because the sample size is small, the perfect confusion matrix results should be interpreted as a proof of concept, not a guarantee of real-world accuracy.
