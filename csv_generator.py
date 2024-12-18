import random
import string
import pandas as pd
import datetime

def generate_random_data(data_type, num_samples, min_value=None, max_value=None, 
                        length=None, charset=None):
  """
  Generates random data of the specified type.

  Args:
    data_type: The type of data to generate. 
              Supported types: 'int', 'float', 'string', 'bool', 'date'
    num_samples: The number of samples to generate.
    min_value: The minimum value for numerical data.
    max_value: The maximum value for numerical data.
    length: The length of the string to generate.
    charset: The characters to use for string generation. 

  Returns:
    A list containing the generated random data.
  """

  data = []
  for _ in range(num_samples):
    if data_type == 'int':
      data.append(random.randint(min_value, max_value))
    elif data_type == 'float':
      data.append(random.uniform(min_value, max_value))
    elif data_type == 'string':
      if charset is None:
        charset = string.ascii_letters + string.digits
      data.append(''.join(random.choice(charset) for _ in range(length)))
    elif data_type == 'bool':
      data.append(random.choice([True, False]))
    elif data_type == 'date':
      start_date = datetime.date(2000, 1, 1)
      end_date = datetime.date(2024, 12, 31)  # Adjust as needed
      time_between_dates = end_date - start_date
      days_between_dates = time_between_dates.days
      random_number_of_days = random.randrange(days_between_dates)
      random_date = start_date + datetime.timedelta(days=random_number_of_days)
      data.append(random_date)
    else:
      raise ValueError(f"Unsupported data type: {data_type}")

  return data

def generate_random_dataframe(columns, num_rows, **kwargs):
  """
  Generates a pandas DataFrame with random data.

  Args:
    columns: A list of dictionaries, where each dictionary represents a column:
             - 'name': The name of the column.
             - 'type': The data type of the column ('int', 'float', 'string', 'bool', 'date').
             - Additional arguments for the `generate_random_data` function.
    num_rows: The number of rows in the DataFrame.

  Returns:
    A pandas DataFrame with the generated random data.
  """

  data = {}
  for col in columns:
    data[col['name']] = generate_random_data(**col)

  return pd.DataFrame(data)

# Example usage:
columns = [
    {'name': 'id', 'type': 'int', 'min_value': 1, 'max_value': 1000},
    {'name': 'name', 'type': 'string', 'length': 10},
    {'name': 'age', 'type': 'int', 'min_value': 18, 'max_value': 65},
    {'name': 'salary', 'type': 'float', 'min_value': 30000, 'max_value': 150000},
    {'name': 'active', 'type': 'bool'}
]

df = generate_random_dataframe(columns, num_rows=100)

# Export to CSV
df.to_csv('random_data.csv', index=False) 