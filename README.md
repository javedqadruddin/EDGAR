# EDGAR

To download SEC filings for any company in the ticker csv files in the data/ticker_data directory, navigate to the lib directory and then simply:

```python scraper.py ../data/ticker_data/[name of ticker csv file you're interested in] [type of filing you want]```

This will not work in python 3, so, if your system is on python 3 by default, make the command:

```python2 scraper.py ../data/ticker_data/[name of ticker csv file you're interested in] [type of filing you want]```
