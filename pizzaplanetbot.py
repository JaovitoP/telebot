# pip install transformers telebot

from transformers import pipeline
import telebot


qa = pipeline('question-answering', model='ktrapeznikov/biobert_v1.1_pubmed_squad_v2', tokenizer='ktrapeznikov/biobert_v1.1_pubmed_squad_v2')

classifier = pipeline("zero-shot-classification")

intencoes = ["fazer pedido", "pedir uma pizza", "promocoes", "promocao", "horario", "endereco", "reclamar"]

def classificar_intencao(message):
    result = classifier(message, intencoes)
    return result['labels'][0]

CHAVE_API = "7197106373:AAGDXRTj_rkMkNlZY88wzSuwF5psend6NjU"


bot = telebot.TeleBot(CHAVE_API)
@bot.message_handler(commands=["mussarela"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Pizza de Mussarela\U0001F355 \nPreços por tamanho\nBroto: R$:20,00\nMédia: R$:30,00\nFamília: R$:40,00\nTempo de espera em 20min\n------------------------------------------\nSelecione o tamanho da Pizza\n/broto Tamanho Broto\n/media Tamanho Média\n/familia Tamanho Família")

@bot.message_handler(commands=["calabresa"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Pizza de Calabresa\U0001F355 \nPreços por tamanho\n Broto: R$:25,00\nMédia: R$:35,00\nFamília: R$:45,00\n\n------------------------------------------\nSelecione o tamanho da Pizza\n/broto Tamanho Broto\n/media Tamanho Média\n/familia Tamanho Família")

@bot.message_handler(commands=["marguerita"])
def fritas(mensagem):
    bot.send_message(mensagem.chat.id, "Pizza de Calabresa\U0001F355 \nPreços por tamanho\n Broto: R$:25,00\nMédia: R$:40,00\nFamília: R$:55,00\n\n------------------------------------------\nSelecione o tamanho da Pizza\n/broto Tamanho Broto\n/media Tamanho Média\n/familia Tamanho Família")

@bot.message_handler(commands=["portuguesa"])
def bauru(mensagem):
    bot.send_message(mensagem.chat.id, "Pizza Portuguesa\U0001F355 \nPreços por tamanho\n Broto: R$:20,00\nMédia: R$:45,00\nFamília: R$:60,00\n\n------------------------------------------\nSelecione o tamanho da Pizza\n/broto Tamanho Broto\n/media Tamanho Média\n/familia Tamanho Família")

@bot.message_handler(commands=["doce"])
def bauru(mensagem):
    bot.send_message(mensagem.chat.id, "Pizza Doce\U0001F355 \nPreços por tamanho\n Broto: R$:15,00\nMédia: R$:20,00\nFamília: R$:40,00\n\n------------------------------------------\nSelecione o tamanho da Pizza\n/broto Tamanho Broto\n/media Tamanho Média\n/familia Tamanho Família")

@bot.message_handler(commands=["broto","media","familia"])
def bauru(mensagem):
    bot.send_message(mensagem.chat.id, "Saindo a Pizza para sua casa! Tempo de espera: 20 minutos.")


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

@bot.message_handler(func=lambda message: True)
def handle_message(mensagem):
    user_message = mensagem.text
    intent = classificar_intencao(user_message)
    
    if intent == "fazer pedido":
        bot.send_message(mensagem.chat.id, """
            O que deseja pedir hoje?\U0001F355 (Clique em uma opção)
                /mussarela Pizza de Mussarela
                /calabresa Pizza de Calabresa
                /marguerita Pizza Marguerita
                /portuguesa Pizza Portuguesa
                /doce Pizza Doce""")
        
    if intent == "endereco":
        bot.send_message(mensagem.chat.id, "Rua dos oompa loompas, 155, Jardim Florinda, São José Dos Campos-SP")

    if intent == "reclamar":
        bot.send_message(mensagem.chat.id, "Para enviar uma reclamação, envie um email para pizzaplanet@disney.com \U0001F4E7")

    if intent == "horario":
        bot.send_message(mensagem.chat.id, """
            Segunda à Sexta: Das 20:00h às 23:00h\nSábado e Domingo: Das 19:00h às 23:00h""")
        
    if intent == "promocoes":
        bot.send_message(mensagem.chat.id, """
            ***OFERTAS ESPECIAIS***\U0001F4B5
            1. **Promoção de segunda a sexta**: De segunda a sexta, todas as pizzas grandes estão com 20% de desconto!
            2. **Promoção de Final de Semana**: Nos finais de semana, compre uma pizza grande e ganhe uma porção de batata frita grátis.
            3. **Combo Família**: 2 pizzas grandes + 1 refrigerante 2L por apenas R$59,90.
            4. **Promoção de Aniversário**: É seu aniversário? Ganhe uma pizza média grátis apresentando um documento de identidade com foto.
            5. **Promoção Fidelidade**: Participe do nosso programa de fidelidade: a cada 10 pizzas adquiridas, ganhe uma pizza média grátis.
            6. **Promoção de Lançamento**: Nova pizza de calabresa com catupiry! Experimente com 30% de desconto este mês.
            7. **Promoção Happy Hour**: Das 18h às 20h, todas as pizzas médias por apenas R$ 19,90.
            8. **Promoção para Estudantes**: Estudantes têm desconto de 15% na apresentação do cartão de estudante.""")
                         
bot.polling()
