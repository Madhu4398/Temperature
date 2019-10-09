"""
Find the least expensive moisturizer and add it to the cart.
SCOPE:
1) Launch Chrome Driver
2) Navigate to least priced Moisturizer in Aloe and Almond.
3) Add that moisturizers to the cart.
4) Open the cart
5) Check if the sum of 2 moisturizers are same.
6) Print the result
7) Close the browser

"""
from selenium import webdriver
import time

# Creating an instance of the web browser and navigating to the Moisturizer page
browser = webdriver.Chrome()
browser.get('https://weathershopper.pythonanywhere.com/moisturizer')

# Checking if the control lands on the correct web page 
if browser.title=="The best moisturizers in the world!":
   print("Page found")
   
else:
    print("Page not found")

# Creating a list with prices of all aloe moisturizers
aloe_prices=list()
Aloe_path=browser.find_elements_by_xpath("//div/p[contains(text(),'Aloe')]/following-sibling::p[contains(.,'Price')]")
for x in Aloe_path:
    price=int(x.text.strip("Price: Rs. "))
    aloe_prices.append(price)
print("The prices of the aloe moisturizers are ",aloe_prices)
# Getting the least expensive aloe moisturizer and addeing into the cart
aloe_min_price=min(aloe_prices)
print("The least expensive price of aloe moisturizer is",aloe_min_price)
aloe_add_button=browser.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(aloe_min_price))
aloe_add_button.click()

# Creating a list with prices of all almond moisturizers
Almond_path=browser.find_elements_by_xpath("//div/p[contains(text(),'Almond')]/following-sibling::p[contains(.,'Price')]")
almond_prices=list()

for y in Almond_path:
    price=int(y.text.strip("Price: Rs. "))
    almond_prices.append(price)
print("The prices of the almond moisturizers are ",almond_prices)
# Getting the least expensive aloe moisturizer and adding into the cart
almond_min_price=min(almond_prices)
print("The least expensive price of almond moisturizer is",almond_min_price)
almond_add_button=browser.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(almond_min_price))
almond_add_button.click()

# Clicking on cart button to check if the correct moisturizer is added
add_to_cart_button=browser.find_element_by_xpath('//button[@class="thin-text nav-link"]')
add_to_cart_button.click()
total_price=browser.find_element_by_xpath("//p[@class='justify-content-center h4 top-space-20']").text.split(' ')
cart_sum=int(total_price[2])
sum_Of_moisturizer=aloe_min_price+almond_min_price #sum of least aloe and almond moisturizer 
#checking if same 2 products are added into the cart
if sum_Of_moisturizer==cart_sum:
    print("Same 2 products are added to the cart") 
else:
    print("Not same products")
time.sleep(3)
browser.close()