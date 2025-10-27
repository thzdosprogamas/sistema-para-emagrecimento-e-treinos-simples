#essa parte simula o hub do usuario, onde ele pode escolher entre calcular o IMC ou receber recomendações de treino
#feito por M.W
#estrutura de importação de módulos e armazenamento de variáveis (retorno de função) implementada com apoio do ChatGPT para melhor organização do código.
print("Bem vindo ao sistema de recomendação de treinos!")
import sistema
usuario_nome = None
usuario_imc = None
while True:
    print('Escolha uma opção:')
    print('1 - Iniciar sistema (calcular IMC)')
    print('2 - Recomendar treino')
    print('3 - Sair')
    opcao = input('Digite sua opção: ')

    if opcao == '1':
        usuario_nome, usuario_imc = sistema.calcular_imc()  
    elif opcao == '2':
        if usuario_imc is None:
            print("Você precisa calcular o IMC primeiro.")
        else:
            recomendacao = sistema.recomendar_treino(usuario_imc)
            print(f"{usuario_nome}, seu treino recomendado é: {recomendacao}")
    elif opcao == '3':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida, tente novamente.')
