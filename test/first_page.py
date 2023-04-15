from selenium.webdriver.support import expected_conditions as ec
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test.config import PASSWORD

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "platformVersion": "11",
    "appPackage": "com.datamed.retention",
    "appActivity": ".DisclaimerActivity"
}


def test_entry_system_button():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    button = driver.find_element(By.ID, "com.datamed.retention:id/continueBtn")
    button.click()
    wait = WebDriverWait(driver, 10)
    expected_element = wait.until(ec.visibility_of_element_located((By.ID, 'com.datamed.retention:id/carerLogInButton')))
    assert expected_element is not None, 'Expected page did not load correctly'
    driver.quit()


def test_exit_button():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    button = driver.find_element(By.ID, "com.datamed.retention:id/exitButton")
    button.click()
    wait = WebDriverWait(driver, 10)
    expected_element = wait.until(ec.visibility_of_element_located((By.ID, 'com.android.launcher3:id/apps_list_view')))
    assert expected_element is not None, 'Expected page did not load correctly'
    driver.quit()


def test_easter_egg():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    button = driver.find_element(By.ID, "com.datamed.retention:id/continueBtn")
    button.click()
    driver.implicitly_wait(4)
    button = driver.find_element(By.ID, "com.datamed.retention:id/logo")
    for i in range(0, 8):
        button.click()
    wait = WebDriverWait(driver, 10)
    expected_element = wait.until(ec.visibility_of_element_located((By.ID, 'com.datamed.retention:id/patient_id_txt')))
    assert expected_element is not None, 'Expected page did not load correctly'
    driver.quit()


def test_button_test():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    button = driver.find_element(By.ID, "com.datamed.retention:id/continueBtn")
    button.click()
    driver.implicitly_wait(4)
    button = driver.find_element(By.ID, "com.datamed.retention:id/logo")
    for i in range(0, 8):
        button.click()
    driver.implicitly_wait(4)
    patient_id = driver.find_element(By.ID, "com.datamed.retention:id/patient_id_txt")
    patient_id.send_keys("P88")
    url = driver.find_element(By.ID, "com.datamed.retention:id/url_txt")
    url.send_keys("https://retention-csb-test.biomed.ntua.gr")

    test_button = driver.find_element(By.ID, "com.datamed.retention:id/testBtn")
    test_button.click()
    wait = WebDriverWait(driver, 10)
    popup = wait.until(ec.text_to_be_present_in_element((By.XPATH, '/hierarchy/android.widget.Toast'), 'Test successful'))

    assert popup is not None, 'Test button does not work'
    driver.quit()


def test_button_test_failed():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    button = driver.find_element(By.ID, "com.datamed.retention:id/continueBtn")
    button.click()
    driver.implicitly_wait(4)
    button = driver.find_element(By.ID, "com.datamed.retention:id/logo")
    for i in range(0, 8):
        button.click()
    driver.implicitly_wait(4)
    patient_id = driver.find_element(By.ID, "com.datamed.retention:id/patient_id_txt")
    patient_id.send_keys("P88")
    url = driver.find_element(By.ID, "com.datamed.retention:id/url_txt")
    url.send_keys("dummy")

    test_button = driver.find_element(By.ID, "com.datamed.retention:id/testBtn")
    test_button.click()
    wait = WebDriverWait(driver, 10)
    popup = wait.until(ec.text_to_be_present_in_element((By.XPATH, '/hierarchy/android.widget.Toast'), 'Test failed'))

    assert popup is not None, 'Test button with dummy data does not work'
    driver.quit()


def test_submit_button():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    button = driver.find_element(By.ID, "com.datamed.retention:id/continueBtn")
    button.click()
    driver.implicitly_wait(4)
    button = driver.find_element(By.ID, "com.datamed.retention:id/logo")
    for i in range(0, 8):
        button.click()
    driver.implicitly_wait(4)
    patient_id = driver.find_element(By.ID, "com.datamed.retention:id/patient_id_txt")
    patient_id.send_keys("P88")
    url = driver.find_element(By.ID, "com.datamed.retention:id/url_txt")
    url.send_keys("https://retention-csb-test.biomed.ntua.gr")

    admin = driver.find_element(By.ID, "com.datamed.retention:id/admin_pass")
    admin.send_keys(PASSWORD)

    submit_button = driver.find_element(By.ID, "com.datamed.retention:id/admin_submit")
    submit_button.click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(ec.visibility_of_element_located((By.ID, 'com.datamed.retention:id/carerLogInButton')))

    assert element is not None, 'Submit button does not work'
    driver.quit()


def test_submit_button_failed():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    button = driver.find_element(By.ID, "com.datamed.retention:id/continueBtn")
    button.click()
    driver.implicitly_wait(4)
    button = driver.find_element(By.ID, "com.datamed.retention:id/logo")
    for i in range(0, 8):
        button.click()
    driver.implicitly_wait(4)
    patient_id = driver.find_element(By.ID, "com.datamed.retention:id/patient_id_txt")
    patient_id.send_keys("P88")
    url = driver.find_element(By.ID, "com.datamed.retention:id/url_txt")
    url.send_keys("https://retention-csb-test.biomed.ntua.gr")

    submit_button = driver.find_element(By.ID, "com.datamed.retention:id/admin_submit")
    submit_button.click()
    wait = WebDriverWait(driver, 10)
    popup = wait.until(ec.text_to_be_present_in_element((By.XPATH, '/hierarchy/android.widget.Toast'), 'Please insert all necessary details'))

    assert popup is not None, 'Submit button with no data does not work'
    driver.quit()

