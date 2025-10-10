from datetime import datetime

# =====================
# Cliente
# =====================
class Cliente:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.nome} ({self.email})"


# =====================
# Produto: Caneta
# =====================
class Caneta:
    _cores_precos = {
        "azul": 15.0,
        "vermelha": 18.0,
        "dourada": 25.0
    }

    _estoque = {
        "azul": 50,
        "vermelha": 30,
        "dourada": 20
    }

    def __init__(self, cor: str, acionamento_por_botao: bool = False):
        self._cor = None
        self._acionamento_por_botao = acionamento_por_botao
        self.cor = cor

    @property
    def cor(self) -> str:
        return self._cor

    @cor.setter
    def cor(self, cor: str) -> None:
        if cor not in self._cores_precos:
            raise ValueError("Cor não fabricada!")
        self._cor = cor

    @property
    def acionamento_por_botao(self) -> bool:
        return self._acionamento_por_botao

    @acionamento_por_botao.setter
    def acionamento_por_botao(self, valor: bool) -> None:
        if self._cor == "vermelha" and not valor:
            raise ValueError("⚠️ Caneta vermelha só pode ser acionada por botão!")
        self._acionamento_por_botao = valor

    @property
    def preco_por_caixa(self) -> float:
        return self._cores_precos[self._cor]

    def __str__(self) -> str:
        return (f"{self._cor.capitalize()} "
                f"({'com botão' if self._acionamento_por_botao else 'sem botão'}) "
                f"→ R$ {self.preco_por_caixa:.2f}/caixa")


# =====================
# Configuração do frete
# =====================
_fretes = {
    "Recife (capital)": {"base": 15.0, "extra_por_caixa": 0.0},
    "Interior de PE": {"base": 25.0, "extra_por_caixa": 2.0},
    "Nordeste (outros estados)": {"base": 35.0, "extra_por_caixa": 3.0},
    "Sudeste": {"base": 50.0, "extra_por_caixa": 4.0},
    "Sul": {"base": 60.0, "extra_por_caixa": 5.0},
    "Centro-Oeste": {"base": 55.0, "extra_por_caixa": 4.0},
    "Norte": {"base": 70.0, "extra_por_caixa": 6.0}
}


# =====================
# Lista de clientes já cadastrados
# =====================
# =====================
# Lista de clientes já cadastrados
# =====================
clientes = [
    Cliente("Ana Silva", "ana@email.com"),
    Cliente("Carlos Souza", "carlos@email.com"),
    Cliente("Carla Dias", "carla@email.com"),
    Cliente("Mariana Lima", "mariana@email.com"),
]

print("=== Sistema de Clientes ===")
print("1 - Logar com cliente existente")
print("2 - Cadastrar novo cliente")
opcao = input("Escolha uma opção: ").strip()

if opcao == "1":

    # Login com autocomplete
    
    nome_busca = input("\nDigite o primeiro nome do cliente: ").strip().lower()
    clientes_filtrados = [c for c in clientes if c.nome.lower().startswith(nome_busca)]

    if not clientes_filtrados:
        print("❌ Nenhum cliente encontrado.")
        exit()

    elif len(clientes_filtrados) == 1:
        cliente_escolhido = clientes_filtrados[0]
        print(f"\n✅ Login realizado automaticamente: {cliente_escolhido.nome}\n")

    else:
        print("\nForam encontrados vários clientes:")
        for i, cliente in enumerate(clientes_filtrados, start=1):
            print(f"{i} - {cliente}")
        escolha = int(input("\nDigite o número do cliente para fazer login: "))
        cliente_escolhido = clientes_filtrados[escolha - 1]
        print(f"\n✅ Bem-vindo, {cliente_escolhido.nome}!\n")

elif opcao == "2":
    # Cadastro de novo cliente
    nome = input("Digite o nome completo do cliente: ").strip()
    email = input("Digite o e-mail do cliente: ").strip()
    novo_cliente = Cliente(nome, email)
    clientes.append(novo_cliente)
    cliente_escolhido = novo_cliente
    print(f"\n✅ Cliente {cliente_escolhido.nome} cadastrado e logado com sucesso!\n")

else:
    print("❌ Opção inválida. Encerrando o sistema.")
    exit()


# =====================
# Loja de Canetas
# =====================
print("=== 🖊️ Loja de Canetas ===\n")

carrinho = []
total = 0.0

def mostrar_menu_cores():
    print("Opções disponíveis (preço por caixa / estoque):")
    for numero, (cor, preco) in enumerate(Caneta._cores_precos.items(), start=1):
        estoque = Caneta._estoque[cor]
        regra = "⚠️ somente COM botão" if cor == "vermelha" else "com ou sem botão"
        print(f"{numero} - {cor.capitalize()} "
              f"(R$ {preco:.2f}, {regra}, estoque: {estoque} caixas)")


# =====================
# Compras
# =====================
while True:
    # escolher cor
    while True:
        try:
            mostrar_menu_cores()
            cores_disponiveis = list(Caneta._cores_precos.keys())
            escolha = int(input("Digite o número da cor desejada: "))
            if escolha < 1 or escolha > len(cores_disponiveis):
                print("❌ Opção inválida.\n")
                continue
            cor_escolhida = cores_disponiveis[escolha - 1]
            break
        except ValueError:
            print("❌ Digite um número válido.\n")

    # escolher acionamento
    while True:
        try:
            print("\nDeseja com acionamento por botão?")
            print("1 - Sim")
            print("2 - Não")
            opc = int(input("Digite a opção: "))
            if opc not in (1, 2):
                print("❌ Opção inválida.\n")
                continue
            botao = (opc == 1)
            if cor_escolhida == "vermelha" and not botao:
                print("❌ Caneta vermelha exige acionamento por botão.\n")
                continue
            break
        except ValueError:
            print("❌ Digite um número válido.\n")

    # quantidade
    while True:
        try:
            qtd = int(input("Digite a quantidade de caixas: "))
            if qtd <= 0:
                print("❌ Quantidade deve ser maior que zero.\n")
                continue
            if qtd > Caneta._estoque[cor_escolhida]:
                print(f"❌ Estoque insuficiente! Só restam {Caneta._estoque[cor_escolhida]} caixas.\n")
                continue
            break
        except ValueError:
            print("❌ Digite um número inteiro válido.\n")

    # adiciona ao carrinho
    item = Caneta(cor_escolhida, botao)
    subtotal = item.preco_por_caixa * qtd
    carrinho.append((item, qtd, subtotal))
    total += subtotal
    Caneta._estoque[cor_escolhida] -= qtd
    print(f"\n✅ {qtd} caixa(s) de {item} adicionada(s) ao carrinho!\n")

    # continuar?
    continuar = int(input("Deseja comprar outra caneta? (1 - Sim, 2 - Finalizar): "))
    if continuar == 2:
        break
    print("")


# =====================
# Frete
# =====================
frete = 0.0
print("\nOpções de entrega:")
print("1 - Retirada na loja (sem custo)")
print("2 - Entrega com frete")
opc_entrega = int(input("Digite a opção: "))

if opc_entrega == 2:
    print("\nEscolha a região de entrega:")
    for i, (regiao, dados) in enumerate(_fretes.items(), start=1):
        print(f"{i} - {regiao} (R$ {dados['base']:.2f} + {dados['extra_por_caixa']:.2f}/caixa)")

    escolha_regiao = int(input("Digite a opção: "))
    regiao_escolhida = list(_fretes.keys())[escolha_regiao - 1]
    dados_frete = _fretes[regiao_escolhida]

    total_caixas = sum(qtd for _, qtd, _ in carrinho)
    frete = dados_frete["base"] + (dados_frete["extra_por_caixa"] * total_caixas)
    print(f"📦 Entrega para {regiao_escolhida}: R$ {frete:.2f}")


# =====================
# Descontos
# =====================
desconto = 0.0
if total > 200:
    desconto += 0.1
cupom = input("\nDigite um cupom de desconto (ou Enter): ").strip().upper()
if cupom == "DESCONTO10":
    desconto += 0.1
valor_desconto = total * desconto
total -= valor_desconto


# =====================
# Pagamento
# =====================
print("\nFormas de pagamento:")
print("1 - PIX (5% de desconto extra)")
print("2 - Cartão de crédito")
print("3 - Boleto bancário")
pagamento = int(input("Escolha a forma de pagamento: "))
parcelas = 1

if pagamento == 1:
    desconto_pix = total * 0.05
    total -= desconto_pix
    print(f"💳 Pagamento via PIX: desconto de R$ {desconto_pix:.2f}")
elif pagamento == 2:
    parcelas = int(input("Digite o número de parcelas (1 a 6): "))
    if parcelas > 3:
        juros = total * 0.05
        total += juros
        print(f"⚠️ Parcelamento em {parcelas}x terá juros de 5% (+R$ {juros:.2f})")
elif pagamento == 3:
    print("📄 Pagamento no boleto escolhido.")


# =====================
# Resumo final
# =====================
print("\n=== 🛒 Resumo da Compra ===")
print(f"Cliente: {cliente_escolhido.nome} ({cliente_escolhido.email})\n")
for caneta, qtd, subtotal in carrinho:
    print(f"- {qtd} caixa(s) de {caneta} → R$ {subtotal:.2f}")
if valor_desconto > 0:
    print(f"\n🎉 Descontos aplicados: -R$ {valor_desconto:.2f}")
if frete > 0:
    print(f"📦 Frete: R$ {frete:.2f}")
print(f"\n💰 Total a pagar: R$ {total + frete:.2f}")
if pagamento == 2 and parcelas > 1:
    valor_parcela = (total + frete) / parcelas
    print(f"💳 Parcelado em {parcelas}x de R$ {valor_parcela:.2f}")


# =====================
# Recibo em TXT
# =====================
recibo = "recibo_compra.txt"
with open(recibo, "w", encoding="utf-8") as f:
    f.write("=== RECIBO DE COMPRA ===\n")
    f.write(f"Cliente: {cliente_escolhido.nome} ({cliente_escolhido.email})\n")
    f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
    for caneta, qtd, subtotal in carrinho:
        f.write(f"- {qtd} caixa(s) de {caneta} → R$ {subtotal:.2f}\n")
    if valor_desconto > 0:
        f.write(f"\n🎉 Descontos aplicados: -R$ {valor_desconto:.2f}\n")
    if frete > 0:
        f.write(f"📦 Frete: R$ {frete:.2f}\n")
    f.write(f"\n💰 Total a pagar: R$ {total + frete:.2f}\n")
    if pagamento == 2 and parcelas > 1:
        valor_parcela = (total + frete) / parcelas
        f.write(f"💳 Parcelado em {parcelas}x de R$ {valor_parcela:.2f}\n")
    f.write("\nObrigado pela sua compra!\n")

print(f"\n🧾 Recibo gerado: {recibo}")
