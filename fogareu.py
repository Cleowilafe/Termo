import pyromat as pm

# Configura unidades
pm.config['unit_pressure'] = 'bar'
pm.config['unit_temperature'] = 'K'
pm.config['unit_energy'] = 'kJ'
pm.config['unit_mass'] = 'kg'

def main():
    while True:
        print("\nEscolha a substância:")
        print("(1) Água")
        print("(2) Amônia")
        print("(0) Sair")
        r1 = input("Opção: ")

        if r1 == "0":
            break
        elif r1 == "1":
            substancia = pm.get('mp.H2O')
        elif r1 == "2":
            substancia = pm.get('mp.NH3')
        else:
            print("Opção inválida.")
            continue

        # Menu de entrada
        print("\nEscolha as DUAS propriedades conhecidas:")
        print("(1) Temperatura (T em °C)")
        print("(2) Pressão (p em kPa)")
        print("(3) Entalpia (h em kJ/kg)")
        print("(4) Entropia (s em kJ/kg·K)")

        entradas = []
        while len(entradas) < 2:
            prop = input(f"Digite o número da propriedade {len(entradas)+1}: ")
            if prop in ["1", "2", "3", "4"] and prop not in entradas:
                entradas.append(prop)
            else:
                print("Entrada inválida ou repetida. Tente novamente.")

        estado = {}

        for e in entradas:
            if e == "1":
                T_C = float(input("Digite a temperatura (°C): "))
                estado["T"] = T_C + 273.15
            elif e == "2":
                p_kPa = float(input("Digite a pressão (kPa): "))
                estado["p"] = p_kPa / 100
            elif e == "3":
                h = float(input("Digite a entalpia (kJ/kg): "))
                estado["h"] = h
            elif e == "4":
                s = float(input("Digite a entropia (kJ/kg·K): "))
                estado["s"] = s

        print("\nEscolha a propriedade termodinâmica a ser calculada:")
        print("(1) Entalpia (h)")
        print("(2) Entropia (s)")
        print("(3) Energia interna (u)")
        print("(4) Temperatura (T)")
        print("(5) Pressão (p)")
        prop_calc = input("Opção: ")

        try:
            if prop_calc == "1":
                resultado = substancia.h(**estado)
                print(f"Entalpia: {resultado[0]:.2f} kJ/kg")
            elif prop_calc == "2":
                resultado = substancia.s(**estado)
                print(f"Entropia: {resultado[0]:.4f} kJ/kg·K")
            elif prop_calc == "3":
                resultado = substancia.u(**estado)
                print(f"Energia interna: {resultado[0]:.2f} kJ/kg")
            elif prop_calc == "4":
                resultado = substancia.T(**estado)
                print(f"Temperatura: {resultado[0] - 273.15:.2f} °C")
            elif prop_calc == "5":
                resultado = substancia.p(**estado)
                print(f"Pressão: {resultado[0] * 100:.2f} kPa")
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro ao calcular a propriedade:", e)

if __name__ == "__main__":
    main()
