import pandas as pd
df = pd.read_csv('final_food_delivery_dataset.csv')
df.columns = df.columns.str.strip()
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

# 1. City with highest total revenue from Gold members
gold_members = df[df['membership'].str.strip() == 'Gold']
city_rev = gold_members.groupby('city')['total_amount'].sum()
print(f"1. Highest Revenue City (Gold): {city_rev.idxmax()}")

# 2. Cuisine with highest average order value
cuisine_avg = df.groupby('cuisine')['total_amount'].mean()
print(f"2. Highest Avg Order Value Cuisine: {cuisine_avg.idxmax()}")

# 3. Distinct users with total orders > ₹1000
user_totals = df.groupby('user_id')['total_amount'].sum()
count_1000 = (user_totals > 1000).sum()
print(f"3. Users with total orders > ₹1000: {count_1000}")

# 4. Rating range with highest revenue
bins = [3.0, 3.5, 4.0, 4.5, 5.0]
labels = ['3.0 – 3.5', '3.6 – 4.0', '4.1 – 4.5', '4.6 – 5.0']
df['rating_range'] = pd.cut(df['rating'], bins=bins, labels=labels, include_lowest=True)
rating_rev = df.groupby('rating_range')['total_amount'].sum()
print(f"4. Highest Revenue Rating Range: {rating_rev.idxmax()}")

# 5. Highest AOV for Gold members by city
gold_city_aov = gold_members.groupby('city')['total_amount'].mean()
print(f"5. Highest Gold AOV City: {gold_city_aov.idxmax()}")

# 6. Cuisine with lowest distinct restaurants but high revenue
cuisine_stats = df.groupby('cuisine').agg(
    unique_restaurants=('restaurant_id', 'nunique'),
    total_rev=('total_amount', 'sum')
)
print("\n6. Cuisine Comparison (Lowest count vs high revenue):")
print(cuisine_stats.sort_values(by='unique_restaurants'))

# 7. Percentage of total orders by Gold members
gold_pct = (len(gold_members) / len(df)) * 100
print(f"\n7. Percentage of Gold Orders: {round(gold_pct)}%")

# 8. Restaurant with highest AOV but < 20 orders
res_stats = df.groupby('restaurant_name_x').agg(
    avg_val=('total_amount', 'mean'), 
    order_count=('total_amount', 'count')
)
small_res = res_stats[res_stats['order_count'] < 20]
print(f"8. Highest AOV Restaurant (<20 orders): {small_res['avg_val'].idxmax()}")

# 9. Highest revenue combination (Membership + Cuisine)
combo_rev = df.groupby(['membership', 'cuisine'])['total_amount'].sum()
print(f"9. Top Revenue Combo: {combo_rev.idxmax()}")

# 10. Highest Revenue Quarter
df['quarter'] = df['order_date'].dt.to_period('Q')
quarter_rev = df.groupby('quarter')['total_amount'].sum()
print(f"10. Highest Revenue Quarter: {quarter_rev.idxmax()}")