from bs4 import BeautifulSoup
import requests
import re

#ask user for the first and last date of their trip
first_date = input("What is the first date of your trip (format as mm-dd-yyyy): ")
last_date = input("What is the last date of your trip (format as mm-dd-yyyy): ")

#ask user for where they are traveling from and where they want to travel to
starting_location = input("What city are you leaving from (format as City,State): ")
destination = input("What city are you going to (format as City,State): ")

#breaks the first date and last date of the trip into day, month, and year to be put into url
first_date_month = first_date[0:2]
first_date_day = first_date[3:5]
first_date_year = first_date[6:10]

last_date_month = last_date[0:2]
last_date_day = last_date[3:5]
last_date_year = last_date[6:10]

#put all user entered data into url to find appropriate flight information
url = f'https://www.expedia.com/Flights-Search?flight-type=on&mode=search&trip=roundtrip&leg1=from%3A{starting_location}%2Cto%3A{destination}%2Cdeparture%3A{first_date_month}%2F{first_date_day}%2F{first_date_year}TANYT&options=cabinclass%3Aeconomy&leg2=from%3A{destination}%2Cto%3A{starting_location}%2Cdeparture%3A{last_date_month}%2F{last_date_day}%2F{last_date_year}TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY&fromDate={first_date_month}%2F{first_date_day}%2F{first_date_year}&toDate={last_date_month}%2F{last_date_day}%2F{last_date_year}&d1={first_date}&d2={last_date}'
#url = 'https://www.expedia.com/Flights-Search?flight-type=on&mode=search&trip=roundtrip&leg1=from%3Ahouston%2Cto%3Anewyork%2Cdeparture%3A4%2F7%2F2023TANYT&options=cabinclass%3Aeconomy&leg2=from%3Anewyork%2Cto%3Ahouston%2Cdeparture%3A4%2F8%2F2023TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY&fromDate=4%2F7%2F2023&toDate=4%2F8%2F2023&d1=2023-04-07&d2=2023-04-08'

page = requests.get(url).text
doc = BeautifulSoup(page,'html.parser')

print(url)