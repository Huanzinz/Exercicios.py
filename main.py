-------------------------------------
#Parte1 Exercícios sem seta
------------------------------
# len()
nome = "Gustavo"
imprimir(len(nome))  # 7
--------------------------
# Concatenação
letras = "ABCDE"
imprimir(letras + "FGHI") # ABCDEFGHI
----------------------------------------
# Repetiição de caracteres
imprimir(letras + "G" *6)  # ABCDEFGGGGGG
imprimir("A" + "-"*5 + "A")  # A-----A
---------------------------------------------
# Fadiga de corda
cidade = "Fortaleza"
imprimir(cidade[0:3])  # Para
imprimir(cidade[4:])  # aleza
---------------------------------------
# Índice de string
alfabeto = "abcdefghijklmnopqrstuvwxyz"
imprimir(alfabeto[1])  # b
imprimir(alfabeto[5])  # f
--------------------------------------------
# Parte 2 Exercicios Com as Setas
------------------------------------------------
# Remove espaços de uma string
nome = 'Ju ve n a l d o Flo ren tin o'
nome = "".join(nome.split())
imprimir(nome) # Resultado -> JuvenaldoFlorentino
# ('') -> Aspas Simples tem a função de indicar que o conteúdo é uma String, ou seja, um texto;
# (.split) -> Separa uma String em partes, utilizadno os espaços como separadores por Padrão;
# (.) -> O Ponto é usado para acessar um método, uma função associada a um objeto;
# ("") -> As Aspas normais representam uma String Vazia.
# (join) -> Junta todos os elementos da lista em uma string
----------------------------------------------------------------------------------------------------------
# Utilizando Regex para separar as palavras
import re
partes = re.findall(r'[A-Z][a-z]*', nome)
nome_corrigido = " ".join(partes)

imprimir(nome_corrigido) # Resultado: Juvenaldo Florentino
# (import)-> Importa algo para o programa
# (re)-> Significa Regular Expressions (Expressões Regulares), ele permite que nós trabalhemos com padrões de texto;
# (findall)-> Procura partes de um texto que correspondam a determinado padrão;
# (*)-> Zero ou mais repetições do elemento anterior;
# (.)-> Serve para acessar um método de um objeto.
-----------------------------------------------------------------------------------------------------------------------------
# Manipulação de Texto
# .lower() -> Deixa tudo minúsculo
texto = "FLAMENGO melhor que palMeiRas"
print(texto.lower()) # Resultado: flamengo melhor que palmeiras
---------------------------------------------------------------------
# .upper() -> Deixa tudo maiúsculo
texto = "Palmeiras melhor que flamengo"
print(texto.upper()) # Resultado: PALMEIRAS MELHOR QUE FLAMENGO
---------------------------------------------------------------------
# .capitalize() -> Primeira letra maiúscula
texto = "flamengo melhor que palmeiras"
print(texto.capitalize()) # Resultado: Flamengo melhor que palmeiras
------------------------------------------------------------------------
# .title() -> Primeira Letra de Cada Palavra Maiúscula
texto = "flamengo melhor que palmeiras"
print(texto.title()) # Resultado: Flamengo Melhor Que Palmeiras
------------------------------------------------------------------------
# .swampcase() -> Inverte maiúsculas e minúsculas
texto = "palmeiras Melhor quE FLAMENGO"
print(texto.swapcase()) # Resultado: PALMEIRAS mElHOR QUe flamengo
--------------------------------------------------------------------
# .casefold() -> Versão mais agressiva do .lower()
texto = "PALMEIRAS MELHOR QUE FLAMENGO"
print(texto.casefold()) # Resultado: palmeiras melhor que flamengo
--------------------------------------------------------------------------
# Manipulação de Espaços
# .strip() -> Remove espaços do inicio ao fim
frase = "       Salve        "
print(frase.strip())  
--------------------------------------------------
# .lstrip() -> Remove apenas do lado esquerdo
frase = "       Salve        "
print(frase.lstrip()) 
--------------------------------------------------
# .rstrip() -> Remove apenas do lado direito
frase = "       Salve        "
print(frase.rstrip()) 
---------------------------------------------
# .removeprefix() -> Remove prefixo
print("Ruby2".removeprefix("Ruby")) 
---------------------------------------------------
# .removesufix() -> Remove sufixo
print("Minecraft.exe".removesuffix(".exe"))
-------------------------------------------------
# Substituição e Formatação
# .replace() -> Substitui Texto
frase = "Eu gosto de ouvir Daniel Caesar"
print(frase.replace("Daniel Caesar", "Malcolm Todd")) #Resultado: Eu gosto de ouvir Malcolm Todd
-----------------------------------------------------------------------------------------
# .format() -> Insere valores em {}
-------------------------------------------------
print("Eu gosto de jogar {}".format("FIFA")) #Resultado: Eu gosto de jogar FIFA
--------------------------------------------------------------------------------------------------------
# .format_map() -> Usa dicionário direto
dados = {"nome": "Huan", "idade": 18}
print("Nome: {nome}, Idade:{idade}".format_map(dados)) #Resultado: Nome: Huan Idade: 18
---------------------------------------------------------------------------------------------
# .expandtabs() -> Troca \t por espaços
print("Coluna1\tColuna2".expandtabs(15)) #Resultado: Coluna1        Coluna2
------------------------------------------------------------------------------------
# .translate() -> Substitui caracteres conforme tabela
tabela = str.maketrans("abcde", "9876")
print("copilot".translate(tabela)) 
---------------------------------------------------------
