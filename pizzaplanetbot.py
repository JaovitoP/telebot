# Certifique-se de que você já instalou os pacotes necessários:
# pip install transformers telebot

from transformers import pipeline
import telebot
from googletrans import Translator

translator = Translator()

# Carregar o pipeline de question-answering com o modelo biobert
qa = pipeline('question-answering', model='ktrapeznikov/biobert_v1.1_pubmed_squad_v2', tokenizer='ktrapeznikov/biobert_v1.1_pubmed_squad_v2')

# Definir o contexto para o modelo
context = context = """
Pizza Planet is a fictional themed restaurant and arcade that appears in the universe of Toy Story, an animated film series produced by Pixar Animation Studios and distributed by Walt Disney Pictures.
1. **Monday to Friday Promotion**: On this Promotion, From Monday to Friday, all large pizzas are 20% off!
2. **Weekend Promotion**: On weekends, buy a large pizza and get a free portion of fries.
3. **Family Combo**: 2 large pizzas + 1 2L soft drink for just R$59.90.
4. **Birthday Promotion**: Is it your birthday? Get a free medium pizza when you present photo ID.
5. **Loyalty Promotion**: Participate in our loyalty program: for every 10 pizzas purchased, receive a free medium pizza.
6. **Launch Promotion**: New pepperoni pizza with catupiry! Try it for 30% off this month.
7. **Happy Hour Promotion**: From 6pm to 8pm, all medium pizzas for just R$19.90.
8. **Promotion for Students**: Students have a 15% discount when presenting their student card.
"""

contexto_traduzido = translator.translate(context, src='en', dest='pt')


# Chave API do Telegram
CHAVE_API = "7197106373:AAGDXRTj_rkMkNlZY88wzSuwF5psend6NjU"

# Inicializar o bot do Telegram
bot = telebot.TeleBot(CHAVE_API)

# Comandos predefinidos
@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a pizza para sua casa. Tempo de espera em 20min")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo o brabo para sua casa. Tempo de espera em 20min")

@bot.message_handler(commands=["fritas"])
def fritas(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo fritas para sua casa. Tempo de espera em 20min")

@bot.message_handler(commands=["bauru"])
def bauru(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo um bauru para sua casa. Tempo de espera em 20min")

@bot.message_handler(commands=["pedido"])
def pedido(mensagem):
    texto = """
O que deseja pedir hoje?\U0001F355 (Clique em uma opção)
    /pizza Pizza
    /fritas Porção de Batatas Fritas
    /hamburguer Hamburguer
    /bauru Bauru"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["promocoes"])
def pedido(mensagem):
    texto = """
***OFERTAS ESPECIAIS***\U0001F4B5
1. **Promoção de segunda a sexta**: De segunda a sexta, todas as pizzas grandes estão com 20% de desconto!
2. **Promoção de Final de Semana**: Nos finais de semana, compre uma pizza grande e ganhe uma porção de batata frita grátis.
3. **Combo Família**: 2 pizzas grandes + 1 refrigerante 2L por apenas R$59,90.
4. **Promoção de Aniversário**: É seu aniversário? Ganhe uma pizza média grátis apresentando um documento de identidade com foto.
5. **Promoção Fidelidade**: Participe do nosso programa de fidelidade: a cada 10 pizzas adquiridas, ganhe uma pizza média grátis.
6. **Promoção de Lançamento**: Nova pizza de calabresa com catupiry! Experimente com 30% de desconto este mês.
7. **Promoção Happy Hour**: Das 18h às 20h, todas as pizzas médias por apenas R$ 19,90.
8. **Promoção para Estudantes**: Estudantes têm desconto de 15% na apresentação do cartão de estudante."""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["reclamar"])
def reclamar(mensagem):
    bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, envie um email para pizzaplanet@disney.com \U0001F4E7")

@bot.message_handler(commands=["horario"])
def horario(mensagem):
    texto = """
Segunda à Sexta: Das 20:00h às 23:00h
Sábado e Domingo: Das 19:00h às 23:00h"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["endereco"])
def endereco(mensagem):
    bot.send_message(mensagem.chat.id, "Rua dos oompa loompas, 155, Jardim Florinda, São José Dos Campos-SP")

# Função para responder a perguntas usando o modelo de question-answering
@bot.message_handler(func=lambda message: True)
def responder_pergunta(mensagem):
    question = mensagem.text
    question_traduzida_obj = translator.translate(question, src='pt', dest='en')
    question_traduzida = question_traduzida_obj.text
    result = qa(context=context, question=question_traduzida)
    resposta = result['answer']
    
    # Verifique se a resposta é relevante
    if resposta.strip() == "" or result['score'] < 0.2:  # Pode ajustar o limiar de score conforme necessário
        mostrar_menu(mensagem.chat.id)
    else:
        try:
                    resposta_traduzida_obj = translator.translate(resposta, src='en', dest='pt')
                    resposta_traduzida = resposta_traduzida_obj.text
                    bot.send_message(mensagem.chat.id, resposta_traduzida)
        except Exception as e:
                    bot.send_message(mensagem.chat.id, f"Erro ao traduzir a resposta: {str(e)}")
                    bot.send_message(mensagem.chat.id, resposta)  # Envia a resposta original em


# Função para exibir o menu padrão
def mostrar_menu(chat_id):
    texto = """
Escolha uma opção para continuar (Clique no item):
    /pedido Fazer um pedido
    /promocoes Visualizar Promoções
    /horario Horário de Funcionamento
    /endereco Endereço do Pizza Planet
    /reclamar Fazer uma reclamação
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.send_message(chat_id, texto)

bot.polling()
