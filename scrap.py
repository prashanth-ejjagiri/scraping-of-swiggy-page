#Project 2 :
#web Scraping using BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas

swiggy_url = "https://www.swiggy.com/hyderabad?page = "
page_num_max = 3
scraped_info_list = []
for page_num in range(1, page_num_max):
    req = requests.get(swiggy_url +str(page_num))
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_swiggy = soup.find_all("div", {"class": "_3FR5S"})
    

    for restaurant in all_swiggy:
        restaurant_dict = {}
        restaurant_dict["name"] = restaurant.find("div", {"class": "nA6kb"}).text
        restaurant_dict["items"] = restaurant.find("div", {"class": "_1gURR"}).text
        restaurant_dict["item_cost"] = restaurant.find("div", {"class": "nVWSi"}).text

        try:

            restaurant_dict["rating"] = restaurant.find("div", {"class": "_9uwBC wY0my"}).text
            restaurant_dict["offers"] = restaurant.find("span", {"class": "sNAfh"}).text
        except AttributeError:
            pass
        scraped_info_list.append(restaurant_dict)
    print(swiggy_url + str(page_num))
        #print(restaurant_name, restaurant_items, restuarant_offers)
dataFrame = pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("swiggy.csv")
