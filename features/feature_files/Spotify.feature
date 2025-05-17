Funcionalidade: Pesquisar Spotify

    @Realizar_login
    Cenário: O usuário deve entrar na plataforma inserindo o seu e-mail e senha
        Dado a página inicial de login deve estar aberta
        Quando o usuário digicar a senha no campo "E-mail ou nome de usuário"
        E digitar a senha no campo "Senha"
        Então o usuário será direcionado à página inicial do Spotify
    
    @Pesquisar_artista
    Cenário: O artista desejado deve aparecer no resultado da busc
        Dado que o usuário esteja na plataforma
        Quando o usuário digita o nome do artista no campo pesquisa
        Então é mostrado ao usuário o artista desejado

    @Seguir_artista
    Cenário: Acompanhar lançamentos e novidades do seu artista favorito
        Dado o usuário deve estar logado na plataforma 
        E o usuário estiver no perfil do artista
        Quando clicar no botão "Seguir"
        Então deve surgir a mensagem "Conteúdo adicionado à sua biblioteca"
        E o botão "Seguir" mudará para "Seguindo"

    @Pesquisa_de_musica
    Cenário: Busca de músicas específicas na plataforma
        Dado o usuário deve estar na pagina de busca
        Quando digitar o nome da música
        Então deve aparecer a música pesquisada e títulos semelhantes

    @Pesquisar_podcast
    Cenário: Deve surgir o Podcast pesquisado na página de busca
        Dado o usuário deve estar na página de busca
        Quando for digitado o nome do podcast no campo pesquisa
        Então o podcast pesquisado deve aparecer na plataforma

