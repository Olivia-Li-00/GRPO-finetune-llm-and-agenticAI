# Coursework Repository

This repository contains the Part I Sections 1-3 implementation and results analysis, as well as the coursework figures and report, for A8.

4 versions exist, v1 for base model gemma-3-1b-it and baseline training reproduction, v2-4 for algorithmic and reward improvements.

## Team
- Team: chlina
- Members: zl656, un212, xc401

## Key Repository Contents

- `report/`: contains the coursework report.
- `figures/`: contains the generated figures used in the report.
- `figure.ipynb`: the jupyter notebook used to generate the report figures for Part I Sections 1-3.
- `measurement/`: contains the selected W&B CSV files for results analysis.
- `scripts/`: contains the code implementation for Part I Section 1-3.
- `OLD_README.md`: the original setup guide.

## Reproducing Figures for Part I Sections 1-3

The report figures can be reproduced locally from the saved W&B CSV files in `measurement/`.

Setting up and activate the python virtual environment, and open VScode:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install pandas matplotlib ipykernel
code .
```

Run all cells in `figure.ipynb` to reproduce the 3 figures in `figures/` that's part of the coursework Part I Sections 1-3.

Or alternatively, install and work in jupyterlab instead.

## Versions and Tags

| Git&nbsp;tag | Version | Logs in tag | Exact acc. [95% CI] | Partial acc. [95% CI] | Format acc. [95% CI] |
|---|---|---|---:|---:|---:|
| `v1` | Base model gemma-3-1b-it | `baseline_evaluate.log` | 39.06% [28.12%, 51.56%] | 40.62% [29.69%, 53.12%] | 4.69% [0.00%, 10.94%] |
| `v1` | Baseline (K=2 + original reward) | `baseline_train.log`, `LoRA_evaluate.log` | 32.81% [21.88%, 43.75%] | 32.81% [21.88%, 43.75%] | 82.81% [73.44%, 92.19%] |
| `v2` | Greater group size (K=8 + original reward) | `improve_k8.log`, `improve_k8_evaluate.log` | 62.50% [51.56%, 73.44%] | 64.06% [51.56%, 75.00%] | 95.31% [89.06%, 100.00%] |
| `v3` | Format downweight (K=8 + format downweight) | `improve_reward_reweighted_ef0-5_af0-5.log`, `improve_reward_reweighted_ef0-5_af0-5_evaluate.log` | 59.38% [48.44%, 70.31%] | 59.38% [48.44%, 70.31%] | 87.50% [79.69%, 95.31%] |
| `v4` | Reward recalibration(K=8 + reward recalibration) | `improve_reward_reweighted_v2.log`, `improve_reward_reweighted_v2_evaluate.log` | 45.31% [34.38%, 57.81%] | 48.44% [35.94%, 60.94%] | 82.81% [71.88%, 92.19%] |

Metrics are from greedy evaluation on the same fixed 64 samples from the GSM8K test  (seed=100), with 95% percentile bootstrap confidence intervals reported (2000 resamples).

## Declaration of AI Tools

AI tools were used to discuss mathematical and theoretical background, LaTex conversion, and syntax troubleshooting.