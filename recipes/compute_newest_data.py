# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#ライブラリのインポート
import requests
from bs4 import BeautifulSoup
from datetime import date
import pytz
from datetime import datetime
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#tenki.jpの目的の地域のページのURL（今回は東京都調布市）
url = 'https://tenki.jp/forecast/2/5/3110/2202/'

#HTTPリクエスト
r = requests.get(url)

#プロキシ環境下の場合は以下を記述
"""
proxies = {
    "http":"http://proxy.xxx.xxx.xxx:8080",
    "https":"http://proxy.xxx.xxx.xxx:8080"
}
r = requests.get(url, proxies=proxies)
"""

#HTMLの解析
bsObj = BeautifulSoup(r.content, "html.parser")

#今日の天気を取得
today = bsObj.find(class_="today-weather")
weather = today.p.string

#気温情報のまとまり
temp=today.div.find(class_="date-value-wrap")

#気温の取得
temp=temp.find_all("dd")
temp_max = temp[0].span.string #最高気温
temp_max_diff=temp[1].string #最高気温の前日比
temp_min = temp[2].span.string #最低気温
temp_min_diff=temp[3].string #最低気温の前日比

#結果の出力
print("天気:{}".format(weather))
print("最高気温:{} {}".format(temp_max,temp_max_diff))
print("最低気温:{} {}".format(temp_min,temp_min_diff))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
temp_ave = (int(temp_max) + int(temp_min))/2
temp_ave

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from dateutil import tz

# METHOD 1: Hardcode zones:
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Japan')

utc = datetime.utcnow()
# utc = datetime.strptime('2011-01-21 02:37:21', '%Y-%m-%d %H:%M:%S')

# Tell the datetime object that it's in UTC time zone since
# datetime objects are 'naive' by default
utc = utc.replace(tzinfo=from_zone)

# Convert time zone
jpn_time = utc.astimezone(to_zone)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
today = str(jpn_time.year)+"/"+str(jpn_time.month)+"/"+str(jpn_time.day)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df = pd.DataFrame({"date":[today], "temperature":[temp_ave]})



py_recipe_output = dataiku.Dataset("newest_data")
py_recipe_output.write_with_schema(df)



