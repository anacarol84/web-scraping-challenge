 # import libraries and requirements
import requests
import pymongo
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import time 
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Connecting to NASA site
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    news_html = browser.html
    news_soup = BeautifulSoup(news_html,'lxml')
    slide_element = news_soup.select_one("ul.item_list li.slide")
    
    Latest_title = slide_element.find("div", class_="content_title").get_text()

    paragraph = slide_element.find("div", class_="article_teaser_body").get_text()

    url2 = "https://spaceimages-mars.com/"
    browser.visit(url2)

    browser.find_by_css("button.btn").click()

    image = browser.find_by_css(".fancybox-image")[0]["src"]

    url2 = "https://marshemispheres.com/"
    browser.visit(url2)

    all_hemisphere = []

    for i in range(0,4):
        browser.find_by_css("a.product-item img")[i].click()
        browser.find_by_text('Sample')["href"]
        browser.find_by_css("h2.title").text
        h={"title": browser.find_by_css("h2.title").text,
        "image_url": browser.find_by_text('Sample')["href"]     
        }
        all_hemisphere.append(h)
        browser.back()
        
    mars_facts = pd.read_html("https://galaxyfacts-mars.com/")[1]

    mars_html = mars_facts.to_html(classes=["table", "table-striped"])

    browser.quit()

    return {
        "news_title": Latest_title,
        "paragraph": paragraph,
        "images": image,
        "mars_facts": mars_html,
        "hemispheres": all_hemisphere
    }

if __name__ == "__main__":
    print(scrape_all())  