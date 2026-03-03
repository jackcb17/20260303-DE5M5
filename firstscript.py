from pathlib import Path
import pandas as pd

root = Path.cwd()

data_dir = root/"data"
books = data_dir/"03_Library Systembook.csv"
customers = data_dir/"03_Library SystemCustomers.csv"

books_df = pd.read_csv(books)
cust_df = pd.read_csv(customers)

datb_cleaned = 
books_df["Days allowed to borrow"].str.replace(r"\bweeks\b","",regex = True)

bc_cleaned = 
books_df["Books checkout"].str.replace(r'^["\']|["\']$','', regex =True)

books_caps = books_df["Books"].str.title()

