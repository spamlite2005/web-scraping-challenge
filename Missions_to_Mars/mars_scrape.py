from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://mars.nasa.gov/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Find Quote Title
quote_title = soup.find('h1')
# Find Quote Text
quote_p = soup.find('div', class_="description")
# Strip /n's
print(quote_title.text, quote_p.text)
news_title = quote_title.text.strip()
news_p = quote_p.text.strip().strip('MORE').rstrip()

news_title

news_p

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
browser.click_link_by_partial_text('FULL IMAGE')
#browser.click_link_by_partial_text('more info')
time.sleep(10)


#button = soup.find("FULL IMAGE")
#print(button)
#button.click
href = soup.find_all("*", class_="fancybox-image")
href
#link = h3.find('a')
#href = link['href']
#title = link['title']
#a.button.click_link_by_partial_text
#featured_image_url = soup.find('img', class_='main_image')

#button3 = soup.find('a', class_='main_image', data_link="*")
#button3


#print(featured_image_url)
#print(href)
#print(button2)
#print(full_image)



#Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. 
#Save the tweet text for the weather report as a variable called mars_weather.
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

mars_weather_element = soup.find('div', class_="content")
mars_weather = print(mars_weather_element.p.text)

#Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
#Use Pandas to convert the data to a HTML table string.
url = 'https://space-facts.com/mars/'
tables = pd.read_html(url)
tables

#Mars - Earth Comparison
mars_earth_comparison = tables[0]
mars_earth_comparison

#Mars Planet Profile
mars_planet_profile = tables[1].rename(columns={0:"Mars Category", 1:"Value"})
mars_planet_profile

#Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

h3s = soup.find_all('h3')
titles = print(h3s)
titles

#for title in h3s:
#    titles[title] = print(h3s[title].text)
#titles
#for x in range(len(titles)):
#    titles[x].strip('h3')
#titles
#images = image.find('a', href=True)
#images

#titles_stripped = [x.text.split(';')[-1].strip() for x in found]

titles
titles_dict = {}
for title in len(titles):
    titles_dict[title] = {'title' : titles[title]}
titles_dict

