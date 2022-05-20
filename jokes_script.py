import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get('https://www.rd.com/list/short-jokes/')
driver.maximize_window()
print("Driver setup done.")

questions = []
answers = []
i = 1
j = 3
while i <= 67:
    path = f'/html/body/main/section[2]/section[{i}]/section[2]/div[{j}]/'
    print(path)
    try:
        question = driver.find_element(By.XPATH, value=path + 'h2')
        answer = driver.find_element(By.XPATH, value = path + 'p')
        questions.append(question.text)
        answers.append(answer.text)
    except Exception as e:
        print(e)
    j += 1
    if j > 3:
        j = 1
        i += 2


print(questions)
print(answers)