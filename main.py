from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "twitter_email"
TWITTER_PASSWORD = "twitter password"
NAME="twitter name"
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.down=0
        self.up=0
    def get_internet_speed(self):
        #firsr we entered speedtest and get the upload net and download net 
        self.driver.get("https://www.speedtest.net/result/16658043737")
        go_button=self.driver.find_element(By.CSS_SELECTOR,".start-button a")
        go_button.click()
        sleep(60)
        self.up=self.driver.find_element(By.XPATH,"result-data-large number result-data-value upload-speed").text
        self.down=self.driver.find_element(By.XPATH,"result-data-large number result-data-value download-speed").text
        print(self.down)
        print(self.up)
    def tweet_at_provider(self):
        #then we login to twitter and tweet to Internet Provider if the net speead as they promised us or not 
        self.driver.get("https://x.com/?logout=1724400108630")
        sleep(5)
        sign_in=self.driver.find_element(By.CLASS_NAME, "css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3")
        sign_in.click()
        sleep(5)
        email=self.driver.find_element(By.CSS_SELECTOR,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label')
        email.send_keys(TWITTER_EMAIL)
        sleep(5)
        next_button=self.driver.find_element(By.CLASS_NAME,"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3" )
        next_button.click()
        sleep(5)
        input_name=self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input')
        input_name.send_keys(NAME)
        sleep(5)
        input_name.send_keys(Keys.ENTER)
        input_password=self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        input_password.send_keys(TWITTER_PASSWORD)
        input_password.send_keys(Keys.ENTER)
        sleep(5)
        tweet=f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_input=self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_input.send_keys(tweet)
        sleep(5)
        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        sleep(2)
        self.driver.quit()
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
