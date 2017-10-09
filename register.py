import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

targetSite = "http://way2automation.com/way2auto_jquery/index.php"


class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_register(self):
        driver = self.driver
        self.driver.maximize_window()
        self.driver.get(targetSite)
        self.driver.implicitly_wait(10)

        # step
        form_name = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/form/fieldset[1]/input')
        form_name.send_keys("Jan")

        # step
        forum_phone = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/form/fieldset[2]/input')
        forum_phone.send_keys('666666666')

        # step
        form_email = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/form/fieldset[3]/input')
        form_email.send_keys("mail@mail.com")

        # step
        form_country = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/form/fieldset[4]/select')
        for option in form_country.find_elements_by_tag_name("option"):
            if option == "Cameroon":
                option.click()
                break

        # step
        form_city = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/form/fieldset[5]/input')
        form_city.send_keys("Warszawa")

        # step
        form_username = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/form/fieldset[6]/input')
        form_username.send_keys("Loremipsum")

        # step
        form_password = driver.find_element_by_xpath('//*[@id="load_form"]/fieldset[7]/input')
        form_password.send_keys("dupajasiu")

        # step
        submit_btn = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/form/fieldset[7]/input')
        submit_btn.click()

    def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
        unittest.main()