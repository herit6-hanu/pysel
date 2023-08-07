import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import elementsrepo

el=elementsrepo

# Initialize the driver to run
driver = webdriver.Chrome()

# Pass the URL to open
url = "https://www.google.com"
driver.get(url)

# Maximize the current window
driver.maximize_window()

# Find the search input element using XPath
search_input=driver.find_element(By.XPATH,'//textarea[@name="q"]')

if search_input.is_displayed():
    print('The search input is displayed, so please search something')
    search_input.send_keys('Elon Musk')
    buttons=driver.find_elements(By.XPATH,'//input[@name="btnK"]')
    occurence_count=len(buttons)
    if occurence_count>0:
        print(f'Occurence count is greater than 0 .The number of occurences {occurence_count}')
        buttons[1].click()
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(7.0)
        try:
            h2_titles=driver.find_elements(By.XPATH,'//div[@class="A9xod ynAwRc ClLRCd q8U8x MBeuO oewGkc LeUQr htnRc"][@role="link"]')
            occurence_count=len(h2_titles)
            for i in range (occurence_count):
                print(i+1," : ",h2_titles[i].get_attribute('text') )
        except Exception as e:
            driver.stack()
    
    else:
        print(f'No button found with the xpath {buttons}')
else:
    print(f'The search input is not displayed on the {url} page')
    driver.quit()

# Get the title of the window
print("Title of the page is:", driver.title)

# Close the browser
driver.quit()

