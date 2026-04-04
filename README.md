# CSV Pipeline

## Description

A simple data pipeline built in Python. It loads a CSV, cleans and normalizes the data, and writes the output along with a terminal summary report. Built as a hands-on project to practice Python class design, pandas, and CLI tooling.

## App Structure
```
csv-pipeline/
├── pipeline/
│   ├── __init__.py
│   ├── loader.py
│   ├── transformer.py
│   └── reporter.py
├── data/
│   └── healthcare_data.csv
├── output/
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

## Classes

### DataLoader
Reads and validates a CSV file. Checks the file extension and verifies the header columns match what's defined in `config.py` before loading it into a DataFrame.

### DataTransformer
Cleans the DataFrame based on flags passed at runtime. Optionally drops rows with null values, min-max scales numeric columns, and encodes categoricals — one-hot for nominal columns, ordinal for ordered ones. Column config is defined in `config.py`.

### Reporter
Builds a Rich summary table of pipeline stats (row counts, drops, features encoded), appends a plain text version to a log file, and saves the cleaned DataFrame as a timestamped CSV in the output directory.

## Usage

Install dependencies:
```bash
pip install -r requirements.txt
```

Run with defaults (uses `config.py` values):
```bash
python main.py
```

With flags:
```bash
python main.py -i data/healthcare_data.csv -o output/ -d -n
```

| Flag | Description |
|------|-------------|
| `-i` | Path to input CSV (default: `data/healthcare_data.csv`) |
| `-o` | Output directory (default: `output/`) |
| `-d` | Drop rows with null values |
| `-n` | Normalize and encode columns |

## Docker

### Build
```bash
docker build -t csv-pipeline .
```

### Run interactive shell
```bash
docker run -it -v $(pwd):/app csv-pipeline
```

### Run program
```bash
python main.py
```
