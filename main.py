from usuario import UsuarioEmagrecimento, UsuarioGanhoMassa, UsuarioManutencao
from dieta import Dieta
from alimento import Alimento


def criar_usuario():
    print("=== Cadastro de Usuário ===")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (cm): "))
    sexo = input("Sexo (M/F): ").upper()
    nivel_atividade = input("Nível (sedentario/leve/moderado/ativo/muito_ativo): ").lower()

    print("Objetivo:")
    print("1 - Emagrecimento")
    print("2 - Ganho de massa")
    print("3 - Manutenção")

    opcao = input("Escolha: ")

    if opcao == "1":
        return UsuarioEmagrecimento(nome, idade, peso, altura, sexo, nivel_atividade)
    elif opcao == "2":
        return UsuarioGanhoMassa(nome, idade, peso, altura, sexo, nivel_atividade)
    else:
        return UsuarioManutencao(nome, idade, peso, altura, sexo, nivel_atividade)


def criar_alimento():
    print("\n=== Novo Alimento ===")

    nome = input("Nome: ")
    quantidade = float(input("Quantidade (g): "))
    calorias = float(input("Calorias por 100g: "))
    proteina = float(input("Proteína por 100g: "))
    carbo = float(input("Carboidrato por 100g: "))
    gordura = float(input("Gordura por 100g: "))

    return Alimento(nome, quantidade, calorias, proteina, carbo, gordura)


def exibir_consumo(dieta):
    totais = dieta.calcular_totais()

    print("\n=== Consumo do Dia ===")
    print(f"Calorias: {totais['calorias']:.2f}")
    print(f"Proteína: {totais['proteina']:.2f}")
    print(f"Carboidrato: {totais['carboidrato']:.2f}")
    print(f"Gordura: {totais['gordura']:.2f}")


def main():
    usuario = criar_usuario()
    dieta = Dieta(usuario)
    dieta.carregar_json()

    while True:
        print("\n=== MENU ===")
        print("1 - Adicionar alimento")
        print("2 - Ver consumo do dia")
        print("3 - Comparar com objetivo")
        print("4 - Salvar dia")
        print("5 - Ver histórico")
        print("6 - Salvar em arquivo")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            alimento = criar_alimento()
            dieta.adicionar_alimento(alimento)

        elif opcao == "2":
            exibir_consumo(dieta)

        elif opcao == "3":
            dieta.comparar_objetivos()

        elif opcao == "4":
            dieta.salvar_dia()

        elif opcao == "5":
            dieta.exibir_historico()

        elif opcao == "6":
            dieta.salvar_json()

        elif opcao == "0":
            dieta.salvar_json()
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()