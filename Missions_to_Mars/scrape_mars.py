from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from pprint import pprint

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

# Use splinter to navigate the site and find the image url for the current 
# featured Mars Image and assign the url string to a variable called featured_image_url.

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(2)
browser.click_link_by_partial_text('more info')
time.sleep(2)
# Inspected website to find specific tags where the Featured Image is
article = soup.find('article')
featured_image = article.find('a')
featured_image_path = featured_image['data-fancybox-href']
print(featured_image_path)

# Make sure to save a complete url string for this image
base_url = 'https://www.jpl.nasa.gov'
featured_image_path_large = featured_image_path.replace('mediumsize','largesize').replace('ip','hires')
print(featured_image_path_large)
featured_image_url = base_url + featured_image_path_large
print(featured_image_url)

#Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. 
#Save the tweet text for the weather report as a variable called mars_weather.
url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
time.sleep(2)
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

#Visit the USGS Astrogeology site here to obtain high resolution images for each of Mars' hemispheres.
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

mars_hemis = []
hemisphere_head = soup.find_all('h3')
pprint(hemisphere_head)

# Get the link for each hemisphere                       
hemisphere1 = soup.find_all('a', class_="itemLink product-item")[1]['href']
hemisphere2 = soup.find_all('a', class_="itemLink product-item")[3]['href']
hemisphere3 = soup.find_all('a', class_="itemLink product-item")[5]['href']
hemisphere4 = soup.find_all('a', class_="itemLink product-item")[7]['href']

# Create a single list called 'mars4hemis'
mars4hemis = [hemisphere1, hemisphere2, hemisphere3, hemisphere4]
mars4hemis

# Go to each of the 4 hemisphere websites and scrape the link for the Sample Image
usgs_url = "https://astrogeology.usgs.gov"
image_url = []
titles = []
for x in range(len(mars4hemis)):
    # Go to the hemisphere website
    browser.visit(usgs_url + mars4hemis[x])
    browser.click_link_by_text("Open")
    time.sleep(2)
    # CLick Sample link to get the image
    sample = browser.find_by_text('Sample')
    image = sample['href']
    image_url.append(image)
    # Search the h2 tags to get the title
    headers = browser.find_by_tag('h2')
    full_title = headers.text
    title = full_title.strip('Enhanced')
    titles.append(title)
#    print(browser.url)
    print(title, image)


# Show the two newly created lists: titles and image_url
print(titles)
print(image_url)

# Create the list of 4 Dictionaries with the image url string and the hemisphere title to a list
hemisphere_image_urls = []
for x in range((len(titles))):
    one_hemisphere = {"title": titles[x], "img_url":image_url[x]}
    hemisphere_image_urls.append(one_hemisphere)
hemisphere_image_urls

# Close the browser after scraping
browser.quit()
