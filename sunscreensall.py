"""
Find the most expensive Sunscreen and add it to the cart.
SCOPE:
1) Launch Chrome Driver.
2) Navigate Sunscreen page.
3) Add all the Sunscreens to the cart.
4) Get the number of items added to cart.
5) Check if all the items are added to the cart.
6) Print the valid message.
7) Close the browser.

"""

from selenium import webdriver
import time

# Creating an instance of the web browser and navigating to the Sunscreen page
browser = webdriver.Chrome()
browser.get('https://weathershopper.pythonanywhere.com/sunscreen')

# Checking if the control lands on the right web page 
head=browser.find_element_by_xpath("//h2").text
print(head)
if head=="Sunscreens":
    print("page found")
    
else:
    print("Page not found")
    browser.close()
    exit()
# Creating a list with prizes of all moistirizers
sunscreen_prices=list()
prices_box=browser.find_elements_by_xpath('//div[@class="text-center col-4"]//descendant::p[contains(text(),"Price")]')
for i in prices_box:
    price=int(i.text.strip("Price: Rs. "))
    sunscreen_prices.append(price)
print("The prizes of the Sunscreens are ",sunscreen_prices)
prices=sunscreen_prices
for i in range(len(prices)):
    single_price=prices[i]
    add_button=browser.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(single_price))
    add_button.click()
#checking the number of items in the cart
no_of_items=browser.find_element_by_xpath("//*[@id='cart']").text.split(' ')
items=no_of_items[0]
if items=='6':
    print("All "+items+" items are added to cart")
else:
    print("Not all items are added")
add_to_cart_button=browser.find_element_by_xpath('//button[@class="thin-text nav-link"]')
add_to_cart_button.click()
time.sleep(3)
browser.close()