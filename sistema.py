def calcular_imc():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    peso_atual = float(input("Digite seu peso atual (em kg): "))
    altura = float(input("Digite sua altura (em metros): "))

    imc = peso_atual / (altura ** 2)
    print(f"Seu IMC é {imc:.2f}")
    return nome, imc

def recomendar_treino(imc):
    if imc < 18.5:
        return "Musculação para ganho de massa + dieta hipercalórica"
    elif imc < 25:
        return "Treino misto (musculação + cardio moderado)"
    elif imc < 30:
        return "Cardio moderado 40min + musculação leve"
    else:
        return "Caminhada leve + aeróbicos de baixo impacto"