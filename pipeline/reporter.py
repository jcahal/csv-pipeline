from datetime import datetime as dt
from rich.text import Text
from rich.table import Table

class Reporter:
  def __init__(self, df_init, df_final, output_dir):
    self.df_init      = df_init
    self.df_final     = df_final
    self.output_dir   = output_dir
    self.report_time  = dt.now()

  def report(self):
    timestamp = self.report_time.strftime("%Y-%m-%d_%H-%M-%S")
    csv_path = f"{self.output_dir}cleaned_{timestamp}.csv"

    # Rich console summary
    initial_rows = self.df_init.shape[0]
    final_rows = self.df_final.shape[0]
    dropped_rows = initial_rows - final_rows
    added_cols = self.df_final.shape[1] - self.df_init.shape[1]
    
    summary = Text()
    summary.append(f"  Summary -  {timestamp}\n\n", style="bold")
    summary.append(f"  {'Initial rows':<18}{initial_rows:>10,}\n")
    summary.append(f"  {'Final rows':<18}{final_rows:>10,}\n")
    summary.append(f"  {'Rows dropped':<18}{dropped_rows:>10,}\n")
    summary.append(f"  {'Features encoded':<18}{added_cols:>10,}\n\n")
    summary.append(f"  Saved to {csv_path}\n\n")

    summary_table = Table(padding=(0, 4))

    summary_table.add_column("Initial rows")
    summary_table.add_column("Final rows")
    summary_table.add_column("Rows dropped")
    summary_table.add_column("Features encoded")
    summary_table.add_column("Saved to")

    summary_table.add_row(
        f"{initial_rows:,}",
        f"{final_rows:,}",
        f"{dropped_rows:,}",
        f"{added_cols:,}",
        csv_path
    )

    # Write to log file
    try:
      with open(f'{self.output_dir}log.txt', 'a') as log_file:
        log_file.write(summary.plain)
    except IOError as e:
      raise ValueError(f'Failed to write log file: {e}')

    # Save the cleaned DataFrame to a timestamped CSV
    try:
      self.df_final.to_csv(csv_path, index=False)
    except Exception as e:
      raise ValueError(f'Failed to save CSV: {e}')
    
    return summary_table
