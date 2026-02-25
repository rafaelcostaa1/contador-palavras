from contador import contar_palavras


def main():
    frase = input("Digite uma frase: ").strip()

    if not frase:
        print("Erro: Nenhuma frase foi digitada.")
        return

    resultado = contar_palavras(frase)

    if not resultado:
        print("Nenhuma palavra válida foi encontrada.")
        return

    print("\nContagem de palavras:")
    for palavra, quantidade in resultado.items():
        print(f"{palavra}: {quantidade}")


if __name__ == "__main__":
    main()
