import argparse

import config
from pipeline.loader import DataLoader
from pipeline.transformer import DataTransformer
from pipeline.reporter import Reporter

def main():
  parser = argparse.ArgumentParser(description='CSV Pipline CLI')

  parser.add_argument('-i', '--input', help='Path to input file')
  parser.add_argument('-o', '--output', help='Path to output directory')
  parser.add_argument('-d', '--drop-na', help='Drop na from csv file', action="store_true")
  parser.add_argument('-n', '--normalize', help='Normalize numeric and categorical columns', action="store_true")

  try:
    args = parser.parse_args()

    # Load the data
    loader = DataLoader(args.input or config.INPUT_FILE)
    df_init = loader.load()

    # Transform the data
    transformer = DataTransformer(df_init, drop_na=args.drop_na, normalize=args.normalize)
    df_final = transformer.transform()

    # Write data report
    reporter = Reporter(df_init, df_final, output_dir=(args.output or config.OUTPUT_DIR))
    reporter.report()

  except Exception as e:
    print(f'Pipeline failed: {e}')

if __name__ == "__main__":
    main()
