from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class DisparoMsg:
    def __init__(self):
        self.navegadorConfigure()
        self.abrirWhatsapp()
        self.enviarMensagem()

    def navegadorConfigure(self):
        self.options = webdriver.ChromeOptions()
        # Caso queira usar em segundo plano, utilize a option abaixo
        self.options.add_argument("--headless=new")
        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service)

    def abrirWhatsapp(self):
        self.browser.get("https://web.whatsapp.com/")
        # O tempo abaixo é necessario para que o usuario escaneie o código QR e se conecte
        sleep(60)
        print("\033[32;1mWhatsapp aberto\033[0;0m")

    def enviarMensagem(self):
        self.msg = """
    Olá! Isto é apenas um teste.
"""
        self.contatos = ["Grupo0","Grupo1", "Grupo2", "Grupo3", "Grupo4"]
        # Clicando em pesquisar
        self.browser.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
        # Buscanto o primeiro grupo
        self.browser.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys("Grupo0", Keys.ENTER)
        sleep(0.5)
        # Copiando a msg para encaminhar para o primeiro contato
        pyperclip.copy(self.msg)
        self.browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').click()
        self.browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.CONTROL + "v")
        self.browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.ENTER)
        sleep(0.5)

        self.qtdContatos = len(self.contatos)
        self.listElements = self.browser.find_elements(By.CLASS_NAME, '_2AOIt')
        sleep(5)

        if self.qtdContatos % 5 == 0:
            self.qtdBlocos = self.qtdContatos // 5
        else:
            self.qtdBlocos = int(self.qtdContatos // 5) + 1

        for i in range(self.qtdBlocos):
            self.iInicial = i * 5 
            self.iFinal = (i + 1) * 5
        self.listEnviar = self.contatos[self.iInicial:self.iFinal]

        for item in self.listElements:
            msg = msg.replace("\n", "")
            texto = item.text.replace("\n", "")
            elemento = item
                

        # Seleciona a mensagem para enviar e abre a caixa para encaminhar
        ActionChains(self.browser).move_to_element(self.elemento).perform()
        elemento.find_element(By.CLASS_NAME, '_2T2Kt').click()
        sleep(0.5)
        self.browser.find_element(By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div').click()
        self.browser.find_element(By.XPATH, '//*[@id="main"]/span[2]/div/button[4]/span').click()
        sleep(0.5)

        for nome in self.listEnviar:
            # Selecionar contato e apertar enter
            self.browser.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(nome)
            sleep(0.2)
            self.browser.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
            # aperar delete
            self.browser.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.BACK_SPACE)
            self.browser.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
            sleep(3)

DisparoMsg()