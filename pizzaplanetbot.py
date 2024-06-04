#pip install transformers
from transformers import pipeline
import telebot

qa = pipeline('question-answering', model='ktrapeznikov/biobert_v1.1_pubmed_squad_v2', tokenizer='ktrapeznikov/biobert_v1.1_pubmed_squad_v2')
qa(context='Pizza Planet is a family restaurant frequented by Andy Davis and his toys in Toy Story. The establishment is identifiable by its unique design that employs a space theme.', question='What is Pizza Planet?')

CHAVE_API = "7197106373:AAGDXRTj_rkMkNlZY88wzSuwF5psend6NjU"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza para sua casa. Tempo de espera em 20min")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o brabo para sua casa. Tempo de espera em 20min")

@bot.message_handler(commands=["fritas"])
def fritas(mensagem):
    bot.send_message(mensagem.chat.id,"Saindo fritas para sua casa. Tempo de espera em 20min")

@bot.message_handler(commands=["bauru"])
def bauru(mensagem):
    bot.send_message(mensagem.chat.id,"Saindo um bauru para sua casa. Tempo de espera em 20min")

@bot.message_handler(commands=["pedido"])
def pedido(mensagem):
    texto = """
Bem Vindo ao Pizza Planet, O que deseja? (Clique em uma opção)
    /pizza Pizza
    /fritas Porção de Batatas Fritas
    /hamburguer Hamburguer
    /bauru Bauru"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Reclamar"])
def reclamar(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, envie um email para pizzaplanet@disney.com")

@bot.message_handler(commands=["horario"])
def horario(mensagem):
    texto = """
Segunda à Sexta: Das 20:00h às 23:00h
Sábado e Dommingo: Das 19:00h às 23:00h"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["endereco"])
def endereco(mensagem):
    bot.send_message(mensagem.chat.id, "Rua dos oompa loompas, 155, Jardim Florinda, São José Dos Campos-SP")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Escolha uma opção para continuar (Clique no item):
    /pedido Fazer um pedido
    /horario Horário de Funcionamento
    /endereco Endereço do Pizza Planet
    /reclamar Fazer uma reclamação
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.send_message(mensagem.chat.id, texto)

bot.polling()