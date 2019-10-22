#!/usr/bin/env python
# coding: utf-8

# In[240]:


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time
import pandas as pd


# # NASA Mars News

# In[241]:

def scrape():
    
    mission_to_mars ={}

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)
    news_html = browser.html
    # response = requests.get(url)
    soup = BeautifulSoup(news_html, 'html.parser')


    # In[242]:


    # results are returned as an iterable list
    results = soup.find('div', class_="slide")
    news_title = results.find('div', class_="content_title").text
    news_p = results.find('div',class_="rollover_description_inner").text
    # print(f"Title: {news_title}")
    # print(f"Description: {news_p}")
    mission_to_mars['news_title'] = news_title
    mission_to_mars['news_description'] = news_p


    # # JPL Mars Space Images - Featured Image

    # In[245]:



    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(1)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)

    browser.is_element_present_by_text("more info", wait_time=1)
    more_info_element = browser.find_link_by_partial_text("more info")
    more_info_element.click()

    html = browser.html
    featured_image_soup = BeautifulSoup(html,'html.parser')
    # print(featured_image_soup.prettify())

    figure = featured_image_soup.find('figure', class_="lede")
    featured_image_url = figure.img['src']
    featured_image_url = f"https://www.jpl.nasa.gov{featured_image_url}"
    # print(featured_image_url)
    mission_to_mars['featured_image_url'] = featured_image_url


    # # Mars Weather

    # In[246]:


    url =  'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(1)


    # In[247]:


    twitter_html = browser.html
    twitter_soup = BeautifulSoup(twitter_html,'html.parser')
    # print(twitter_soup.prettify())

    tweets = twitter_soup.find('div', class_='js-tweet-text-container')
    mars_weather = tweets.find('p', class_="tweet-text").text
    # mars_weather
    mission_to_mars['mars_weather'] = mars_weather


    # # Mars Facts

    # In[248]:


    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    time.sleep(1)

    tables = pd.read_html(url)
    mars_facts_df = tables[1]
    mars_facts_df.columns=['Mars','Facts']
    # mars_facts_df
    mars_facts_html = mars_facts_df.to_html()
    mission_to_mars['mars_facts_df'] = mars_facts_html


    # # Mars Hemisphers

    # ## Use a for loop next time...

    # In[249]:


    url =  'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(1)


    # In[250]:



    hem_html = browser.html
    hem_soup = BeautifulSoup(hem_html,'html.parser')

    hems_dict =[]
    hems = hem_soup.find_all('div', class_='item')


    for hem in hems:
        
        time.sleep(1)
        hem_dict = {}

        hem_name = hem.find('h3').text
        hem_name = hem_name.split(' Enhanced')
        hem_name = hem_name[0]

        hem_url = hem.a['href']
        browser.visit('https://astrogeology.usgs.gov' + hem_url)
        
        hem_img_html = browser.html
        hem_img_soup = BeautifulSoup(hem_img_html,'html.parser')
        hem_img_url = hem_img_soup.find('a', text='Sample').get('href')
        
            
        hem_dict ={'title': hem_name, 'img_url': hem_img_url}
        hems_dict.append(hem_dict)
        browser.back()
        


    # hemisphere_image_urls
    mission_to_mars['hemisphere_image_urls'] = hems_dict
    browser.quit()

    return mission_to_mars
# In[255]:


# mission_to_mars


# In[ ]:




