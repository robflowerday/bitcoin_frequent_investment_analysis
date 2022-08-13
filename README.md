# bitcoin_frequent_investment_analysis
Data analysis to determine the best day of week and hour of the day to invest in bitcoin on a weekly basis.

# Motivation
Determine the best time of the week to set-up an automated weekly investment in bitcoin in order to maximise future returns.

# Process
Split price data by the day of the week and the wek of the year, normalise data by week so that the data points can be visualised and compared over time and create violin plots of this data. If an hour of the day or day of the week show a particularly thick section on the graph at the top of the 'violin', this day or time has historically recorded a high itcoin spot price, the inverse also holds.
I believe that a shorter time period than 4 or 10 years would be useful as the bitcoin environment has changed dramatically in this time, along with the global environment. 1 year is likely a good amount of data to use for analysis.

# Limitations
I have not allowed for exchanging between GBP and USD as I have normalised prices over a week and I do not believe that over the time period of a week a cange in the exchange rate would have a significant affect on relative change in the price of bitcoin, I also believe exchange of GBP-USD is much less dependant on time of day and week.

# Data sources
- 10 years of daily bitcoin-USD spot price data: https://uk.investing.com/crypto/bitcoin/historical-data
- 4 years, 3 months of hourly bitcoin-USD 'open' price data: https://www.cryptodatadownload.com/data/bitstamp/
