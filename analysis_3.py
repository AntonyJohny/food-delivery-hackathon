import pandas as pd
import sqlite3
import json
orders = pd.read_csv('orders.csv')
with open('users.json', 'r') as f:
    users_data = json.load(f)
users = pd.DataFrame(users_data)
conn = sqlite3.connect(':memory:')
with open('restaurants.sql', 'r') as f:
    sql_script = f.read()
conn.executescript(sql_script)
restaurants = pd.read_sql_query("SELECT * FROM restaurants", conn)
merged_step1 = pd.merge(orders, users, on='user_id', how='left')
final_df = pd.merge(merged_step1, restaurants, on='restaurant_id', how='left')
final_df.columns = final_df.columns.str.strip()
final_df['order_date'] = pd.to_datetime(final_df['order_date'], dayfirst=True)
final_df.to_csv('final_food_delivery_dataset.csv', index=False)

#printing 3rd ans
print(f"Total Rows in Dataset: {len(final_df)}")