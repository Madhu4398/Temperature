'''
SCOPE:
1) Launch Chrome Driver.
2) Navigate to Weathershopper page.
3) Check for the current temperature.
4)if the temperature is below 19 degree.Write test for clicking the  Buy moisturizers button.
5)Else click the Buy Sunsreens button if temperature is above 34 degrees.  
6) Close the browser
'''
import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
# Navigate to Weathershopper page
driver.get("https://weathershopper.pythonanywhere.com/")
if(driver.title=="The best moisturizers in the world!"):
    print ("Success:  page launched successfully")
else:
    print ("Failed:  page Title is incorrect")
# Getting the temperature using the Xpath 
temp=driver.find_element_by_xpath("//span[@id='temperature']").text.split(' ')
temperature=int(temp[0])
print("Temperature =",temperature)
# Checking the conditions related to the temperature

def check_title(product,page_title):
    if product==page_title:
       print("Landed on the product %s page"%product)
    else:
        print("Can't landed the page")
if temperature<19:
# KEY POINT: Locate the button and click on it 
    product="Moisturizers"
    moisturizer_button  = driver.find_element_by_xpath("//button[text()='Buy moisturizers']").click()
    driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
    moisturizer_page=driver.find_element_by_xpath("//h2").text
    print(moisturizer_page)
    check_title(product,moisturizer_page)
elif temperature>34:
    product="Sunscreens"
    suncreens_button  = driver.find_element_by_xpath("//button[text()='Buy sunscreens']").click()
    driver.get("https://weathershopper.pythonanywhere.com/sunscreen")
    sunscreens_page=driver.find_element_by_xpath("//h2").text
    print(sunscreens_page)
    check_title(product,sunscreens_page)
# Pause the script to wait for page elements to load
time.sleep(3)

# Close the browser
driver.close()