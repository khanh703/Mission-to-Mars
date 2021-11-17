# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
# does this mean wait for up to 1 second before finding div classed list_text?
browser.is_element_present_by_css('div.list_text', wait_time=1)



html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div', class_='list_text')
slide_elem



news_title = slide_elem.find('div', class_='content_title').get_text()
# news_title = slide_elem.select('div', class_='content_title')
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


## Practice

all_list_elem = news_soup.find_all('div', class_='list_text')
len(all_list_elem)

for item in all_list_elem:
    print('--------')
    print(item)


# ### Featured Images

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel



# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # 10.3.5 Scrape HTML Table
# 
# The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML.


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

browser.quit()


# INSERT
# SYNTAX
# database.table.action(payload)
# db.zoo.insert({name: 'Cleo', species: 'jaguar', age: 12, hobbies: ['sleeping', 'eating', 'climbing']})

# FIND
# db.zoo.find()

# DROP SYNTAX
# db.collectionName.remove({})

# DROP TABLE ZOO
#db.zoo.drop()

# EMPTY TABLE
# db.zoo.remove({})

# DROP A ROW
# db.zoo.remove({name: 'Cleo'})

# DROP A DATABASE
# db.dropDatabase()