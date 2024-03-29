#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[5]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[6]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[7]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[8]:


slide_elem.find('div', class_='content_title')


# In[9]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[10]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image
# 

# In[11]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[12]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[13]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[14]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[15]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[16]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[17]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[18]:


url = 'https://marshemispheres.com'
browser.visit(url)


# In[19]:


# 2. Create a list to hold the images and titles.
links=browser.find_by_css('a.product-item img')

hemisphere_img_urls=[]

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for x in range(len(links)):
     hemisphere ={}
     browser.find_by_css('a.product-item img')[x].click()

     sample=browser.links.find_by_text('Sample').first
     hemisphere['img_url']=sample['href']

     hemisphere['title']=browser.find_by_css('h2.title').text

     hemisphere_img_urls.append(hemisphere)

     browser.back()


# In[20]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_img_urls


# In[21]:


# 5. Quit the browser
browser.quit()

