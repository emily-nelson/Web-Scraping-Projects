from select import select
from datetime import datetime
import requests, bs4

bbc = requests.get("https://www.bbc.co.uk/weather/2641181")
bbc.raise_for_status()
bbc_soup = bs4.BeautifulSoup(bbc.text, 'html.parser')

current_temp = bbc_soup.select('#wr-forecast > div.wr-time-slot-container > div > div.wr-time-slot-container__details-container > div.wr-time-slot-container__slots > div > div > div > div.wr-time-slot-list__item.wr-time-slot-list__item--time-slots > ol > li:nth-child(1) > button > div.wr-time-slot-primary.wr-js-time-slot-primary > div.wr-time-slot-primary__content.wr-time-slot-primary__content--temp9to10 > div.wr-time-slot-primary__body > div.wr-time-slot-primary__weather-curve > div > div > div.wr-time-slot-primary__temperature > span > span.wr-value--temperature--c')


met_office = requests.get("https://www.metoffice.gov.uk/weather/forecast/u12gmt1fz#?date=2022-04-27")
met_office.raise_for_status()
met_office_soup = bs4.BeautifulSoup(met_office.text, 'html.parser')

sunrise = met_office_soup.select('#dayLink2022-04-27 > div.row.hide-xs-only.col-sm-12.highlight-card.significant-weather > div > div.row.col-sm-5 > div:nth-child(1) > div > div > time')

sunset = met_office_soup.select('#dayLink2022-04-27 > div.row.hide-xs-only.col-sm-12.highlight-card.significant-weather > div > div.row.col-sm-5 > div:nth-child(2) > div > div > time')

pollen = met_office_soup.select('#dayLink2022-04-27 > div.row.hide-xs-only.col-sm-12.highlight-card.significant-weather > div > div.col-sm-7 > div > div.col-sm-4.weather-item > div.weather-icons > span')

day_1 = met_office_soup.select('#dayLink2022-04-28 > div.tab-upper > div.day-row > div > div.tab-temp > span.tab-temp-high')

day_2 = met_office_soup.select('#dayLink2022-04-29 > div.tab-upper > div.day-row > div > div.tab-temp > span.tab-temp-high')

day_3 = met_office_soup.select('#dayLink2022-04-30 > div.tab-upper > div.day-row > div > div.tab-temp > span.tab-temp-high')

day_4 = met_office_soup.select('#dayLink2022-05-01 > div.tab-upper > div.day-row > div > div.tab-temp > span.tab-temp-high')

day_5 = met_office_soup.select('#dayLink2022-05-02 > div.tab-upper > div.day-row > div > div.tab-temp > span.tab-temp-high')

msn = requests.get("https://www.msn.com/en-gb/weather/today/weather-today/we-city?el=aMzze9avE7QLXCle99ojQg1Vo3Ahi8s%2FiqSmwk7ErA1tmufSSEQx94jHLHUXHGFS&ocid=ansmsnweather")
msn.raise_for_status()
msn_soup = bs4.BeautifulSoup(msn.text, 'html.parser')



print("NORWICH, ENGLAND")
print(sunrise[0].getText() + " | " + sunset[0].getText())


print(current_temp[0].getText() + " | " + day_1[0].getText() + " | " + day_2[0].getText() + " | " + day_3[0].getText() + " | " + day_4[0].getText() + " | " + day_5[0].getText())
print("Pollen " + "| " + pollen[0].getText())
