import email
import os
def processar_resposta(resposta,nome):
    if resposta =='1':
     print(f'{os.linesep}{nome} Projeto calculadora basica, utilizei (HTML5 E CSS) LINK ABAIXO PARA ACESSAR O PROJETO{os.linesep} https://CalculadoraBasica.felipheferreira.repl.co')
    elif resposta =='2':
     print(f'{os.linesep}{nome} Nesse projeto você tera acesso a calculadora media, utilizei (Html5, Css e JavaScript) o Link do projeto esta disponivel logo abaixo:{os.linesep}https://CalculadoraDeMedia.felipheferreira.repl.co')
    elif resposta =='3':
     print(f'{os.linesep}{nome} Criei essa pagina de formulario, meu principal foco foi deixar a pagina responsiva ultilizei (HTML5 E CSS) O LINK DO PROJETO ESTA DISPONIVEL LOGO A BAIXO.{os.linesep}https://FORMULARIO.felipheferreira.repl.co')
    elif resposta =='4':
     print(f'{os.linesep}{nome} Conversor de moedas, veja quanto esta valendo cada moeda em REAL, LINK DO PROJETO{os.linesep}https://github.com/feliphe1906/CONVERSOR-DE-MOEDAS.git')
    elif resposta =='5':
     print(f'{os.linesep}{nome} JOGO MENTALISTA. NESSE JOGO VOCÊ VAI COLOCAR UM NUMERO PARA TENTAR ADVINHAR QUAL NUMERO O COMPUTADOR ESTARÁ PENSANDO, O PROJETO FOI DESENVOLVIDO NA IMERSÃO DEV ALURA, FOI FEITA ALGUMAS MODIFICAÇÕES NA ESTILIZAÇÃO (CSS).BORA BRINCAR? </> LINK DO PROJETO ABAIXO.{os.linesep}https://Jogo-Mentalista.felipheferreira.repl.co')
    else:
     print('Digite apenas 1,2,3,4 ou 5')
def start():
    # Apresentar o chatbot
             print('Olá! Bem Vindo ao meu novo projeto. Todos desenvolvidos por Feliphe Ferreira ')
    # pedir o nome 
nome = input('Digite seu nome:')
    # pedir o e-mail
email = input('Digite seu e-mail:')
while True:
    # Oferecer o menu de opções
    resposta = input( f'Sou Feliphe Ferreira estudante do curso Analise e Desenvolvimento de Sistemas, criei esse chatbot em python com o objetivo de mostrar meus projetos, minhas habilidades e conhecimentos. No momento estudo React native para desenvolvimento mobile (uma area na qual tenho muito interesse em aprender ainda mais). Também tenho muito interesse em Cibersegurança pois me identifico muito. Então é isso vamos la conhecer meus projetos?{os.linesep}[1] - Projeto calculadora{os.linesep}[2] - Projeto Calculadora de média{os.linesep}[3] - Projeto Formulario{os.linesep}[4] - Projeto Conversor de moedas{os.linesep}[5] - Jogo Mentalista{os.linesep}')
    
    # Processar a resposta enviada
    processar_resposta(resposta,nome)
    
    
    
if __name__ == '__main__':
   start()
