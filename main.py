# #from selenium import webdriver
# from selenium.webdriver.common.by import By
# #from selenium.webdriver.chrome.service import Service
# #from webdriver_manager.chrome import ChromeDriverManager
# #import undetected_chromedriver as webdriver
# import pandas as pd
# #import requests
# import gspread
# from google.oauth2.service_account import Credentials
# #from googleapiclient.discovery import build

# # Importing built-in libraries
# import time
# from datetime import datetime

# #from bs4 import BeautifulSoup as bs

# from tiktok_captcha_solver import SeleniumSolver
# import undetected_chromedriver as uc

# # Connect to spreadsheet
# scopes = [
#     "https://www.googleapis.com/auth/spreadsheets"
# ]

# creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
# client = gspread.authorize(creds)

# sheet_id = "19DsWqJW09VxMfNojPH9mnGJ4MCQl7m3Ud3LNLkn-Ag4"
# workbook = client.open_by_key(sheet_id)

# mainSheet = workbook.worksheet("Sheet1")
# reScraper = workbook.worksheet("Sheet2")
# giftedSheet = workbook.worksheet("Sheet3")


# options = uc.ChromeOptions()
# options.headless=True
# options.add_argument('--headless')
# driver = uc.Chrome(options=options)
# api_key = "df6c8f9d6b26cdc2771d33988efb8c39"
# sadcaptcha = SeleniumSolver(
#     driver,
#     api_key,
#     mouse_step_size=1, # Adjust to change mouse speed
#     mouse_step_delay_ms=10 # Adjust to change mouse speed
# )

# # Function to scrape user pages
# def scrape_user_page_with_selenium(url, post_link, index):
#     driver.get(url)
#     sadcaptcha.solve_captcha_if_present()
#     #driver.execute_script('window.scrollBy(0, 1000)')
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)  # Waiting for the page to load
#     print(index)
#     user_data = {}

#     # Extracting views
#     try:
#         views = driver.find_element(By.XPATH, "//a[contains(@href, '"+post_link+"')]//strong[@data-e2e='video-views']").text
#         print(views)
#         user_data['Views'] = views
#         mainSheet.update_cell(index, 4, views)

#     except Exception as e:
#         user_data['Views'] = 'N/A'
#         mainSheet.update_cell(index, 4, 'N/A')


#     return user_data

# # Function to RESCRAPE user pages
# def rescrape_user_page_with_selenium(url, post_link, index):
#     driver.get(url)
#     #driver.execute_script('window.scrollBy(0, 1000)')
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)  # Waiting for the page to load
#     print(index)
#     user_data = {}

#     # Extracting views
#     try:
#         views = driver.find_element(By.XPATH, "//a[contains(@href, '"+post_link+"')]//strong[@data-e2e='video-views']").text
#         user_data['Views'] = views
#         reScraper.update_cell(index, 4, views)

#     except Exception as e:
#         user_data['Views'] = 'N/A'
#         reScraper.update_cell(index, 4, 'N/A')


#     return user_data

# # Function to scrape GIFTED user pages
# def gifted_scrape_user_page_with_selenium(url, post_link, index):
#     driver.get(url)
#     sadcaptcha.solve_captcha_if_present()
#     #driver.execute_script('window.scrollBy(0, 1000)')
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)  # Waiting for the page to load
#     print(index)
#     user_data = {}

#     # Extracting views
#     try:
#         views = driver.find_element(By.XPATH, "//a[contains(@href, '"+post_link+"')]//strong[@data-e2e='video-views']").text
#         user_data['Views'] = views
#         print(views)
#         giftedSheet.update_cell(index, 4, views)

#     except Exception as e:
#         user_data['Views'] = 'N/A'
#         giftedSheet.update_cell(index, 4, 'N/A')


#     return user_data

# def trailblazer_data(profiles_list, post_list):
#     #Scrape TRAILBLAZER data for each user page
#     user_data_list = []
#     for ((index, url), post_link) in zip(enumerate(profiles_list), post_list):
#         user_data = scrape_user_page_with_selenium(str(url), post_link, index+2) #index+2 so data is being input on the correct row on google sheets after the header
#         user_data['Post Link'] = post_link  # Add URL to the data for reference
#         user_data_list.append(user_data)
#         print(url)
#         print(post_link)
#     #csv_title = "TRAILBLAZER"
#     #csv_file_maker(user_data_list, csv_title)
#     driver.quit()


# def rescrape_data(profiles_list, post_list):
#     #RESCRAPE data for each user page
#     user_data_list = []
#     for ((index, url), post_link) in zip(enumerate(profiles_list), post_list):
#         user_data = rescrape_user_page_with_selenium(str(url), post_link, index+2) #index+2 so data is being input on the correct row on google sheets after the header
#         user_data['Post Link'] = post_link  # Add URL to the data for reference
#         user_data_list.append(user_data)
#     #csv_title = "RESCRAPE"
#     #csv_file_maker(user_data_list, csv_title)
#     driver.quit()

# def gifted_data(profiles_list_gifted, post_list_gifted):
#     # Scrape GIFTED data for each user page
#     user_data_list = []
#     for ((index, url), post_link_gifted) in zip(enumerate(profiles_list_gifted), post_list_gifted):
#         user_data = gifted_scrape_user_page_with_selenium(str(url), post_link_gifted, index+435) #index+2 so data is being input on the correct row on google sheets after the header
#         user_data['Post Link'] = post_link_gifted  # Add URL to the data for reference
#         user_data_list.append(user_data)
#         print(url)
#         print(post_link_gifted)
#     #csv_title = "GIFTED"
#     #csv_file_maker(user_data_list, csv_title)
#     driver.quit()

# profiles_list = mainSheet.col_values(2)
# post_list = mainSheet.col_values(3)
# profiles_list.pop(0)
# post_list.pop(0)
# trailblazer_data(profiles_list, post_list)

# profiles_list_gifted = giftedSheet.col_values(2)
# post_list_gifted = giftedSheet.col_values(3)
# profiles_list_gifted.pop(0)
# post_list_gifted.pop(0)
# gifted_data(profiles_list_gifted, post_list_gifted)

# # def csv_file_maker(user_data_list, csv_title):
# #     # Convert to DataFrame and save to CSV
# #     df_user = pd.DataFrame(user_data_list)
# #     df_user.to_csv(csv_title+' Data Scrape '+ str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) +'.csv', index=False)
# #     print('Data scraped and saved to csv file')


# # def submenu(profiles_list, post_list):
# #     row_select = input("Which row do you want to start the data scrape?")
# #     for x in range(int(row_select) + 1):
# #         profiles_list.pop(0)
# #         post_list.pop(0)


# import time
# import gspread
# from google.oauth2.service_account import Credentials
# from selenium.webdriver.common.by import By
# import undetected_chromedriver as uc
# from tiktok_captcha_solver import SeleniumSolver

# # Google Sheets Authentication
# scopes = ["https://www.googleapis.com/auth/spreadsheets"]
# creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
# client = gspread.authorize(creds)

# # Open Spreadsheet
# sheet_id = "19DsWqJW09VxMfNojPH9mnGJ4MCQl7m3Ud3LNLkn-Ag4"
# workbook = client.open_by_key(sheet_id)
# mainSheet = workbook.worksheet("Sheet1")
# reScraper = workbook.worksheet("Sheet2")
# giftedSheet = workbook.worksheet("Sheet3")

# # Function to initialize WebDriver
# def init_driver():
#     options = uc.ChromeOptions()
#     options.headless = True
#     options.add_argument('--headless')
#     driver = uc.Chrome(options=options)
#     return driver

# def scrape_page(driver, url, post_link, sheet, index, solver=None):
#     driver.get(url)
#     if solver:
#         solver.solve_captcha_if_present()
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
    
#     try:
#         views = driver.find_element(By.XPATH, f"//a[contains(@href, '{post_link}')]//strong[@data-e2e='video-views']").text
#         sheet.update_cell(index, 4, views)
#         return views
#     except Exception:
#         sheet.update_cell(index, 4, 'N/A')
#         return 'N/A'

# def process_data(profiles_list, post_list, sheet, start_index, use_solver=False):
#     solver = None
#     if use_solver:
#         driver = init_driver()
#         solver = SeleniumSolver(driver, "df6c8f9d6b26cdc2771d33988efb8c39")
    
#     for batch_start in range(0, len(profiles_list), 100):
#         driver = init_driver()
#         if use_solver:
#             solver = SeleniumSolver(driver, "df6c8f9d6b26cdc2771d33988efb8c39")
        
#         batch_profiles = profiles_list[batch_start:batch_start+100]
#         batch_posts = post_list[batch_start:batch_start+100]
        
#         for index, (url, post_link) in enumerate(zip(batch_profiles, batch_posts), start=batch_start + start_index):
#             scrape_page(driver, url, post_link, sheet, index, solver if use_solver else None)
#             print(f"Processed: {url}, {post_link}")
        
#         driver.quit()

# def main():
#     # # Trailblazer Data
#     # profiles_list = mainSheet.col_values(2)[1:]
#     # post_list = mainSheet.col_values(3)[1:]
#     # process_data(profiles_list, post_list, mainSheet, 2, use_solver=True)
    
#     # Gifted Data
#     profiles_list_gifted = giftedSheet.col_values(2)[1:]
#     post_list_gifted = giftedSheet.col_values(3)[1:]
#     process_data(profiles_list_gifted, post_list_gifted, giftedSheet, 2, use_solver=True)

# if __name__ == "__main__":
#     main()

import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tiktok_captcha_solver import SeleniumSolver
import gspread
from google.oauth2.service_account import Credentials

# Connect to Google Sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "19DsWqJW09VxMfNojPH9mnGJ4MCQl7m3Ud3LNLkn-Ag4"
workbook = client.open_by_key(sheet_id)

mainSheet = workbook.worksheet("Sheet1")
reScraper = workbook.worksheet("Sheet2")
giftedSheet = workbook.worksheet("Sheet3")

def init_driver():
    options = uc.ChromeOptions()
    options.headless = True
    driver = uc.Chrome(options=options)
    return driver

def solve_captcha(driver):
    api_key = "df6c8f9d6b26cdc2771d33988efb8c39"
    solver = SeleniumSolver(driver, api_key)
    solver.solve_captcha_if_present()

def scrape_profile(driver, profile, post_links, sheet, start_index):
    driver.get(profile)
    solve_captcha(driver)
    
    # Scroll until all post links are found or bottom is reached
    found_posts = set()
    attempts = 0
    max_attempts = 10  # Prevent infinite scrolling
    
    while len(found_posts) < len(post_links) and attempts < max_attempts:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)
        attempts += 1
        
        for i, post_link in enumerate(post_links):
            row_index = start_index + i  # Ensure correct row calculation
            print(f"Checking post: {post_link} at row {row_index}")
            if post_link not in found_posts:
                try:
                    views = driver.find_element(By.XPATH, f"//a[contains(@href, '{post_link}')]//strong[@data-e2e='video-views']").text
                    sheet.update_cell(row_index, 4, views)
                    print(f"Found views: {views} for post: {post_link}")
                    found_posts.add(post_link)
                except:
                    continue
    
    # Mark missing posts as "N/A"
    for i, post_link in enumerate(post_links):
        row_index = start_index + i  # Ensure correct row calculation
        if post_link not in found_posts:
            sheet.update_cell(row_index, 4, "N/A")
            print(f"Post {post_link} not found, setting row {row_index} to N/A")

def process_data(profiles_list, post_list, sheet, start_index):
    driver = init_driver()
    profile_posts = {}
    
    for profile, post in zip(profiles_list, post_list):
        if profile not in profile_posts:
            profile_posts[profile] = []
        profile_posts[profile].append(post)
    
    current_index = start_index  # Track correct row placement
    
    for profile, posts in profile_posts.items():
        scrape_profile(driver, profile, posts, sheet, current_index)
        current_index += len(posts)  # Move index by number of posts per profile
    
    driver.quit()

profiles_list = mainSheet.col_values(2)[1:]
post_list = mainSheet.col_values(3)[1:]
process_data(profiles_list, post_list, mainSheet, 2)

gifted_profiles = giftedSheet.col_values(2)[1:]
gifted_posts = giftedSheet.col_values(3)[1:]
process_data(gifted_profiles, gifted_posts, giftedSheet, 2)