import argparse
from rich.console import Console
from rich.progress import Progress
from rich.markup import escape

import config
from pipeline.loader import DataLoader
from pipeline.transformer import DataTransformer
from pipeline.reporter import Reporter

def main():
  parser = argparse.ArgumentParser(description='CSV Pipeline CLI')
  parser.add_argument('-i', '--input', help='Path to input file')
  parser.add_argument('-o', '--output', help='Path to output directory')
  parser.add_argument('-d', '--drop-na', help='Drop rows with null values', action='store_true')
  parser.add_argument('-n', '--normalize', help='Normalize and encode columns', action='store_true')

  try:
    args = parser.parse_args()

    # Get CLI args
    input_file = args.input or config.INPUT_FILE
    output_dir = args.output or config.OUTPUT_DIR
    drop_na    = args.drop_na
    normalize  = args.normalize
    
    # Set up console
    console = Console()
    console.rule('[bold]CSV Pipeline[/bold]')
    console.print()

    # Run pipeline in steps w/ progress
    steps = ["Loading", "Transforming", "Reporting"]
    df_init, df_final, ps_report = None, None, None

    with Progress() as progress:
      task = progress.add_task("[cyan]Starting...", total=len(steps))
      for step in steps:
        progress.update(task, description=f"{step}...")
        match step:
          case "Loading":
            loader = DataLoader(input_file)
            df_init = loader.load()
          case "Transforming":
            transformer = DataTransformer(df_init, drop_na=drop_na, normalize=normalize)
            df_final = transformer.transform()
          case "Reporting":
            reporter = Reporter(df_init, df_final, output_dir)
            ps_report = reporter.report()
        progress.advance(task)

      progress.update(task, description="Done")
      progress.advance(task)

    console.print("\n[bold]Summary[/bold]\n")
    console.print(ps_report)
    console.print("[bold]Preview[/bold]\n")
    console.print(df_final.iloc[:20, :8])

  except Exception as e:
    console.print(f'[red]Pipeline failed:[/red] {escape(str(e))}')

if __name__ == '__main__':
  main()
