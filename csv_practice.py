#Reflection 
#1: doing an ETL pipeline is Python allows for automated , repeatable data cleaning and 
#transformation at scale, whereas Excel relied heavily on manual intervention or fragile macros. 
# Python handles massive datsets effortlessly without row-limit crashes, through Excel is much 
# faster for quick ad-hoc visual formatting and manual data exploration.
#2 An e-commerce inventory audit log would greatly benefit from and append-mode log file. Append 
# mode ensures that every time stockadjustments run, new entries are safely added at the end without 
# overwriting historical audit records.


#Exercise 1
import csv
from datetime import datetime

#Exercise 2
print("--- Exercise 2: Raw Rows ---")
with open("data/sales.csv", mode="r", encoding="utf-8") as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)

#Exercise 3 

with open("data/sales.csv", mode="r", encoding="utf-8") as file:
  reader = csv.reader(file)
  header = next(reader)
  print("Header:", header)
  for row in reader:
    print(row)

#Exercise 4
total_revenue = 0
with open("data/sales.csv", mode="r", encoding="utf-8") as file:
  reader = csv.reader(file)
  next(reader)
  for row in reader:
    product, price_str, qty_str = row
    price = float(price_str)
    quantity = int (qty_str)
    line_total = price * quantity
    total_revenue += line_total
    print(f"{product}: {quantity} units x ${price:.2f} = ${line_total:.2f}")

print(f"Overall Total Revenue: ${total_revenue:.2f}")

#Exercise 5
original_count = 0
written_count = 0

with open("data/sales.csv", mode="r", encoding="utf-8") as infile, open ("data/cleaned.csv", mode="w", newline="", encoding="utf-8" ) as outfile:
  reader = csv.reader(infile)
  writer = csv.writer(outfile)

  header = next(reader)
  writer.writerow(["Product", "Price", "Qty", "Total"])

  for row in reader:
    original_count += 1
    product, price_str, qty_str = row
    price = float(price_str)
    quantity = int(qty_str)
    line_total = price * quantity

    if line_total > 100:
      writer.writerow([product, f"{price:.2f}", quantity, f"{line_total:.2f}"])
      written_count += 1

print(f"Original rows: {original_count}, Cleaned rows written: {written_count}")

#Exercise 6 
dict_total_revenue = 0
with open("data/sales.csv", mode="r", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  for row in reader:
    price = float(row["price"])
    quantity = int(row["quantity"])
    dict_total_revenue += price * quantity
print(f"DictReader Total Revenue: ${dict_total_revenue:.2f}")

#Exercise 7 
product_summary = {}
with open("data/sales.csv", mode="r", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  for row in reader:
    product = row["product"]
    revenue = float(row["price"]) * int(row["quantity"])
    product_summary[product] = product_summary.get(product,0) + revenue

for prod in sorted(product_summary.keys()):
  print(f"{prod}: ${product_summary[prod]:.2f}")

#Exercise 8 
with open("data/run_log.txt", mode="a", encoding="utf-8") as log_file:
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  log_file.write(f"{timestamp} - Total Revenue: ${total_revenue:.2f}\n")
print("Run logged successfully to data/run_log.txt")

  

      