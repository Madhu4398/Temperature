"""
Find the least expensive sunscreen and add it to the cart.
SCOPE:
1) Launch Chrome Driver
2) Navigate to least priced sunscreen in SPF-30 and SPF-50.
3) Add that sunscreens to the cart.
4) Open the cart
5) Check if the sum of 2 sunscreens are same.
6) Print the result
7) Close the browser

"""
from selenium import webdriver
import time

# Creating an instance of the web browser and navigating to the sunscreen page
browser = webdriver.Chrome()
browser.get('https://weathershopper.pythonanywhere.com/sunscreen')

# Checking if the control lands on the right web page 
if browser.title=="The best moisturizers in the world!":
   print("Page found")
else:
    print("Page not found")

# Creating a list with prices of all aloe sunscreens
spf_30_prices=list()
spf_30_path=browser.find_elements_by_xpath("//div/p[contains(text(),'SPF-30')]/following-sibling::p[contains(.,'Price')]")
for x in spf_30_path:
    price=int(x.text.strip("Price: Rs. "))
    spf_30_prices.append(price)
print("The prices of the SPF-30 sunscreens are ",spf_30_prices)
# Getting the least expensive spf_30 sunscreen and addeing into the cart
spf_30_min_price=min(spf_30_prices)
print("The least expensive price of SPF-30 sunscreen is",spf_30_min_price)
spf_30_add_button=browser.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(spf_30_min_price))
spf_30_add_button.click()

# Creating a list with prices of all spf_50 sunscreens
spf_50_path=browser.find_elements_by_xpath("//div/p[contains(text(),'SPF-50')]/following-sibling::p[contains(.,'Price')]")
spf_50_prices=list()

for y in spf_50_path:
    price=int(y.text.strip("Price: Rs. "))
    spf_50_prices.append(price)
print("The prices of the SPF-50 sunscreens are ",spf_50_prices)
# Getting the least expensive spf-30 sunscreen and adding into the cart
spf_50_min_price=min(spf_50_prices)
print("The least expensive price of SPF-50 sunscreen is",spf_50_min_price)
spf_50_add_button=browser.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(spf_50_min_price))
spf_50_add_button.click()

# Clicking on cart button to check if the correct sunscreen is added
add_to_cart_button=browser.find_element_by_xpath('//button[@class="thin-text nav-link"]')
add_to_cart_button.click()
total_price=browser.find_element_by_xpath("//p[@class='justify-content-center h4 top-space-20']").text.split(' ')
cart_sum=int(total_price[2])
sum_Of_sunscreen=spf_30_min_price+spf_50_min_price #sum of least spf_30 and spf_50 sunscreen 
#checking if same 2 products are added into the cart
if sum_Of_sunscreen==cart_sum:
    print("Same 2 products are added to the cart") 
else:
    print("Not same products")
time.sleep(3)
browser.close()