import time
import random
from selenium import webdriver

def getView(link, views):
    try:
        # Create a Chrome WebDriver instance
        browser = webdriver.Chrome('chromedriver.py')

        for i in range(views+1):
            # Open the YouTube video link
            browser.get(link)

            # Generate a random sleep time between 45 and 50 seconds
            sleep_time = random.randint(45, 50)

            print("Running the video for {} time".format(i))
            print("Sleep time is", sleep_time)
            print("------------------------------------------------")

            # Wait for the specified sleep time
            time.sleep(sleep_time)

        # Quit the browser after finishing the loop
        browser.quit()

    except Exception as err:
        print(err)
