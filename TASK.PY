import pandas as pd
from datetime import datetime

#Answer to Question No.1

df = pd.read_csv("C:/TaskOffice/employeesSheet1.csv", index_col=0)
filtered_df = df[(df['Department'] == 'Engineering') | (df['Salary'] > 60000)]

print(filtered_df)

#Answer to Question No.2

average_salary_all=df['Salary'].mean()
average_salary_byDepartment=df.groupby('Department')['Salary'].mean()


print(f'Average Salary of all employess:{average_salary_all}')
print(f'Average Salary for specific Department:{average_salary_byDepartment}')

#Answer to Question No.3

df['JoiningDate'] = pd.to_datetime(df['JoiningDate'], format='%m/%d/%Y')
df['FormattedJoiningDate'] = df['JoiningDate'].dt.strftime('%d-%m-%Y')
current_date = pd.to_datetime(datetime.now())
df['YearsWithCompany'] = (current_date - df['JoiningDate']).dt.days / 365.25  

print(df[['JoiningDate', 'FormattedJoiningDate', 'YearsWithCompany']])

