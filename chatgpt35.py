import openai

# Configurer une clé d'API valide
openai.api_key = "sk-tacleapi-XXXXXXXXXXXXXXXXXXX"


# Initialisation de la conversation avec un message système
conversation = [
    {"role": "system", "content": "Tu es un assistant qui aide les gens."}
]

while True:
    # Demander à l'utilisateur de saisir une question
    user_input = input("Tape ta question ('exit' pour sortir) : ")
    if user_input == "exit":
        break

    # Ajouter le message de l'utilisateur à la conversation
    conversation.append({"role": "user", "content": user_input})

    # Envoyer une requête à l'API de GPT pour un modèle de chat
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    # Ajouter la réponse générée par l'assistant à la conversation
    assistant_reply = response.choices[0].message["content"]
    conversation.append({"role": "assistant", "content": assistant_reply})

    # Afficher la réponse de l'assistant
    print(assistant_reply)
