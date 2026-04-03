INPUT_FILE = 'data/healthcare_data.csv'
OUTPUT_DIR = 'output/'

COLUMNS = ['Available Extra Rooms in Hospital', 'Department', 'Ward_Facility_Code', 'doctor_name', 'staff_available', 'patientid', 'Age', 'gender', 'Type of Admission', 'Severity of Illness', 'health_conditions', 'Visitors with Patient', 'Insurance', 'Admission_Deposit', 'Stay (in days)']

# Continuous numeric columns
NUMERICAL_COLS = ['Available Extra Rooms in Hospital', 'staff_available', 'Visitors with Patient', 'Admission_Deposit', 'Stay (in days)']

# Nominal categoricals
ONE_HOT_ENCODING = {
  'Department': 'dept',
  'Ward_Facility_Code': 'ward',
  'doctor_name': 'doctor',
  'gender': 'gender',
  'Type of Admission': 'admission_type',
  'health_conditions': 'condition',
  'Insurance': 'insurance'
}

# Ordinal categoricals
ORDINAL_ENCODING = {
  'Age': {'0-10': 0, '11-20': 1, '21-30': 2, '31-40': 3, '41-50': 4, '51-60': 5, '61-70': 6, '71-80': 7, '81-90': 8, '91-100': 9},
  'Severity of Illness': {'Minor': 0, 'Moderate': 1, 'Extreme': 2}
}
