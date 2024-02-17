import os
import openai
openai.api_key = os.getenv("...")

# On déclare une liste pour conserver l'historique de tous nos messages avec ChatGPT
messages = []

# optionnel, permet de définir le comportement que l'assistant doit adopter
messages.append({"role": "system", "content": "Tu es un développeur Python"})

# Une question classique qu'on pourrait poser à ChatGPT
messages.append({"role": "user", "content": "Explique moi comment faire une opération ternaire en Python"})

# Je crée ma requête en choisissant le modèle et en envoyant mes messages
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
)

# La réponse fournie par ChatGPT
response_chatgpt = completion.choices[0].message.content

print(response_chatgpt)
