import pandas as pd
df = pd.read_csv('final_food_delivery_dataset.csv')
df.columns = df.columns.str.strip()

# 1. Total orders placed by users with Gold membership
gold_orders = len(df[df['membership'] == 'Gold'])

# 2. Total revenue generated from Hyderabad (rounded to nearest integer)
hyd_rev = round(df[df['city'] == 'Hyderabad']['total_amount'].sum())

# 3. How many distinct users placed at least one order?
distinct_users = df['user_id'].nunique()

# 4. Average order value for Gold members (rounded to 2 decimals)
gold_aov = round(df[df['membership'] == 'Gold']['total_amount'].mean(), 2)

# 5. How many orders were placed for restaurants with rating >= 4.5?
high_rating_orders = len(df[df['rating'] >= 4.5])

# 6. How many orders were placed in the top revenue city among Gold members only?
gold_df = df[df['membership'] == 'Gold']
top_city = gold_df.groupby('city')['total_amount'].sum().idxmax()
top_city_gold_orders = len(gold_df[gold_df['city'] == top_city])

# Printing Results
print(f"1. Total Gold Orders: {gold_orders}")
print(f"2. Hyderabad Total Revenue: {hyd_rev}")
print(f"3. Distinct Users Count: {distinct_users}")
print(f"4. Gold Member AOV: {gold_aov}")
print(f"5. Rating >= 4.5 Orders: {high_rating_orders}")
print(f"6. Orders in Top Gold City ({top_city}): {top_city_gold_orders}")