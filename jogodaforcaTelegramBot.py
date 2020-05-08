import telebot
from telebot import types
import re
import random
from telebot import util
import pandas as pd

bot = telebot.TeleBot("YOUR TOKEN HERE")

updates = bot.get_updates()

user_dic={}
count=0


# Copiar a partir daqui
import unicodedata

# Remove acentuação e passa para minuscula
def strip_accents(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text).lower()


partida_forca=0


@bot.message_handler(commands=['forca'])
def forca_partida(message):
    global partida_forca
    global palavra_atualizada
    global dica
    global palavra_escolhida
    global error
    global rodadas
    
    HANGMANPICS = [
        '''```
            +---+
            |   |
                |
                |
                |
                |
           =========
         ```''', '''```
            +---+
            |   |
            o   |
                |
                |
                |
           =========
           ```''', '''```
            +---+
            |   |
            o   |
            |   |
                |
                |
           =========
           ```''', '''```
            +---+
            |   |
            o   |
           /|   |
                |
                |
           =========
           ```''', '''```
            +---+
            |   |
            o   |
           /|\  |
                |
                |
           =========
           ```''', '''```
            +---+
            |   |
            o   |
           /|\  |
           /    |
                |
           ========
           ```''', '''```
            +---+
            |   |
            o   |
           /|\  |
           / \  |
                |
           ========
           ```'''
        ]
    
    if partida_forca==0:
        
        # Inicializando variáveis
        error = -1
        rodadas = 1

        # Base de dados de palavras
        df = pd.read_csv('forca_palavras2.csv', header=None, encoding='latin-1')

        # Palavra escolhida
        randomico = random.randint(0, len(df) - 1)
        palavra_escolhida = strip_accents(df.iloc[randomico][0])
        dica = df.iloc[randomico][1]
        
        # Gabarito
        print(palavra_escolhida)

        # Palavra a ser revelada
        palavra_atualizada = [' _ ' if i not in [' ',',','.','-','_'] else ' '+i+' ' for i in list(palavra_escolhida)]
        bot.reply_to(message, ''.join(palavra_atualizada) + '\n' + 'DICA: ' + dica)
        
        # Partida em andamento
        partida_forca=1
    
    else:
        
        # Função para converter em minuscula e sem acentuacao
        message.text = strip_accents(message.text)
        
        # Pegar letra soletrada
        escolha = re.findall('/forca (.*)', message.text)
        if len(escolha) >= 1: 
            
            # Soletrando
            if len(escolha[0]) == 1:
                encontrado = 0
                for i in range(len(list(palavra_escolhida))):
                    if list(palavra_escolhida)[i] == escolha[0]:
                        palavra_atualizada[i] = escolha[0]
                        encontrado = 1
                # Erro
                if encontrado == 0:
                    error += 1
                    print(error)
                    bot.reply_to(message, HANGMANPICS[error], parse_mode='Markdown')

                if ''.join(palavra_atualizada)==palavra_escolhida:
                    bot.reply_to(message, """ACERTOU!!!\nPalavra escolhida: {}\nGanhador: {}\nTotal de rodadas: {}
                                 """.format(palavra_escolhida, message.from_user.first_name, str(rodadas)))
                    # Partida termina
                    partida_forca=0

                else:
                    bot.reply_to(message, ''.join(palavra_atualizada) + '\n' + 'DICA: ' + dica)

            # Chutando
            if len(escolha[0]) > 1:
                if escolha[0] == palavra_escolhida:
                    bot.reply_to(message, 
                                 """ACERTOU!!!\nPalavra escolhida: {}\nGanhador: {}\nTotal de rodadas: {}
                                 """.format(palavra_escolhida, message.from_user.first_name, str(rodadas)))
                    # Partida termina
                    partida_forca=0
                else:
                    error += 1
                    print(error)
                    bot.reply_to(message, HANGMANPICS[error], parse_mode='Markdown')
                    bot.reply_to(message, ''.join(palavra_atualizada) + '\n' + 'DICA: ' + dica)


            # Contador de rodadas
            rodadas+=1

            if error >= 6:
                bot.reply_to(message, """PERDEU!!!\nPalavra escolhida: {}\nNenhum ganhador!\nTotal de rodadas: {}
                                 """.format(palavra_escolhida, str(rodadas)))
                # Partida termina
                partida_forca=0
        
        

bot.polling()
