# Sample data: replace this with your actual data processing logic
import pandas as pd

data = {
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C'],
    'Output': [10.5, 12.3, 14.1]
}
df = pd.DataFrame(data)

# Saving to a new CSV file
output_filename = 'newoutput.csv'  # Specify the new CSV file name
df.to_csv("C:/Users/PSL/task2\Employee-Data-Analysis--Filtering--Averaging--and-Date-Conversions/newoutput.csv")  # Save DataFrame to CSV