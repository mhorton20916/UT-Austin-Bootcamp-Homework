
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests as req
import pandas as pd

def scrape():
    # In[2]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[3]:


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(.5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    slides = soup.body.find_all('li', class_='slide')
    headings = list()
    teasers = list()
    full_text = list()
    for slide in slides:
        heading = slide.find('div', class_='content_title')
        headings.append(heading.text)
        teaser = slide.find('div', class_='article_teaser_body')
        teasers.append(teaser.text)
    #    full_text_temp = list()
    #    browser.visit(url[0:21]+heading.a['href'])
    #    html2 = browser.html
    #    soup2 = BeautifulSoup(html2, 'html.parser')
    #    art = soup2.body.find('article')
    #    paragraphs = art.find_all('p')
    #    for pg in paragraphs:
    #        full_text_temp.append(pg.text)
    #    full_text.append(full_text_temp)


    # In[4]:


    #print(headings[0])
    #print(teasers[0])


    # In[5]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(.5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    style_link = soup.body.find('div',class_='carousel_items').article['style']
    link = style_link[style_link.find('/'):-3]
    featured_image_url = url[:url.find('/spaceimages')]+link


    # In[6]:


    #featured_image_url


    # In[7]:


    url = 'https://twitter.com/marswxreport?lang=en'
    resp = req.get(url)
    soup = BeautifulSoup(resp.content,'lxml')
    mars_weather = soup.body.find('div',class_='stream').p.text


    # In[8]:


    #mars_weather


    # In[9]:


    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df.rename(columns={0:'Description',1:'Value'},inplace=True)
    df.set_index('Description',drop=True,inplace=True)
    table = df.to_html()


    # In[10]:


    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    hemispheres = soup.body.find('div',class_='collapsible results').find_all('div',class_='description')
    hemispheres_d = []
    for hem in hemispheres:
        hem_title = ' '.join(hem.a.text.split(' ')[:-1])
        browser.click_link_by_partial_text(hem_title)
        hem_link = browser.find_link_by_text('Sample')['href']
        temp_dict = {'title':hem_title,'img_url':hem_link}
        hemispheres_d.append(temp_dict)
        browser.back()


    # In[11]:


    #hemispheres_d


    # In[13]:


    output_dict = {'heading': headings[0],
                'teaser': teasers[0],
                'featured_image_url': featured_image_url,
                'mars_weather': mars_weather,
                'table_html': table,
                'hemisphere_urls': hemispheres_d}

    browser.quit()

    return output_dict