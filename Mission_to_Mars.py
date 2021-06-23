
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading page
browser.is_element_present_by_css('div.list_text',wait_time = 1)

html = browser.html
news_soup = bs(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
print(slide_elem)


article = slide_elem.find('div',class_='content_title').get_text()
summary = slide_elem.find('div', class_='article_teaser_body').get_text()
print(article)
print(summary)


url = 'https://spaceimages-mars.com'
browser.visit(url)

full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

html = browser.html
image_soup = bs(html,'html.parser')

image_url_rel = image_soup.find('img',class_='fancybox-image').get('src')

final_image_url = f'https://spaceimages-mars.com/{image_url_rel}'
print(final_image_url)

mars_facts_df = pd.read_html('https://galaxyfacts-mars.com')[0]
mars_facts_df.columns=['description','Mars','Earth']
mars_facts_df.set_index('description',inplace=True)
mars_facts_df.head()

mars_facts_df.to_html()


browser.quit()
