# connect to Google
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)

# setting - build payload
kw_list = ["Nvidia", "Tesla"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='KR', gprop='')

data = pytrends.interest_over_time()
print(data)
