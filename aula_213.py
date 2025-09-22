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
            raise ValueError("Caneta vermelha só pode ser acionada por botão!")
        self._acionamento_por_botao = valor

    # ===== preço =====
    @property
    def preco_por_caixa(self) -> float:
        return self._cores_precos[self._cor]

    # ===== representação =====
    def __str__(self):
        return (f"Caneta(cor={self._cor}, "
                f"botão={'Sim' if self._acionamento_por_botao else 'Não'}, "
                f"preço_caixa=R$ {self.preco_por_caixa:.2f})")


# =====================
# Carrinho de Compras
# =====================
print("=== 🖊️ Loja de Canetas ===")
print("Confira nossas opções de canetas (preço por caixa):\n")

for cor, preco in Caneta._cores_precos.items():
    if cor == "vermelha":
        descricao = "⚠️ somente COM botão"
    else:
        descricao = "disponível com ou sem botão"
    print(f"- {cor.capitalize()} → R$ {preco:.2f} ({descricao})")

carrinho = []
total = 0.0

while True:
    try:
        cor = input("\nEscolha a cor da caneta desejada: ").strip().lower()

        botao_input = input("Você deseja com acionamento por botão? (s/n): ").strip().lower()
        botao = True if botao_input == "s" else False

        quantidade = int(input("Digite a quantidade de caixas: "))

        caneta = Caneta(cor, botao)
        subtotal = caneta.preco_por_caixa * quantidade

        carrinho.append((caneta, quantidade, subtotal))
        total += subtotal

        print(f"✅ {quantidade} caixa(s) de caneta {cor} adicionada(s) ao carrinho!")

        continuar = input("\nDeseja comprar outra caneta? (s/n): ").strip().lower()
        if continuar != "s":
            break

    except Exception as e:
        print("❌ Erro:", e)

# =====================
# Resumo final
# =====================
print("\n=== 🛒 Resumo da Compra ===")
for item in carrinho:
    caneta, qtd, subtotal = item
    print(f"- {qtd} caixa(s) de {caneta.cor} "
          f"({'com botão' if caneta.acionamento_por_botao else 'sem botão'}) "
          f"→ R$ {subtotal:.2f}")

print(f"\n💰 Total a pagar: R$ {total:.2f}")
