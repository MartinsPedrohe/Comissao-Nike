def calcular_comissao(meta, vendas):
    atingimento = (vendas / meta) * 100
    comissao = 0

    if atingimento <= 79.99:
        comissao = 0
    elif atingimento <= 81.99:
        comissao = vendas * 0.0015
    elif atingimento <= 83.99:
        comissao = vendas * 0.0020
    elif atingimento <= 85.99:
        comissao = vendas * 0.0025
    elif atingimento <= 87.99:
        comissao = vendas * 0.0030
    elif atingimento <= 89.99:
        comissao = vendas * 0.0035
    elif atingimento <= 91.99:
        comissao = vendas * 0.0040
    elif atingimento <= 93.99:
        comissao = vendas * 0.0045
    elif atingimento <= 95.99:
        comissao = vendas * 0.0050
    elif atingimento <= 97.99:
        comissao = vendas * 0.0055
    elif atingimento <= 99.99:
        comissao = vendas * 0.0060
    elif atingimento <= 101.99:
        comissao = vendas * 0.0100
    elif atingimento <= 103.99:
        comissao = vendas * 0.0104
    elif atingimento <= 105.99:
        comissao = vendas * 0.0106
    elif atingimento <= 107.99:
        comissao = vendas * 0.0108
    elif atingimento <= 109.99:
        comissao = vendas * 0.0110
    elif atingimento <= 111.99:
        comissao = vendas * 0.0112
    elif atingimento <= 113.99:
        comissao = vendas * 0.0114
    elif atingimento <= 115.99:
        comissao = vendas * 0.0116
    elif atingimento <= 117.99:
        comissao = vendas * 0.0118
    elif atingimento <= 119.99:
        comissao = vendas * 0.0120
    elif atingimento <= 121.99:
        comissao = vendas * 0.0122
    elif atingimento <= 123.99:
        comissao = vendas * 0.0124
    elif atingimento <= 125.99:
        comissao = vendas * 0.0126
    elif atingimento <= 127.99:
        comissao = vendas * 0.0128
    elif atingimento <= 129.99:
        comissao = vendas * 0.0130
    elif atingimento <= 131.99:
        comissao = vendas * 0.0132
    elif atingimento <= 133.99:
        comissao = vendas * 0.0134
    elif atingimento <= 135.99:
        comissao = vendas * 0.0136
    elif atingimento <= 137.99:
        comissao = vendas * 0.0138
    else:
        comissao = vendas * 0.0140

    return atingimento, comissao

# Recebe a meta e os dias de trabalho
print("\n--- Simulador de Comissão ---")
meta = float(input("Digite a meta de vendas para todos os vendedores: R$ "))

# Loop para vários vendedores
while True:
    dias_planejados = int(input("Digite a quantidade de dias planejados para trabalhar: "))
    dias_trabalhados = int(input("Digite a quantidade de dias já trabalhados: "))
    vendas = float(input("\nDigite o valor vendido pelo vendedor: R$ "))
# Calcula metas diárias
    meta_diaria_original = meta / dias_planejados
    dias_restantes = dias_planejados - dias_trabalhados

    if dias_restantes > 0:
        meta_restante = meta - (meta_diaria_original * dias_trabalhados)
        meta_diaria_ajustada = meta_restante / dias_restantes
    else:
        meta_diaria_ajustada = 0


    if dias_restantes > 0:
        print(f"Meta diária ajustada para os próximos {dias_restantes} dias: R$ {meta_diaria_ajustada:.2f}")
    else:
        print("Todos os dias planejados já foram trabalhados.")


    atingimento, comissao = calcular_comissao(meta, vendas)

    print(f"Atingimento: {atingimento:.2f}%")
    print(f"Comissão: R$ {comissao:.2f}")

    continuar = input("\nDeseja simular para outro vendedor com a mesma meta? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando o simulador. Até a próxima!")
        break
