# bitcoin_frequent_investment_analysis
Data analysis to determine the best day of week and hour of the day to invest in bitcoin on a weekly basis.

# Motivation
Determine the best time of the week to set-up an automated weekly investment in bitcoin in order to maximise future returns.

# Process
Split price data by the day of the week and the wek of the year, normalise data by week so that the data points can be visualised and compared over time and create violin plots of this data. If an hour of the day or day of the week show a particularly thick section on the graph at the top of the 'violin', this day or time has historically recorded a high itcoin spot price, the inverse also holds.
I believe that a shorter time period than 4 or 10 years would be useful as the bitcoin environment has changed dramatically in this time, along with the global environment. 1 year is likely a good amount of data to use for analysis.I intend to hold bitcoin rather than sell and so I shall not look into when the price is highest but this could be done in a similar fashion.

# Limitations
I have not allowed for exchanging between GBP and USD as I have normalised prices over a week and I do not believe that over the time period of a week a cange in the exchange rate would have a significant affect on relative change in the price of bitcoin, I also believe exchange of GBP-USD is much less dependant on time of day and week.

# Data sources
- 10 years of daily bitcoin-USD spot price data: https://uk.investing.com/crypto/bitcoin/historical-data
- 4 years, 3 months of hourly bitcoin-USD 'open' price data: https://www.cryptodatadownload.com/data/bitstamp/

# Results
The code produces violin plots which are more visually intuitive versions of box plots. Yjey still show the typical values of a box plot in a standard fashion, on top of this they also expand and contract where there are more and less data points at a particular value. In this instance I am looking for any points of the violin plot that are particularly wide in the lower end of the violin plot to indicate that the price was consistantly low in this period, and for wide plots at the upper end of the violin to indicate high points of the week. I'll look first at the day of the week, then use this information to look into a single day in particular.

![day_of_week_1_year](https://user-images.githubusercontent.com/26042506/184531519-a85065c7-b381-45bc-b315-492b8d598d06.png)

This graph shows that over the last year, Friday was a consistant low point for the price of bitcoin, interestingly, the low points are considerably different to that shown by data taken over the last 10 years. I have chosen to use only data over the last year because of big shifts in the adoption of bitcoin and the global economy but it could be said that a years worth of data is not a sufficient amount.

Looking into Fridays houly data over the last year.

![hour_of_day_friday_1_year](https://user-images.githubusercontent.com/26042506/184531732-abd7974b-2009-4e01-928f-7a4f0eb0dedf.png)

We'reagain looking for low points on the graph, here it seems that the low points are around midnight. It seems to follow then that I should buy bitcoin between 23:00 and 24:00 Friday night.
