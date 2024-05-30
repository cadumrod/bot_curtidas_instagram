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
sleep(random.randint(1,3))

# Clicar e digitar a senha
campo_senha = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
campo_senha.send_keys('2650Duka2299!@')
sleep(random.randint(1,3))

# Clicar no campo entrar
btn_entrar = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[text()='Entrar']")))
sleep(random.randint(1,3))
btn_entrar.click()
sleep(3)

# Navegar até a página alvo
driver.get('https://www.instagram.com/cadu.mrod')

# Clicar na última postagem
postagens = wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, "//div[@class='_aagw']")))
sleep(random.randint(1,5))
postagens[0].click()
sleep(random.randint(1,5))

try:
    # Encontre todos os elementos div pelo nome da classe
    div_elements = wait.until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'x1i10hfl')))
    print(f"Número de elementos div encontrados: {len(div_elements)}")
    sleep(2)
    
    # Iterar sobre os divs encontrados para garantir que estamos pegando o correto
    target_div = None
    for div in div_elements:
        inner_html = div.get_attribute('innerHTML')
        print("HTML do div:", inner_html)
        if '<span' in inner_html and '<svg' in inner_html:
            target_div = div
            break

    if target_div is None:
        raise Exception("Nenhum div contendo span e svg foi encontrado.")

    # Verificar o conteúdo do div selecionado
    print("HTML do div selecionado:", target_div.get_attribute('innerHTML'))
    
    # Tentar encontrar todos os spans dentro do div
    span_elements = target_div.find_elements(By.TAG_NAME, 'span')
    print(f"Número de spans encontrados dentro do div: {len(span_elements)}")

    if not span_elements:
        raise Exception("Nenhum elemento span encontrado dentro do div.")
    
    # Iterar sobre os spans para encontrar aquele que contém o elemento SVG
    svg_element = None
    for span_element in span_elements:
        print("Analisando span:", span_element.get_attribute('outerHTML'))
        try:
            svg_element = span_element.find_element(By.TAG_NAME, 'svg')
            if svg_element:
                print("Elemento SVG encontrado:", svg_element.get_attribute('outerHTML'))
                break
        except Exception as e:
            print("SVG não encontrado no span:", span_element.get_attribute('outerHTML'))
            continue
    
    if svg_element is None:
        raise Exception("Nenhum elemento SVG encontrado dentro de qualquer span.")

    sleep(2)

    # Verifique se a postagem já está curtida
    aria_label = svg_element.get_attribute('aria-label')
    print(f"Valor de aria-label: {aria_label}")
    is_liked = aria_label == 'Descurtir'

    if not is_liked:
        target_div.click()
        print("A postagem foi curtida.")
    else:
        print("A postagem já está curtida.")

except Exception as e:
    print("Erro ao localizar o elemento:", e)



input('')
driver.close()


