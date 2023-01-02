from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, os
from generate_twitter_massage import GenerateMassage


tweet_massage = GenerateMassage('Harimoto Tomokazu', 'Chuang Chih-Yuan').generate_massage()

def get_credentials() -> dict:

    credentials = dict()
    
    
    with open("credentials.txt") as f:
        
        for line in f.readlines():
            try:
                
                key, value = line.split(": ")
            except ValueError:
                
                print('Add your email and password in credentials file')
                exit(0)

            credentials[key] = value.rstrip(" \n")
 
    return credentials

login_data = get_credentials()


class Twitterbot:

    def __init__(self, email, password):


        self.email = email
        self.password = password
        self.username = "tt_matches"
        # initializing chrome options
        chrome_options = Options()

        # adding the path to the chrome driver and
        # integrating chrome_options with the bot
        self.bot = webdriver.Chrome(
            executable_path=os.path.join(os.getcwd(), 'chromedriver'),
            options=chrome_options
        )

    def login(self):
        bot = self.bot
        # fetches the login page
        bot.get('https://twitter.com/login')
        try:

            # adjust the sleep time according to your internet speed
            time.sleep(3)

            email = bot.find_element(By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
            )
            email.send_keys(self.email)
            time.sleep(1)
            next = bot.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
            next.click()
            time.sleep(1)

            password = bot.find_element(By.XPATH,
                '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]'
            )

            password.send_keys(self.password)

            login = bot.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
            login.click()

            time.sleep(5)
        except:
            username = bot.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            username.send_keys(self.username)
            next = bot.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div")
            next.click()

            time.sleep(1)

            password = bot.find_element(By.XPATH,
                                        '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')

            password.send_keys(self.password)

            login = bot.find_element(By.XPATH,
                                     "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")
            login.click()




        tweet = bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet.send_keys(tweet_massage)

        time.sleep(1)

        send = bot.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div")
        send.click()

        time.sleep(20)


me = Twitterbot(login_data["email"], login_data["password"])

me.login()


