import random
import csv
from datetime import datetime, timedelta

#Function to generate random dates
def generate_random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

#Function to generate a random sales data CSV
def generate_random_csv(file_name, num_rows):
    #Define sample data for randomization
    products = ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard", "Mouse"]
    categories = ["Electronics", "Accessories", "Mobile"]
    regions = ["North", "South", "East", "West"]

    #Define date range
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)

    #Open the CSV file for writing
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)

        #Write header row
        writer.writerow(["Date", "Product", "Category", "Region", "Sales"])

        #Generate and write random rows
        for _ in range(num_rows):
            date = generate_random_date(start_date, end_date).strftime("%Y-%m-%d")
            product = random.choice(products)
            category = random.choice(categories)
            region = random.choice(regions)
            sales = round(random.uniform(10.0, 1000.0), 2) #Random sales amount

            writer.writerow([date, product, category, region, sales])

    print(f"Random CSV file '{file_name}' with {num_rows} rows generated successfully.")

#Example usage
file_name = "sales_data.csv"
num_rows = 500 #Number of rows to generate
generate_random_csv(file_name, num_rows)