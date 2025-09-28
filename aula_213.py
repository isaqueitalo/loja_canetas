class Caneta:
    # Cores válidas e preços por caixa (em reais)
    _cores_precos = {
        "azul": 15.0,
        "vermelha": 18.0,
        "dourada": 25.0
    }

    def __init__(self, cor: str, acionamento_por_botao: bool = False):
        self._cor = None
        self._acionamento_por_botao = acionamento_por_botao
        self.cor = cor  # usa o setter para validar

    # ===== cor =====
    @property
    def cor(self) -> str:
        return self._cor

    @cor.setter
    def cor(self, cor: str) -> None:
        if cor not in self._cores_precos:
            raise ValueError("Cor não fabricada!")
        self._cor = cor

    # ===== acionamento_por_botao =====
    @property
    def acionamento_por_botao(self) -> bool:
        return self._acionamento_por_botao

    @acionamento_por_botao.setter
    def acionamento_por_botao(self, valor: bool) -> None:
        if self._cor == "vermelha" and not valor:
            raise ValueError("⚠️ Caneta vermelha só pode ser acionada por botão!")
        self._acionamento_por_botao = valor

    # ===== preço =====
    @property
    def preco_por_caixa(self) -> float:
        return self._cores_precos[self._cor]

    # ===== representação =====
    def __str__(self) -> str:
        return (f"Caneta(cor={self._cor}, "
                f"botão={'Sim' if self._acionamento_por_botao else 'Não'}, "
                f"preço_caixa=R$ {self.preco_por_caixa:.2f})")


# =====================
# Carrinho de Compras
# =====================
print("=== 🖊️ Loja de Canetas ===\n")

def mostrar_menu_cores():
    print("Opções disponíveis (preço por caixa):")
    for numero, (cor, preco) in enumerate(Caneta._cores_precos.items(), start=1):
        regra = "⚠️ somente COM botão" if cor == "vermelha" else "com ou sem botão"
        print(f"{numero} - {cor.capitalize()} (R$ {preco:.2f}, {regra})")

carrinho = []
total = 0.0

while True:
    # --- escolher cor ---
    while True:
        try:
            mostrar_menu_cores()
            cores_disponiveis = list(Caneta._cores_precos.keys())
            escolha = int(input("Digite o número da cor desejada: "))
            if escolha < 1 or escolha > len(cores_disponiveis):
                print("❌ Opção inválida. Tente novamente.\n")
                continue
            cor_escolhida = cores_disponiveis[escolha - 1]
            break
        except ValueError:
            print("❌ Digite um número válido.\n")

    # --- escolher acionamento ---
    while True:
        try:
            print("\nDeseja com acionamento por botão?")
            print("1 - Sim")
            print("2 - Não")
            opc = int(input("Digite a opção: "))
            if opc not in (1, 2):
                print("❌ Opção inválida. Tente novamente.\n")
                continue
            botao = (opc == 1)
            # regra da vermelha
            if cor_escolhida == "vermelha" and not botao:
                print("❌ Caneta vermelha exige acionamento por botão. Escolha 'Sim'.\n")
                continue
            break
        except ValueError:
            print("❌ Digite um número válido.\n")

    # --- quantidade ---
    while True:
        try:
            qtd = int(input("Digite a quantidade de caixas: "))
            if qtd <= 0:
                raise ValueError("❌ A quantidade deve ser maior que zero.\n")
            break
        except ValueError as e:
            print("❌ Digite um número inteiro válido.\n")

    # --- cria item e adiciona ao carrinho ---
    try:
        item = Caneta(cor_escolhida, botao)
        subtotal = item.preco_por_caixa * qtd
        carrinho.append((item, qtd, subtotal))
        total += subtotal
        print(f"\n✅ {qtd} caixa(s) de {item} adicionada(s) ao carrinho!\n")
    except Exception as e:
        print("❌ Erro ao adicionar item:", e)
        continue

    # --- continuar comprando? ---
    while True:
        try:
            print("Deseja comprar outra caneta?")
            print("1 - Sim")
            print("2 - Finalizar compra")
            continuar = int(input("Digite a opção: "))
            if continuar not in (1, 2):
                print("❌ Opção inválida. Tente novamente.\n")
                continue
            break
        except ValueError:
            print("❌ Digite um número válido.\n")

    if continuar == 2:
        break
    print("")  # linha em branco estética

# =====================
# Frete ou Retirada
# =====================
# =====================
# Frete ou Retirada
# =====================
frete = 0.0
_fretes = {
    "Recife (capital)": {"base": 15.0, "extra_por_caixa": 0.0},
    "Interior de PE": {"base": 25.0, "extra_por_caixa": 2.0},
    "Nordeste (outros estados)": {"base": 35.0, "extra_por_caixa": 3.0},
    "Sudeste": {"base": 50.0, "extra_por_caixa": 4.0},
    "Sul": {"base": 60.0, "extra_por_caixa": 5.0},
    "Centro-Oeste": {"base": 55.0, "extra_por_caixa": 4.0},
    "Norte": {"base": 70.0, "extra_por_caixa": 6.0}
}

while True:
    try:
        print("\nOpções de entrega:")
        print("1 - Retirada na loja (sem custo)")
        print("2 - Entrega com frete")
        opc_entrega = int(input("Digite a opção: "))

        if opc_entrega == 1:
            print("🚶 Retirada na loja escolhida.")
            break
        elif opc_entrega == 2:
            print("\nEscolha a região de entrega:")
            for i, (regiao, dados) in enumerate(_fretes.items(), start=1):
                print(f"{i} - {regiao} (R$ {dados['base']:.2f} + "
                      f"R$ {dados['extra_por_caixa']:.2f} por caixa extra)")

            escolha_regiao = int(input("Digite a opção: "))
            if escolha_regiao < 1 or escolha_regiao > len(_fretes):
                print("❌ Opção inválida. Tente novamente.\n")
                continue

            regiao_escolhida = list(_fretes.keys())[escolha_regiao - 1]
            dados_frete = _fretes[regiao_escolhida]

            # calcula frete total
            total_caixas = sum(qtd for _, qtd, _ in carrinho)
            frete = dados_frete["base"] + (dados_frete["extra_por_caixa"] * total_caixas)

            print(f"📦 Entrega para {regiao_escolhida} escolhida "
                  f"(R$ {frete:.2f} para {total_caixas} caixas).")
            break
        else:
            print("❌ Opção inválida. Tente novamente.\n")
    except ValueError:
        print("❌ Digite um número válido.\n")


# =====================
# Resumo final
# =====================
print("\n=== 🛒 Resumo da Compra ===")
if not carrinho:
    print("Nenhum item no carrinho.")
else:
    for caneta, qtd, subtotal in carrinho:
        print(f"- {qtd} caixa(s) de {caneta} → R$ {subtotal:.2f}")
    if frete > 0:
        print(f"\n📦 Frete: R$ {frete:.2f}")
    print(f"\n💰 Total a pagar: R$ {total + frete:.2f}")
