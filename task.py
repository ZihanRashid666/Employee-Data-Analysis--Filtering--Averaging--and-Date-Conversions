import pandas as pd

# Existing data
data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['John Doe', 'Stuart Broad', 'Jane Smith', 'Michale', 'Zihan', 'Sara', 'Imran', 'Shakib', 'Labib', 'Farhan'],
    'Department': ['Engineering', 'Sales', 'Marketing', 'Engineering', 'Sales', 'Sales', 'Marketing', 'Engineering', 'Sales', 'Engineering'],
    'Salary': [50000, 60000, 70000, 50000, 55000, 45000, 30000, 75000, 60000, 29000],
    'JoiningDate': ['10/1/2022', '9/2/2023', '10/1/2022', '9/2/2023', '9/3/2023', '9/4/2023', '9/5/2023', '9/6/2023', '9/7/2023', '9/8/2023']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the extended data to CSV
csv_file_path = 'C:/Users/PSL/task2/Employee-Data-Analysis--Filtering--Averaging--and-Date-Conversions/newoutput.csv'
df.to_csv(csv_file_path, index=False)

print(f'CSV file has been saved to {csv_file_path}')
