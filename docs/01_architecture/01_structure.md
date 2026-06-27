# Project Structure

## Repository Tree

```plaintext
project_suspicious_sensor/
├── .gitignore                             # Comprehensive Python/data/IDE ignore rules
├── .python-version                        # Python 3.12 version pin
├── main.py                                # CLI entry point stub
├── pyproject.toml                         # Project metadata and dependencies
├── uv.lock                                # UV lockfile for reproducible environments
├── README.md                              # Project overview and learning objectives
│
├── data/
│   └── raw/
│       └── pressure_sensor_readings.csv   # 72 hourly pressure readings (2026-05-01 to 2026-05-03)
│
├── docs/
│   ├── 00_overveiw/
│   │   ├── 01_problem_statement.md        # Problem scenario and five-part analysis framework
│   │   ├── 02_data.md                     # Dataset description and column definitions
│   │   └── 03_docstring_template.md       # Google-style docstring standards
│   │
│   ├── 01_architecture/
│   │   └── 01_structure.md                # This file — directory layout and organization rationale
│   │
│   └── 02_strategy/
│       └── 01_descriptive_statistics_strategy.md  # 10-step analysis workflow and utility design
│
├── notebooks/
│   └── 01_descriptive_statistics.ipynb    # Exploratory data analysis notebook
│
├── src/suspicious_sensor
│   └── utils/
│       ├── __init__.py                    # Package init
│       └── descriptive_stats_funtions.py  # Data loading and statistics utilities
│
└── tests/
    └── __init__.py                        # Test package init (empty)
```

## Directory Rationale

| Directory                      | Purpose |
|--------------------------------|---------|
| `data/raw/`                    | Immutable source data; never modified in place |
| `docs/`                        | Human-readable documentation organized by topic |
| `notebooks/`                   | Exploratory analysis and visualization (not production code) |
| `src/suspicious_sensor/utils/` | Reusable, testable Python utility functions extracted from notebooks |
| `tests/`                       | Unit tests for `src/` modules |

## Key Files

| File                                                        | Role |
|-------------------------------------------------------------|------|
| `pyproject.toml`                                            | Declares dependencies (numpy, pandas, matplotlib, seaborn, ipykernel) and Python ≥3.12 |
| `uv.lock`                                                   | Pins exact transitive dependency versions for reproducibility |
| `src/suspicious_sensor/utils/descriptive_stats_funtions.py` | `load_data(filename)` — loads a CSV from `data/raw/` into a DataFrame |
| `data/raw/pressure_sensor_readings.csv`                     | 72 rows: `timestamp`, `pressure_psi` (range 64.9–83.6 psi) |

## Conventions

- **Utilities first**: analysis logic is extracted from notebooks into `src/utils/` to keep notebooks clean and enable testing.
- **Raw data is read-only**: processed or derived datasets would live under `data/processed/` (gitignored).
- **Numbered docs**: prefixes (`00_`, `01_`, `02_`) reflect the intended reading/execution order.
