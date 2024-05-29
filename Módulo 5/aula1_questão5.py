import emoji

def apresentar_emojis_disponiveis():
    emojis_disponiveis = {
        ":red_heart:": "❤️",
        ":thumbs_up:": "👍",
        ":thinking_face:": "🤔",
        ":partying_face:": "🥳"
    }

    print("Emojis disponíveis:")
    for descricao, simbolo in emojis_disponiveis.items():
        print(f"{simbolo} - {descricao}")

def emojizar_frase():
    apresentar_emojis_disponiveis()
    frase_codificada = input("Digite uma frase e ela será emojizada:\n")
    frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)
    print(f"Frase emojizada:\n{frase_emojizada}")
emojizar_frase()

