import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Day of week analysis.
# Data source URL: https://uk.investing.com/crypto/bitcoin/historical-data
df = pd.read_csv("Data/daily_historic_bitcoin_price_data.csv")

# Only keep columns that will be used.
df = df[["Price", "Date"]]

# Store the spot price of bitcoin as a float without comma separation of thousands.
df["Price"] = df["Price"].apply(lambda x: x.replace(",", ""))
df["Price"] = df["Price"].astype(float)

# Change date format, specify day of the week and week number.
df["Date"] = pd.to_datetime(df["Date"])
df["Day of week"] = df["Date"].dt.dayofweek.replace(
    [0, 1, 2, 3, 4, 5, 6],
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
)
df["Week number"] = df.index // 7


# Normalise price data at a weekly level.
agg_price_df = df.groupby("Week number").agg({"Price": ["min", "max"]})
agg_price_df["Week number"] = agg_price_df.index
df = df.join(agg_price_df, on="Week number", rsuffix="_week_avg", how="outer")
df["Norm week price"] = (df["Price"] - df[("Price", "min")]) / (df[("Price", "max")] - df[("Price", "min")])

# Show which days of the week most frequently have the highest and lowest bitcoin prices with a violin plot.
ax = sns.violinplot(x="Day of week", y="Norm week price", data=df)
plt.title("Day of Week Analysis, 10 Years of Data")
# plt.show()

# Limit data to the last year and repeat the analysis.
df = df[:365]
ax = sns.violinplot(x="Day of week", y="Norm week price", data=df)
plt.title("Day of Week Analysis, 1 Year of Data")
# plt.show()


# Hour of day analysis.
# data source: https://www.cryptodatadownload.com/data/bitstamp/
df = pd.read_csv("Data/hourly_bitcoin_price_data.csv")

# Only keep columns that will be used.
df = df[["date", "open"]]

# Change date to python datetime format, specify hour of the day and day number.
df["date"] = pd.to_datetime(df["date"])
df["hour of day"] = df["date"].dt.hour
df["day number"] = df.index // 24

# Normalise price data at a daily level.
agg_price_df = df.groupby("day number").agg({"open": ["min", "max"]})
agg_price_df["day number"] = agg_price_df.index
df = df.join(agg_price_df, on="day number", rsuffix="_day_avg", how="outer")
df["norm day price"] = (df["open"] - df[("open", "min")]) / (df[("open", "max")] - df[("open", "min")])

# Show which days of the week most frequently have the highest and lowest bitcoin prices with a violin plot.
ax = sns.violinplot(x="hour of day", y="norm day price", data=df)
plt.title("Hour of Day Analysis, 4+ Years of Data")
plt.show()

# Limit data to the last year and repeat the analysis.
df = df[:365*24]
ax = sns.violinplot(x="hour of day", y="norm day price", data=df)
plt.title("Day of Week Analysis, 1 Year of Data")
plt.show()


# Hour of week analysis.
# Add day of week as a column.
df["day of week"] = df["date"].dt.dayofweek.replace(
    [0, 1, 2, 3, 4, 5, 6],
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
)

# Create graphs using data filtered by each day of the week.
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    filtered_df = df[df["day of week"] == day]

    ax = sns.violinplot(x="hour of day", y="norm day price", data=filtered_df)
    plt.title(f"Hour of Day Analysis - {day}, 4+ Years of Data")
    plt.show()

    filtered_df = filtered_df[:52*24]
    ax = sns.violinplot(x="hour of day", y="norm day price", data=filtered_df)
    plt.title(f"Hour of Day Analysis - {day}, 1 Year of Data")
    plt.show()
