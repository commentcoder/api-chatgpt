[![Comment utiliser l'API de ChatGPT en Python ?](https://img.youtube.com/vi/O9z1QRsUnRU/maxresdefault.jpg)](https://www.youtube.com/watch?v=O9z1QRsUnRU)

Lien vers la vidéo :
- [Comment utiliser l'API de ChatGPT en Python ?](https://www.youtube.com/watch?v=O9z1QRsUnRU)

---

OpenAI a sorti le point d'accès de son interface de programmation d'application pour communiquer avec Chat GPT le 1er mars 2023.

Vous pouvez l'intégrer à vos projets ou bien utiliser l'API pour utiliser ChatGPT de manière programmatique en fonction de vos besoins.

🔗 Liens utiles :
- L'article de la vidéo : https://www.commentcoder.com/api-chatgpt/
- Installer Python : https://www.commentcoder.com/installer-python/
- Installer Visual Studio Code : https://www.commentcoder.com/visual-studio-code/
- Jupyter sur VSCode : https://code.visualstudio.com/docs/datascience/jupyter-notebooks
- Pricing API OpenAI : https://openai.com/pricing
- Documentation de l'API d'Open AI : https://platform.openai.com/docs/guides/chat

👨‍💻 Code : 

```
import openai

openai.api_key = "sk-XXXXXXX"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Quelle distance sépare la terre de la lune ?"}
    ]
)

print(response)

print(response.choices[0].message.content)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user", "content": "Et pour Jupiter ?"
    }]
)

print(response.choices[0].message.content)

messages = []

messages.append({"role": "system", "content": "Tu es une IA utile qui répond aux questions posées."})

messages.append({"role": "user", "content": "Quelle distance sépare la terre de la lune ?"})

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(completion.choices[0].message.content)

messages.append({"role": "assistant", "content": completion.choices[0].message.content})

messages.append({"role": "user", "content": "Et pour Jupiter ?"})

for message in messages:
    print(message)

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(completion.choices[0].message.content)
```

Pour pouvoir suivre ce tutoriel vous aurez besoin de Python d'installer sur votre machine. Ainsi qu’un interpreteur Python ou un IDE de votre choix, pour ce tuto, j'utilise Visual Studio code et Jupyter pour interagir avec l’API de ChatGPT.

Vous pourrez trouver tous les liens pour installer Python, Visual Studio Code et Jupyter en description de cette video.

Une fois que vous avez tout installé, commencez par installer le module Python d’openAI avec la commande pip install Open AI.

Une fois installé on va l'importer dans notre script python avec `import openai`

Ensuite, on va devoir fournir une clé d’API qu'on peut récupérer sur le site d’Open AI.

Pour ça ouvrez un navigateur et rendez-vous sur le site platform.openai.com. 

Si n’avez pas encore de compte, créez-en un. Sinon connectez vous.

Il faut savoir que l’utilisation de l’API d’OpenAI a un coût. Pour nos requêtes avec le modèle GPT-3.5-turbo, il est de 1/5 centime de dollars américains pour 1000 token.

Je vous reparle des tokens plus tard dans cette vidéo pour savoir ce que ca représente.

OpenAI offre des crédits gratuits quand on crée un nouveau compte. Pour vérifier que vous avez des crédits gratuits, allez dans Usage et vous devrez voir un “Free trial usage” qui est de 5 dollars au moment où je tourne cette vidéo.

Si vous voyez que vous avez un Free trial usage de 0.00 sur 0.00, il faudra ajouter un mode de paiement ou bien créer un nouveau compte OpenAI.


---

🚀 Envie d'aller plus loin ?
- Pratiquez Python avec 200+ exercices : https://www.commentcoder.com/cours/python-exercices/
- Abonnez-vous pour plus de vidéos sur Python : https://www.youtube.com/channel/UCEztUC2WwKEDkVl9c6oUoTw?sub_confirmation=1
- Détails du projet : https://github.com/commentcoder/bot-discord-py-replit
- Posez vos questions sur discord : https://discord.gg/2AubRA4eBQ

🐍 Mes autres tutoriels en Python :
- [Apprendre Python en 1 heure - Cours complet pour débutant en Python](https://www.youtube.com/watch?v=5EnpNI2iCZA)
- [Apprendre Django en 1 heure - Cours complet pour débutant en Python](https://www.youtube.com/watch?v=xJNvJaLl8bU)
- [Comment créer un bot de clic en Python ?](https://www.youtube.com/watch?v=yEYN4P0lRzY)
- [Comment créer un bot discord en Python ?](https://www.youtube.com/watch?v=LHF1dgwW6aw)
- [Comment créer un bot telegram en Python ?](https://www.youtube.com/watch?v=vF7MaDR6zX4)
