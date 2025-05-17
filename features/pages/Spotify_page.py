from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class Spotify_page(BasePage):
    CAMPO_EMAIL = (By.ID, 'login-username') #Criar o campo
    CAMPO_SENHA = (By.ID, "login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR,'button[data-testid="login-button"]')
    BUTTON_PLAYLIST = (By.CSS_SELECTOR,'button[data-encore-id="buttonPrimary"')
    PLAYLIST = (By.CSS_SELECTOR, '[data-encore-id="listRowTitle"] span')
    BOTAO_PLAYLIST = (By.CSS_SELECTOR, 'div.RowButton-sc-xxkq4e-0') # Age como um botão mas é um campo
    BUSCA_MUSICA = (By.CSS_SELECTOR, 'input.FeWwGSRANj36qpOBoxdx')
    BOTAO_BUSCAR = (By.CSS_SELECTOR, 'input.NtkAQg9R1r5CjuP0XHwl') # Selecionar botão buscar
    PESQUISAR_ARTISTA = (By.CSS_SELECTOR, 'a.hNvCMxbfz7HwgzLjt3IZ') 
    ADICIONAR_MUSICA = (By.CSS_SELECTOR, 'div[aria-rowindex="1"] button[data-testid="add-to-playlist-button"]')
    NOME_MUSICA = (By.CSS_SELECTOR, 'div.btE2c3IKaOXZ4VNAb8WQ') 

    def preencher_campos_login(self):
        campo_email = self.find_element(*self.CAMPO_EMAIL) #Atribuir o e-mail ao campo
        campo_email.send_keys('Weslley3442@hotmail.com')
        campo_senha = self.find_element(*self.CAMPO_SENHA) #Atribui a senha
        campo_senha.send_keys('30305688w&Sll@y')
    
    def clicar_botao_logar(self):
        self.find_element(*self.LOGIN_BUTTON).click()

    def clicar_botao_playlist(self):
        self.find_element(*self.BUTTON_PLAYLIST).click()

    def Verificar_se_playlist_foi_criada(self):
        return self.find_element(*self.PLAYLIST).text
    
    def clicar_playlist(self):
        self.find_element(*self.BOTAO_PLAYLIST).click()

    def buscar_musica(self):
        campo_musica = self.find_element(*self.BUSCA_MUSICA)
        campo_musica.send_keys('Baby alô')

    def botao_musica(self):
        self.find_element(*self.ADICIONAR_MUSICA).click()

    def verificar_musica(self):
        return self.find_element(*self.NOME_MUSICA).text
    
    def preencher_campos_buscar(self):
        campo = self.find_elements(*self.PESQUISAR_ARTISTA) # Pega a função criada em base_page
        campo[1].click()
        
    def clicar_botao_buscar(self):
        botao = self.find_element(*self.BOTAO_BUSCAR)
        botao.send_keys('Dua lipa')
        
