# Certifique-se de que você já instalou os pacotes necessários:
# pip install transformers telebot
# pip install googletrans==4.0.0-rc1

from transformers import pipeline
import telebot
from googletrans import Translator

# Carregar o pipeline de question-answering com o modelo biobert
qa = pipeline('question-answering', model='ktrapeznikov/biobert_v1.1_pubmed_squad_v2', tokenizer='ktrapeznikov/biobert_v1.1_pubmed_squad_v2')

# Definir o contexto para o modelo
context = context = """
Pizza Planet is a family-owned pizzeria known for its unique space theme and welcoming atmosphere. Frequented by Andy Davis and his toys in the film Toy Story, Pizza Planet offers a fun and memorable experience for all ages. Here is some important information and current promotions:

**About the Pizzeria:**
- Address: Rua dos Oompa Loompas, 155, Jardim Florinda, São José Dos Campos-SP
- Opening Hours:
 - Monday to Friday: from 8:00 pm to 11:00 pm
 - Saturday and Sunday: from 7:00 pm to 11:00 pm
- Contact: (12) 3456-7890
- Email: contato@pizzaplanet.com

**Promotions:**
1. **Monday to Friday Promotion**: From Monday to Friday, all large pizzas are 20% off!
2. **Weekend Promotion**: On weekends, buy a large pizza and get a free portion of fries.
3. **Family Combo**: 2 large pizzas + 1 2L soft drink for just R$59.90.
4. **Birthday Promotion**: Is it your birthday? Get a free medium pizza when you present photo ID.
5. **Loyalty Promotion**: Participate in our loyalty program: for every 10 pizzas purchased, receive a free medium pizza.
6. **Launch Promotion**: New pepperoni pizza with catupiry! Try it for 30% off this month.
7. **Happy Hour Promotion**: From 6pm to 8pm, all medium pizzas for just R$19.90.
8. **Promotion for Students**: Students have a 15% discount when presenting their student card.

**Menu:**
- **Pizzas**:
 - Pepperoni, Margherita, Four Cheeses, Chicken with Catupiry, Portuguese, Vegetarian.
- **Drinks**:
 - Soft drinks, juices, water.
- **Desserts**:
 - Chocolate Pizza, Ice Cream, Brownies.

**Additional Services:**
- **Delivery**: We deliver throughout the city of São José Dos Campos. Waiting time approximately 20-30 minutes.
- **Events**: We organize birthday parties and corporate events. Contact us for more details.
- **Loyalty Program**: For every 10 pizzas purchased, receive a free medium pizza.

**How ​​to Place an Order:**
- Visit our website or call (12) 3456-7890 to place your order.
- You can also contact us via WhatsApp: (12) 98765-4321.

**Complaints and Suggestions:**
- To send a complaint or suggestion, send an email to pizzaplanet@disney.com.

We look forward to serving you at Pizza Planet, where every meal is a trip to space!
"""


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
Sábado e Domingo: Das 19:00h às 23:00h"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["endereco"])
def endereco(mensagem):
    bot.send_message(mensagem.chat.id, "Rua dos oompa loompas, 155, Jardim Florinda, São José Dos Campos-SP")


def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='pt', dest='en')
    return translation.text

# Função para responder a perguntas usando o modelo de question-answering
@bot.message_handler(func=lambda message: True)
def responder_pergunta(mensagem):
    question = translate_to_english(mensagem.text)
    result = qa(context=context, question=question)
    resposta = result['answer']
    
    # Verifique se a resposta é relevante
    if resposta.strip() == "" or result['score'] < 0.2:  # Pode ajustar o limiar de score conforme necessário
        bot.send_message("Mensagem não entendida :()")
    else:
        bot.send_message(mensagem.chat.id, resposta)

# Função para exibir o menu padrão
def mostrar_menu(chat_id):
    texto = """
Escolha uma opção para continuar (Clique no item):
    /pedido Fazer um pedido
    /horario Horário de Funcionamento
    /endereco Endereço do Pizza Planet
    /reclamar Fazer uma reclamação
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.send_message(chat_id, texto)

bot.polling()
