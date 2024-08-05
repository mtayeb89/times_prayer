from pystyle import *
import requests
from bs4 import BeautifulSoup as bs

# Print styled text and boxes
print(Box.Lines('[+] Learn Python with El-tayeb [+]'))  # Print a box with lines around the text
Write.Print('[-] this program for Prayer times', Colors.blue_to_red)  # Print a styled text message with a color gradient
print(Box.DoubleCube('Example []12'))  # Print a box with double cube borders around the text

# Set up a user agent
user_agent1 = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0'}

# Send an HTTP request
r = requests.get('https://timesprayer.com/en/prayer-times-in-cairo.html', headers=user_agent1)

# Parse the HTML response
soup = bs(r.content, 'html.parser')

# Extract prayer times
fajr = soup.find(class_='info prayertable mobile').find_all('tr')[1].text
Sunrise = soup.find(class_='info prayertable mobile').find_all('tr')[2].text
Dhuhr = soup.find(class_='info prayertable mobile').find_all('tr')[3].text
Asr= soup.find(class_='info prayertable mobile').find_all('tr')[4].text
Maghrib= soup.find(class_='info prayertable mobile').find_all('tr')[5].text
Isha= soup.find(class_='info prayertable mobile').find_all('tr')[6].text

# Print the extracted prayer times
print(fajr)
print(Sunrise)
print(Dhuhr)
print(Asr)
print(Maghrib)
print(Isha)
