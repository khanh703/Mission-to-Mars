#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[20]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
# does this mean wait for up to 1 second before finding div classed list_text?
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div', class_='list_text')


# In[5]:


# news_title = slide_elem.find('div', class_='content_title').text
news_title = slide_elem.select('div', class_='content_title')


# In[6]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body')
news_p


# ### Featured Images

# In[7]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[8]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[9]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[10]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[11]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # 10.3.5 Scrape HTML Table
# 
# The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML.

# In[12]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[13]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[29]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[30]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[31]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
high_resolution_soup = soup(html, 'html.parser')
wrapper_elem = high_resolution_soup.find('div', class_='collapsible')

# all relevant items
items = wrapper_elem.find_all('div', class_='item')

for item in items:
    
    # extract title
    title = item.find('h3').text
    
    # extract and build item content url
    itemLinkHref = item.find('a', class_="itemLink").get('href')
    itemContentUrl = f"{url}{itemLinkHref}"
    
    # visit itemContentUrl
    browser.visit(itemContentUrl)
    
    # find anchor element with text Sample
    # extract href attribute and append to url
    img_html = browser.html
    img_hr_soup = soup(img_html, 'html.parser')
    imageLinkHref = img_hr_soup.find('a', text='Sample').get('href')
    img_url_rel = f"{url}{imageLinkHref}"
    
    # add this object to our hemisphere_image_urls
    hemisphere_image_urls.append({"title":title, "img_url":img_url_rel})


# In[32]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[18]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:




