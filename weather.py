import requests
from lxml import html

rq = requests.get('https://weather.com/weather/today/l/USIL0389:1:US')
xpath = "//div[@class='today_nowcard-temp']/span[1]/text()"
xp2 = "//div[@class='today_nowcard-phrase']/text()"
hixp = "//div[@id='daypart-0']/div[@class='today-daypart-content' and 1]/div[@class='today-daypart-temp' and 4]/span[1]/text()"

tree = html.fromstring(rq.content)

temp = tree.xpath(xpath)[0]
cond = tree.xpath(xp2)[0]
hi = tree.xpath(hixp)[0]

toSpeak = "It is {} degrees and {} outside in Evanston. Today, the high will be {} degrees.".format(temp, cond, hi)