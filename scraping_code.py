
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# First scrape for article title

def mars_news(browser):
    url = 'https://redplanetscience.com'
    browser.visit(url)
    # Optional delay for loading page
    browser.is_element_present_by_css('div.list_text',wait_time = 1)
    html = browser.html
    try:
        news_soup = bs(html, 'html.parser')
        slide_elem = news_soup.select_one('div.list_text')
        article = slide_elem.find('div',class_='content_title').get_text()
        summary = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None
return article, summary

def featured_image(browser):
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
# find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()
# scrape to get the 
    html = browser.html
    image_soup = bs(html,'html.parser')
    try:
        image_url_rel = image_soup.find('img',class_='fancybox-image').get('src')
    except AttributeError:
        return None
    img_url = f'https://spaceimages-mars.com/{image_url_rel}'

    return img_url

def mars_facts(browser):
    try:
        mars_facts_df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None

    mars_facts_df.columns=['description','Mars','Earth']
    mars_facts_df.set_index('description',inplace=True)
    mars_facts_df.head()

    return mars_facts_df.to_html()

browser.quit()
