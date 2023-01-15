import openai

# Configurer une clé d'API valide
openai.api_key = "tacleapi-xxxxxXXXX1111222abc"


# Demander à l'utilisateur de saisir une recherche
prompt = input("Tape ta question : ")

# Envoyer une requête à l'API de GPT
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
)

# Afficher la réponse
print(response)

print(response["choices"][0]["text"])
