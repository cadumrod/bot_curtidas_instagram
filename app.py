from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
import random

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return driver, wait


driver, wait = iniciar_driver()

# Entrar no site do Instagram
driver.get('https://www.instagram.com/')

# Clicar e digitar meu usuário
campo_usuario = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
campo_usuario.send_keys('cadu.mrod@gmail.com')
sleep(random.randint(1,2))

# Clicar e digitar a senha
campo_senha = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
campo_senha.send_keys('2650Duka2299!@')
sleep(random.randint(1,2))

# Clicar no campo entrar
btn_entrar = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[text()='Entrar']")))
sleep(random.randint(1,2))
btn_entrar.click()
sleep(3)

# Navegar até a página alvo
driver.get('https://www.instagram.com/cadu.mrod')

# Clicar na última postagem
postagens = wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, "//div[@class='_aagw']")))
sleep(random.randint(1,2))
postagens[0].click()
sleep(random.randint(1,2))

# Verificar se está curtido ou não e realizar ação
btn_coracao = driver.find_element(By.XPATH, "//span[@class='x1rg5ohu xp7jhwk']/div/div/span")

if btn_coracao.find_element(By.TAG_NAME, 'svg').get_attribute('class') == 'x1lliihq x1n2onr6 xyb1xck':
    print(btn_coracao)
    btn_coracao.click()

else:
    print('Essa postagem já foi curtida.')




input('')
driver.close()


