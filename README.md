# CSV Pipeline

## Description

A simple data pipeline built in Python. It loads a CSV, cleans and normalizes the data, and writes the output along with a summary report. Built as a hands-on project to practice Python class design, pandas, and CLI tooling.

## App Structure
```
csv-pipeline/
├── pipeline/
│   ├── __init__.py
│   ├── loader.py
│   ├── transformer.py
│   └── reporter.py
├── data/
│   └── sample.csv
├── output/
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

## Classes

### DataLoader
Reads and validates a CSV file. Checks the file extension and verifies the header columns match what's expected before loading it into a DataFrame.

### DataTransformer
Cleans the DataFrame. Optionally drops rows with null values and normalizes numeric columns using min-max scaling. Encodes categorical columns using one-hot and ordinal encoding.

### Reporter
Prints a summary of what changed (row counts, nulls dropped, columns before/after), appends it to a log file, and saves the cleaned DataFrame as a timestamped CSV in the output directory.

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
python main.py -i data/sample.csv -o output/ -d -n
```

| Flag | Description |
|------|-------------|
| `-i` | Path to input CSV (default: `data/sample.csv`) |
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
