import pandas as pd
import numpy as np

# Generate 5,000 days (~13.7 years)
days = pd.date_range(start="2010-01-01", periods=5000)
df = pd.DataFrame({'Date': days})

# Day of year (1 to 365)
day_of_year = df['Date'].dt.dayofyear
# Sinusoidal Seasonality: Highs in summer/winter, lows in spring/fall
seasonality = 10 * np.sin(2 * np.pi * day_of_year / 365.25)
# Growth Trend: 0.01 units of sales growth per day
trend = 0.02 * np.arange(len(df))

from faker import Faker
fake = Faker()

# Generate Ad Spend (Features)
df['TV'] = np.random.gamma(shape=2, scale=50, size=5000)      # Skewed distribution (common in ad spend)
df['Social'] = np.random.uniform(10, 200, size=5000)
df['Newspaper'] = np.random.exponential(scale=30, size=5000)

# Metadata
df['Campaign_Manager'] = [fake.name() for _ in range(5000)]
df['Region'] = [fake.city() for _ in range(5000)]

# Sales = Base + TV_Effect + Social_Effect + Seasonality + Trend + Noise
noise = np.random.normal(0, 5, size=5000)
df['Sales'] = (
    20 + 
    (df['TV'] * 0.35) + 
    (df['Social'] * 0.55) + 
    (df['Newspaper'] * 0.05) + 
    seasonality + 
    trend + 
    noise
)