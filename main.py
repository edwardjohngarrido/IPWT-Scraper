#from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#import undetected_chromedriver as webdriver
import pandas as pd
#import requests
import gspread
from google.oauth2.service_account import Credentials
#from googleapiclient.discovery import build

# Importing built-in libraries
import time
from datetime import datetime

#from bs4 import BeautifulSoup as bs

from tiktok_captcha_solver import SeleniumSolver
import undetected_chromedriver as uc

# Connect to spreadsheet
scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "19DsWqJW09VxMfNojPH9mnGJ4MCQl7m3Ud3LNLkn-Ag4"
workbook = client.open_by_key(sheet_id)

mainSheet = workbook.worksheet("Sheet1")
reScraper = workbook.worksheet("Sheet2")
giftedSheet = workbook.worksheet("Sheet3")


options = uc.ChromeOptions()
options.headless=True
options.add_argument('--headless')
driver = uc.Chrome(options=options)
api_key = "df6c8f9d6b26cdc2771d33988efb8c39"
sadcaptcha = SeleniumSolver(
    driver,
    api_key,
    mouse_step_size=1, # Adjust to change mouse speed
    mouse_step_delay_ms=10 # Adjust to change mouse speed
)

# Function to scrape user pages
def scrape_user_page_with_selenium(url, post_link, index):
    driver.get(url)
    sadcaptcha.solve_captcha_if_present()
    #driver.execute_script('window.scrollBy(0, 1000)')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Waiting for the page to load
    print(index)
    user_data = {}

    # Extracting views
    try:
        views = driver.find_element(By.XPATH, "//a[contains(@href, '"+post_link+"')]//strong[@data-e2e='video-views']").text
        user_data['Views'] = views
        mainSheet.update_cell(index, 4, views)

    except Exception as e:
        user_data['Views'] = 'N/A'
        mainSheet.update_cell(index, 4, 'N/A')


    return user_data

# Function to RESCRAPE user pages
def rescrape_user_page_with_selenium(url, post_link, index):
    driver.get(url)
    #driver.execute_script('window.scrollBy(0, 1000)')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Waiting for the page to load
    print(index)
    user_data = {}

    # Extracting views
    try:
        views = driver.find_element(By.XPATH, "//a[contains(@href, '"+post_link+"')]//strong[@data-e2e='video-views']").text
        user_data['Views'] = views
        reScraper.update_cell(index, 4, views)

    except Exception as e:
        user_data['Views'] = 'N/A'
        reScraper.update_cell(index, 4, 'N/A')


    return user_data

# Function to scrape GIFTED user pages
def gifted_scrape_user_page_with_selenium(url, post_link, index):
    driver.get(url)
    sadcaptcha.solve_captcha_if_present()
    #driver.execute_script('window.scrollBy(0, 1000)')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Waiting for the page to load
    print(index)
    user_data = {}

    # Extracting views
    try:
        views = driver.find_element(By.XPATH, "//a[contains(@href, '"+post_link+"')]//strong[@data-e2e='video-views']").text
        user_data['Views'] = views
        print(views)
        giftedSheet.update_cell(index, 4, views)

    except Exception as e:
        user_data['Views'] = 'N/A'
        giftedSheet.update_cell(index, 4, 'N/A')


    return user_data

def trailblazer_data(profiles_list, post_list):
    #Scrape TRAILBLAZER data for each user page
    user_data_list = []
    for ((index, url), post_link) in zip(enumerate(profiles_list), post_list):
        user_data = scrape_user_page_with_selenium(str(url), post_link, index+2) #index+2 so data is being input on the correct row on google sheets after the header
        user_data['Post Link'] = post_link  # Add URL to the data for reference
        user_data_list.append(user_data)
        print(url)
        print(post_link)
    #csv_title = "TRAILBLAZER"
    #csv_file_maker(user_data_list, csv_title)
    driver.quit()


def rescrape_data(profiles_list, post_list):
    #RESCRAPE data for each user page
    user_data_list = []
    for ((index, url), post_link) in zip(enumerate(profiles_list), post_list):
        user_data = rescrape_user_page_with_selenium(str(url), post_link, index+2) #index+2 so data is being input on the correct row on google sheets after the header
        user_data['Post Link'] = post_link  # Add URL to the data for reference
        user_data_list.append(user_data)
    #csv_title = "RESCRAPE"
    #csv_file_maker(user_data_list, csv_title)
    driver.quit()

def gifted_data(profiles_list_gifted, post_list_gifted):
    # Scrape GIFTED data for each user page
    user_data_list = []
    for ((index, url), post_link_gifted) in zip(enumerate(profiles_list_gifted), post_list_gifted):
        user_data = gifted_scrape_user_page_with_selenium(str(url), post_link_gifted, index+435) #index+2 so data is being input on the correct row on google sheets after the header
        user_data['Post Link'] = post_link_gifted  # Add URL to the data for reference
        user_data_list.append(user_data)
        print(url)
        print(post_link_gifted)
    #csv_title = "GIFTED"
    #csv_file_maker(user_data_list, csv_title)
    driver.quit()

profiles_list = mainSheet.col_values(2)
post_list = mainSheet.col_values(3)
profiles_list.pop(0)
post_list.pop(0)
trailblazer_data(profiles_list, post_list)

profiles_list_gifted = giftedSheet.col_values(2)
post_list_gifted = giftedSheet.col_values(3)
profiles_list_gifted.pop(0)
post_list_gifted.pop(0)
gifted_data(profiles_list_gifted, post_list_gifted)

# def csv_file_maker(user_data_list, csv_title):
#     # Convert to DataFrame and save to CSV
#     df_user = pd.DataFrame(user_data_list)
#     df_user.to_csv(csv_title+' Data Scrape '+ str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) +'.csv', index=False)
#     print('Data scraped and saved to csv file')


# def submenu(profiles_list, post_list):
#     row_select = input("Which row do you want to start the data scrape?")
#     for x in range(int(row_select) + 1):
#         profiles_list.pop(0)
#         post_list.pop(0)


# def menu(select):
#     if select == "a":
#         # List of user page URLs and posts to scrape
#         # Data from Google Spreadsheets
#         profiles_list = mainSheet.col_values(2)
#         post_list = mainSheet.col_values(3)

#         select = input("Scrape from specific row? y/n: ")
#         if(select == "y"):
#             submenu(profiles_list, post_list)
#         else:
#             #Remove headers from the data
#             profiles_list.pop(0)
#             post_list.pop(0)

#         trailblazer_data(profiles_list, post_list)

#     elif select == "b":
#         # List of user page URLs and posts to scrape
#         # Data from Google Spreadsheets
#         profiles_list = reScraper.col_values(2)
#         post_list = reScraper.col_values(3)

#         select = input("Scrape from specific row? y/n: ")
#         if(select == "y"):
#             submenu(profiles_list, post_list)
#         else:
#             #Remove headers from the data
#             profiles_list.pop(0)
#             post_list.pop(0)

#         rescrape_data(profiles_list, post_list)


#     elif select == "c":
#         # List of user page URLs and posts to scrape
#         # Data from Google Spreadsheets
#         profiles_list = giftedSheet.col_values(2)
#         post_list = giftedSheet.col_values(3)

#         select = input("Scrape from specific row? y/n: ")
#         if(select == "y"):
#             submenu(profiles_list, post_list)
#         else:
#             #Remove headers from the data
#             profiles_list.pop(0)
#             post_list.pop(0)

#         gifted_data(profiles_list, post_list)

# line_start = 433
# profiles_list = giftedSheet.col_values(2)
# post_list = giftedSheet.col_values(3)
# for x in range(int(line_start) + 1):
#         profiles_list.pop(0)
#         post_list.pop(0)
# #profiles_list.pop(446)
# #post_list.pop(446)
# gifted_data(profiles_list, post_list)

# print("Welcome to the IPWT Tiktok View Scraper")
# print("Please choose what you'd like to scrape:")
# print("a Trailblazer")
# print("b Rescrape")
# print("c Gifted")
# select = input("\n")
# menu(select)

# profiles_list_rescrape = reScraper.col_values(2)
# post_list_rescrape = reScraper.col_values(3)

# profiles_list_gifted = giftedSheet.col_values(2)
# post_list_gifted = giftedSheet.col_values(3)


# profiles_list_rescrape.pop(0)
# post_list_rescrape.pop(0)

# profiles_list_gifted.pop(0)
# post_list_gifted.pop(0)

# for x in range(288):
#     profiles_list_gifted.pop(0)
#     post_list_gifted.pop(0)