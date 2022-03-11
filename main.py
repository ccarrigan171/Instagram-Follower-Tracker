from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Safari()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        login_field = self.driver.find_element(by=By.XPATH, value="//input[@name=\"username\"]")
        login_field.send_keys(username)
        login_field = self.driver.find_element(by=By.XPATH, value="//input[@name=\"password\"]")
        for c in pw:
           login_field.send_keys(c)
           sleep(0.5)
        login_field = self.driver.find_element(by=By.XPATH, value='//button[@type="submit"]')
        login_field.click()
        sleep(5)
        login_field = self.driver.find_element(by=By.XPATH, value="//button[contains(text(),'Not Now')]")
        login_field.click()
        sleep(2)

    def get_unfollowers(self):
        self.driver.maximize_window()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value="//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(2)
        following = self.driver.find_element(by=By.XPATH, value="//a[contains(@href, '/{}/following/')]".format(self.username))
        self.driver.execute_script("arguments[0].click();", following)
        following = self._get_names_following()
        followers = self.driver.find_element(by=By.XPATH, value="//a[contains(@href, '/{}/followers/')]".format(self.username))
        self.driver.execute_script("arguments[0].click();", followers)
        followers = self._get_names_followers()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
    
    def _get_names_following(self):
        sleep(3)
        scroll_box = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[3]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1.25)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements(by=By.TAG_NAME, value='a')
        names = [name.text for name in links if name.text != '']
        #print(names)
        sleep(5)
        # close button
        self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[1]/div/div[2]/button").click()
        return names

    def _get_names_followers(self):
        sleep(3)
        scroll_box = self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1.25)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements(by=By.TAG_NAME, value='a')
        names = [name.text for name in links if name.text != '']
        #print(names)
        sleep(5)
        # close button
        self.driver.find_element(by=By.XPATH, value="/html/body/div[6]/div/div/div/div[1]/div/div[2]/button").click()
        return names


my_bot = InstaBot('YOUR_USERNAME_HERE', 'YOUR_PASSWORD_HERE')
my_bot.get_unfollowers()