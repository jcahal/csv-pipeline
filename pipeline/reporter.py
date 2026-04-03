import os
from datetime import datetime as dt

class Reporter:
  def __init__(self, df_init, df_final, output_dir):
    self.df_init = df_init
    self.df_final = df_final
    self.report_time = dt.now()
    self.output_dir = output_dir
    
  def report(self):
    summary = f"""
========================================
  CSV Pipeline Report
  {self.report_time.strftime("%Y-%m-%d %H:%M:%S")}
========================================

ROWS
  Before : {self.df_init.shape[0]}
  After  : {self.df_final.shape[0]}
  Dropped: {self.df_init.shape[0] - self.df_final.shape[0]}

COLUMNS
  Before : {self.df_init.shape[1]}
  After  : {self.df_final.shape[1]}

NULLS DROPPED
  {self.df_init.isna().sum().sum() - self.df_final.isna().sum().sum()}

OUTPUT
  Saved to: output/cleaned_{self.report_time.strftime("%Y-%m-%d_%H-%M-%S")}.csv

========================================
"""

    print(summary)

    # Append report to the running log file
    try:
      with open('output/log.txt', 'a') as log_file:
        log_file.write(summary)
    except IOError as e:
      raise ValueError(f'Failed to write log file: {e}')

    # Save the cleaned DataFrame to a timestamped CSV
    try:
      self.df_final.to_csv(f'{self.output_dir}cleaned_{self.report_time.strftime("%Y-%m-%d_%H-%M-%S")}.csv', index=False)
    except Exception as e:
      raise ValueError(f'Failed to save CSV: {e}')
    
