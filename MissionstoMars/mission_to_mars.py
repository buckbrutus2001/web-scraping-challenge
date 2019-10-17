#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
import pandas as pd


# # NASA Mars News

# In[2]:



url = 'https://mars.nasa.gov/news/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:


# print(soup.prettify())


# In[3]:


# results are returned as an iterable list
results = soup.find('div', class_="slide")
news_title = results.find('div', class_="content_title").text
news_p = results.find('div',class_="rollover_description_inner").text
print(f"Title: {news_title}")
print(f"Description: {news_p}")


# # JPL Mars Space Images - Featured Image

# In[93]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[94]:


button = browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(1)
button2 = browser.click_link_by_partial_text('more info')
time.sleep(1)
html = browser.html
featured_image_soup = BeautifulSoup(html,'html.parser')
# print(featured_image_soup.prettify())

figure = featured_image_soup.find('figure', class_="lede")
featured_image_url = figure.img['src']
featured_image_url = f"https://www.jpl.nasa.gov{featured_image_url}"
print(featured_image_url)


# # Mars Weather

# In[225]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
url =  'https://twitter.com/marswxreport?lang=en'
browser.visit(url)
time.sleep(1)


# In[226]:


twitter_html = browser.html
twitter_soup = BeautifulSoup(twitter_html,'html.parser')
# print(twitter_soup.prettify())

tweets = twitter_soup.find('div', class_='js-tweet-text-container')
mars_weather = tweets.find('p', class_="tweet-text").text
mars_weather


# # Mars Facts

# In[227]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://space-facts.com/mars/'
browser.visit(url)
time.sleep(1)

tables = pd.read_html(url)
mars_facts_df = tables[1]
mars_facts_df.columns=['Mars','Facts']
mars_facts_df


# # Mars Hemisphers

# ## Use a for loop next time...

# In[228]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
url =  'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
time.sleep(1)


# In[229]:


button = browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
time.sleep(1)
cer_hem_html = browser.html
cer_hem_soup = BeautifulSoup(cer_hem_html,'html.parser')

cer_hem = cer_hem_soup.find_all('li')
cer_hem_img_url = cer_hem[1].a['href']
cer_hem_title = browser.title
cer_hem_title = cer_hem_title.split(' Enhanced')[0]
cer_hem_title
cer_hem_img_url

hemisphere_image_urls=[]
hem_dict = {}
hem_dict['title'] = cer_hem_title,
hem_dict['img_url'] = cer_hem_img_url 
hemisphere_image_urls.append(hem_dict)

browser.back()


# In[230]:


button = browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
time.sleep(1)
sch_hem_html = browser.html
sch_hem_soup = BeautifulSoup(sch_hem_html,'html.parser')
sch_hem = sch_hem_soup.find_all('li')
sch_hem_img_url = sch_hem[1].a['href']
sch_hem_title = browser.title
sch_hem_title = sch_hem_title.split(' Enhanced')[0]

hem_dict = {}
hem_dict['title'] = sch_hem_title,
hem_dict['img_url'] = sch_hem_img_url 
hemisphere_image_urls.append(hem_dict)

browser.back()


# In[231]:


button = browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
time.sleep(1)
syr_hem_html = browser.html
syr_hem_soup = BeautifulSoup(syr_hem_html,'html.parser')
syr_hem = syr_hem_soup.find_all('li')
syr_hem_img_url = syr_hem[1].a['href']
syr_hem_title = browser.title
syr_hem_title = syr_hem_title.split(' Enhanced')[0]

hem_dict = {}
hem_dict['title'] = syr_hem_title,
hem_dict['img_url'] = syr_hem_img_url 
hemisphere_image_urls.append(hem_dict)


browser.back()


# In[232]:


button = browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
time.sleep(1)
val_hem_html = browser.html
val_hem_soup = BeautifulSoup(val_hem_html,'html.parser')
val_hem = val_hem_soup.find_all('li')
val_hem_img_url = val_hem[1].a['href']
val_hem_title = browser.title
val_hem_title = val_hem_title.split(' Enhanced')[0]

hem_dict = {}
hem_dict['title'] = val_hem_title,
hem_dict['img_url'] = val_hem_img_url 
hemisphere_image_urls.append(hem_dict)

browser.back()


# In[233]:


hemisphere_image_urls


# In[ ]:




