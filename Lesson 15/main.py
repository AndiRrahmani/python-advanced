# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
# Replace 'temperature_data.csv' with your actual file name
df = pd.read_csv('temperature_data.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# ---------------------------------------------------
# 1. Temperature Overview
# ---------------------------------------------------

average_temp = df['Temperature'].mean()

print("1. Average Temperature")
print(f"Average Temperature: {average_temp:.2f}")

# ---------------------------------------------------
# 2. Monthly Temperature
# ---------------------------------------------------

# Extract month name
df['Month'] = df['Date'].dt.month_name()

# Calculate monthly average temperature
monthly_avg = df.groupby('Month')['Temperature'].mean()

print("\n2. Monthly Average Temperature")
print(monthly_avg)

# Bar Plot
plt.figure(figsize=(10,5))
monthly_avg.plot(kind='bar', color='skyblue')

plt.title('Monthly Average Temperature')
plt.xlabel('Month')
plt.ylabel('Average Temperature')
plt.xticks(rotation=45)

plt.show()

# ---------------------------------------------------
# 3. Highs and Lows
# ---------------------------------------------------

# Hottest day
hottest_day = df.loc[df['Temperature'].idxmax()]

# Coldest day
coldest_day = df.loc[df['Temperature'].idxmin()]

print("\n3. Hottest Day")
print(hottest_day)

print("\n3. Coldest Day")
print(coldest_day)

# ---------------------------------------------------
# 4. Temperature Trends
# ---------------------------------------------------

# Line graph for temperature over time
plt.figure(figsize=(12,5))

plt.plot(df['Date'], df['Temperature'], color='red')

plt.title('Temperature Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature')

plt.grid(True)

plt.show()

# ---------------------------------------------------
# 4b. Seasonal Average Temperature
# ---------------------------------------------------

# Function to assign seasons
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

# Create Season column
df['Season'] = df['Date'].dt.month.apply(get_season)

# Seasonal averages
seasonal_avg = df.groupby('Season')['Temperature'].mean()

print("\n4b. Seasonal Average Temperature")
print(seasonal_avg)