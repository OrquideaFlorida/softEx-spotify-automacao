from behave import given, when, then
from features.pages.Spotify_page import Spotify_page
import time

# region Teste Criação_de_Playlist

@given(u'que o usuário está logado no Spotify')
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt")
    context.Spotify_page = Spotify_page(context.driver)
    context.Spotify_page.clicar_botao_logar()
    context.Spotify_page.preencher_campos_login()
    context.Spotify_page.clicar_botao_logar()
    time.sleep(4)

@when(u'clicar no botão Criar playlist')
def step_impl(context):
    context.Spotify_page.clicar_botao_playlist()
    time.sleep(4)

@then(u'a playlist "{texto}" deve ser criada com sucesso')
def step_impl(context,texto):
    assert texto == context.Spotify_page.Verificar_se_playlist_foi_criada()


# endregion

# region Teste Playlist_aparecer_no_tela_inicio

@given(u'Existe uma playlist chamada "{texto}"')
def step_impl(context,texto):
    assert texto == context.Spotify_page.Verificar_se_playlist_foi_criada()

@when(u'visualizar a lista de playlists no perfil')
def step_impl(context):
    raise NotImplementedError(u'STEP: When visualizar a lista de playlists no perfil')

@then(u'a playlist "Minha playlist nº 1" deve aparecer na lista')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a playlist "Minha playlist nº 1" deve aparecer na lista')

# endregion

# region Teste Adicionar_música_na_playlist

@given(u'selecionar playlist chamada "Minha playlist nº 1"')
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt")
    context.Spotify_page = Spotify_page(context.driver)
    context.Spotify_page.clicar_botao_logar()
    context.Spotify_page.preencher_campos_login()
    context.Spotify_page.clicar_botao_logar()
    time.sleep(4)
    context.Spotify_page.clicar_playlist()


@when(u'selecionar a opção de adicionar músicas à playlist')
def step_impl(context):
    context.Spotify_page.buscar_musica()
    time.sleep(2)

@when(u'eu escolho a música "Baby alô" para adicionar à playlist')
def step_impl(context):
    context.Spotify_page.botao_musica()
    time.sleep(2)

@then(u'a música "{texto}" deve ser adicionada com sucesso à playlist "Minha playlist nº 1"')
def step_impl(context,texto):
    assert texto == context.Spotify_page.verificar_musica()
    

# endregion

# region Teste Editar_Playlist

@given(u'playlist chamada "Minha playlist nº 1" contendo a música "Song A"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given playlist chamada "Minha playlist nº 1" contendo a música "Song A"')

@when(u'o usuário edita a playlist para renomeá-la para "Melhores Músicas"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When o usuário edita a playlist para renomeá-la para "Melhores Músicas"')

@when(u'remove a música "Song A" da playlist')
def step_impl(context):
    raise NotImplementedError(u'STEP: When remove a música "Song A" da playlist')

@then(u'a playlist deve ser renomeada para "Melhores Músicas"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a playlist deve ser renomeada para "Melhores Músicas"')

@then(u'a música "Song A" não deve mais estar presente na playlist')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a música "Song A" não deve mais estar presente na playlist')

# endregion

# region Teste Deletar_Playlist

@given(u'uma playlist chamada "Melhores Músicas"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given uma playlist chamada "Melhores Músicas"')

@when(u'selecionar a opção de deletar a playlist')
def step_impl(context):
    raise NotImplementedError(u'STEP: When selecionar a opção de deletar a playlist')

@then(u'a playlist deve ser deletada com sucesso')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a playlist deve ser deletada com sucesso')

@then(u'a playlist não deve mais aparecer na lista de playlists do meu perfil')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a playlist não deve mais aparecer na lista de playlists do meu perfil')

# endregion

# region Teste Orquídea

@given(u'a página inicial de login deve estar aberta') # Clicar no botão de login
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt") #Inserir o endereço
    context.Spotify_page = Spotify_page(context.driver) # Web Driver - Tem que colocar 
    context.Spotify_page.clicar_botao_logar()


@when(u'o usuário digicar a senha no campo "E-mail ou nome de usuário"') # Digitou o e-mail e a senha
def step_impl(context):
    context.Spotify_page.preencher_campos_login()
    

@when(u'digitar a senha no campo "Senha"')
def step_impl(context):
    pass # Ignorar porque já foi preenchido no passo anterior
    #raise NotImplementedError(u'STEP: When digitar a senha no campo "Senha"')


@then(u'o usuário será direcionado à página inicial do Spotify') # Clicar no entrar e direcionado a pág inicial
def step_impl(context):
    context.Spotify_page.clicar_botao_logar()
    time.sleep(5)


@given(u'que o usuário esteja na plataforma') # Precisa fazer os passos anteriores necessários p página de login
def step_impl(context):
    context.driver.get("https://open.spotify.com/intl-pt") #Inserir o endereço
    context.Spotify_page = Spotify_page(context.driver) # Web Driver - Tem que colocar 
    context.Spotify_page.clicar_botao_logar()
    context.Spotify_page.preencher_campos_login()
    context.Spotify_page.clicar_botao_logar()
    time.sleep(5)


@when(u'o usuário digita o nome do artista no campo pesquisa')
def step_impl(context):
    context.Spotify_page.preencher_campos_buscar() #Pega a função que foi criada em Spotify_page
    context.Spotify_page.clicar_botao_buscar()
    time.sleep(5)

@then(u'é mostrado ao usuário o artista desejado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then é mostrado ao usuário o artista desejado')


@given(u'o usuário deve estar logado na plataforma')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given o usuário deve estar logado na plataforma')


@given(u'o usuário estiver no perfil do artista')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given o usuário estiver no perfil do artista')


@when(u'clicar no botão "Seguir"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clicar no botão "Seguir"')


@then(u'deve surgir a mensagem "Conteúdo adicionado à sua biblioteca"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then deve surgir a mensagem "Conteúdo adicionado à sua biblioteca"')


@then(u'o botão "Seguir" mudará para "Seguindo"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o botão "Seguir" mudará para "Seguindo"')


@given(u'o usuário deve estar na pagina de busca')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given o usuário deve estar na pagina de busca')


@when(u'digitar o nome da música')
def step_impl(context):
    raise NotImplementedError(u'STEP: When digitar o nome da música')


@then(u'deve aparecer a música pesquisada e títulos semelhantes')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then deve aparecer a música pesquisada e títulos semelhantes')


@given(u'o usuário deve estar na página de busca')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given o usuário deve estar na página de busca')


@when(u'for digitado o nome do podcast no campo pesquisa')
def step_impl(context):
    raise NotImplementedError(u'STEP: When for digitado o nome do podcast no campo pesquisa')


@then(u'o podcast pesquisado deve aparecer na plataforma')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o podcast pesquisado deve aparecer na plataforma')




