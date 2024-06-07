from transformers import pipeline

# Carregar o pipeline de question-answering com o modelo biobert
qa = pipeline('question-answering', model='ktrapeznikov/biobert_v1.1_pubmed_squad_v2', tokenizer='ktrapeznikov/biobert_v1.1_pubmed_squad_v2')

# Contexto e pergunta
context = 'Pizza Planet is a family restaurant frequented by Andy Davis and his toys in Toy Story. The establishment is identifiable by its unique design that employs a space theme.'
question = 'What is Pizza Planet?'

# Executar o pipeline
result = qa(context=context, question=question)

print(result['answer'])
