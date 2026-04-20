perguntas = {
    "Quanto é 2 + 2?": "4",
    "Qual a capital do Brasil?": "brasilia",
    "Quanto é 5 * 2?": "10",
    "Qual o resultado de 10 / 2?": "5"
}

pontuacao = 0

print("Bem-vindo ao sistema de perguntas!")

for pergunta, resposta in perguntas.items():
    resposta_usuario = input(pergunta + " ").strip().lower()

    if resposta_usuario == resposta:
        print("Resposta correta!")
        pontuacao += 1
    else:
        print(f"Resposta incorreta! A resposta correta é: {resposta}")

print(f"\nSua pontuação final é: {pontuacao} de {len(perguntas)}")