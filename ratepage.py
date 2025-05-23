from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random


def post_review(api_data: str):
    chrome_options = Options()
    chrome_options.add_extension('uBlock.crx')
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    link = "https://www.ratemyprofessors.com/add/professor-rating/2574020"
    driver.get(link)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.css-19bb58m")))

    course_code = driver.find_element(By.CSS_SELECTOR, "div.css-19bb58m")
    course_code_input = course_code.find_element(By.CSS_SELECTOR, "input#class")
    course_code_input.send_keys("CSE373")
    course_code_input.send_keys(Keys.RETURN)

    rating_slider = driver.find_elements(By.CSS_SELECTOR, "div.RatingSliderBox__StyledRatingSliderBox-skwa8i-0.hViVZE")[0]
    rating_slider.click()

    rand = random.randint(4,6)
    diff = None
    if rand == 6:
        diff_slider_max = driver.find_elements(By.CSS_SELECTOR, "div.RatingSliderBox__StyledRatingSliderBox-skwa8i-0.iCQVWK")[1]
        diff = diff_slider_max
    else:
        diff_slider = driver.find_elements(By.CSS_SELECTOR, "div.RatingSliderBox__StyledRatingSliderBox-skwa8i-0.fIxeNW")[rand]
        diff = diff_slider
    diff.click()

    take_again_no = driver.find_element(By.CSS_SELECTOR, "input#wouldTakeAgain-No.RadioButtons__StyledRadioButton-sc-1ho7g4w-3.hBJFQm")
    take_again_no.click()

    review_box = driver.find_element(By.CSS_SELECTOR, "textarea.FormTextArea__StyledTextArea-mntwgt-1.eaHDmj")
    review_box.send_keys(api_data)
    