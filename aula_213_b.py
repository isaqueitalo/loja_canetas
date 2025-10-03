class Caneta:

    _cores_precos = {
        "azul": 15.0,
        "vermelha": 18.0,
        "dourada": 25.0
    }


    def __init__(self, cor: str, acionamento_por_botao: bool = False):
        self._cor = None
        self._acionamento_por_botao = acionamento_por_botao
        self.cor = cor

        @property
        def cor(self):
            return self._cor
        
        @cor.setter
        def cor(self, cor: str) -> None:
            if cor not in self._cores_precos:
                raise ValueError('cor não fabricada!')
            self._cor = cor

    # acionamento por botão

        @property
        def acionamento_por_botao(self):
            return self._acionamento_por_botao
        
        @acionamento_por_botao.setter
        def acionamento_por_botao(self, valor: bool) -> None:
            if self._cor == 'vermelha' and not valor:
                raise ValueError('caneta vermelha só pode ser acionada por botão!')
            self._acionamento_por_botao = valor

# preço

    @property
    def preco_por_caixa(self) -> float:
        return self._cores_precos[self._cor]

    # representação

    def __str__(self) -> str:
        return (f"Caneta(cor={self._cor}, "
                f"botão={'Sim' if self._acionamento_por_botao else 'Não'}, "
                f"preço_caixa=R$ {self.preco_por_caixa:.2f})")


def mostrar_menu_cores():
    print('opções disponíveis (preço por caixa):')
    for numero, cor in enumerate(Caneta._cores_precos.keys(), start=1):
        preco = Caneta._cores_precos[cor]
        regra = 'somente com botão' if cor == 'vermelha' else 'com ou sem botão'
        print(f'{numero}, {cor} - R${preco:.2f} - {regra}')

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

# carrinho de compras
print('=== 🖊️ Loja de Canetas ===\n')

def mostrar_menu_cores():
    print("Opções disponíveis (preço por caixa):")
    for numero, (cor, preco) in enumerate(Caneta._cores_precos.items(), start=1):
        regra = "⚠️ somente COM botão" if cor == "vermelha" else "com ou sem botão"
        print(f"{numero} - {cor.capitalize()} (R$ {preco:.2f}, {regra})")


carrinho = []
total = 0.0

while True:
# escolher cor
    while True:
        try:
            mostrar_menu_cores()
            cores_disponiveis = list(Caneta._cores_precos.keys())
            escolha = int(input('digite o numero da cor desejada: '))
            if escolha < 1 or escolha > len(cores_disponiveis):
                print('opção inválida!')
                continue
            cor_escolhida = cores_disponiveis[escolha - 1]
            break
        except ValueError as e:
            print(f'erro: {e} digite novamente.\n')

    # escolher acionamento
    while True:
        try:
            acionamento = input('digite "s" para acionamento por botão ou "n" para acionamento por pressão: ')
            if acionamento not in ['s', 'n']:
                raise ValueError('opção inválida!')
                continue
            acionamento_por_botao = acionamento =='s'
            break
        except ValueError as e:
            print(f'erro: {e} digite novamente.\n')
    
    # escolher quantidade
    while True:
        try:
            quantidade = int(input('digite a quantidade de caixas desejadas: '))
            if quantidade <= 0:
                raise ValueError('quantidade deve ser maior que zero!')
                continue
            break
        except ValueError as e:
            print(f'erro: {e} digite novamente\n')

    # criar caneta e adicionar ao carrinho
    while True:
        try:
            caneta = Caneta(cor_escolhida, acionamento_por_botao)
            carrinho.append((caneta, quantidade))
            subtotal = caneta._cores_precos[cor_escolhida] * quantidade
            total += subtotal
            print(f'\n{quantidade} caixas de {caneta._cor} adicionadas ao carrinho')
        except ValueError as e:
            print(f'erro: {e} digite novamente.\n')
            continue

    # continuar comprando?
        while True:
            try:
                continuar = input('deseja continuar comprando?')
                print('1 - sim')
                print('2 - não')
                if continuar not in ['1', '2']:
                    raise ValueError('opção inválida!')
                    continue
                break
            except ValueError as e:
                print(f'erro: {e} digite novamente.\n')
        if continuar == '2':
            break
        print('')

    # frete ou retirada
    while True:
        try:
            print('opções de frete:')
            print('1 - Retirar na loja (grátis)')
            print('2 - Entrega com frete')
            escolha_frete = int(input('digite a opção: '))
            if escolha_frete == 1:
                print('você escolheu retirar na loja. sem custo de frete.')
                break
            elif escolha_frete == 2:
                print('opções de entrega:')
                for i, (regiao, dados) in enumerate(_fretes.items(), start=1):
                    print(f'{i}, {regiao} - R$({dados["base"]}) + R$({dados["extra_por_caixa"]}) por caixa extra')

                escolha_regiao = int(input('digite a região de entrega: '))
                if escolha_regiao < 1 or escolha_regiao > len(_fretes):
                    raise ValueError('opção inválida!')
                    continue

                regiao_escolhida = list(_fretes.keys())[escolha_regiao - 1]
                frete = _fretes[regiao_escolhida]
                print(f'você escolheu entrega para {regiao_escolhida}. custo do frete: R${frete:.2f}')
                break
            else:
                print('opção inválida! tente novamente.\n')
        except ValueError as e:
            print(f'erro: {e} digite novamente.\n')

# resumo final

        print('\nResumo da compra:')
        if not carrinho:
            print('carrinho vazio. nada foi comprado.')
        else:
            for item, quantidade in carrinho:
                preco_unitario = item._cores_precos[item.cor]
                subtotal = preco_unitario * quantidade
                print(f'{quantidade} caixas de caneta {item.cor} ({"botão" if item.acionamento_por_botao else "pressão"}) - R${preco_unitario:.2f} cada - Subtotal: R${subtotal:.2f}')
                total += subtotal
           
    while True:
        try:
            print('opções de frete:')
            print('1 - Retirar na loja (grátis)')
            print('2 - Entrega com frete')
            escolha_frete = int(input('digite a opção: '))
            if escolha_frete == 1:
                print('você escolheu retirar na loja. sem custo de frete.')
                break
            
            elif escolha_frete == 2:
                print('opções de entrega:')
                for i, (regiao, dados) in enumerate(_fretes.items(), start=1):
                    print(f'{i}, {regiao} - R$({dados["base"]}) + R$({dados["extra_por_caixa"]}) por caixa extra')

                escolha_regiao = int(input('digite a região de entrega: '))
                if escolha_regiao < 1 or escolha_regiao > len(_fretes):
                    raise ValueError('opção inválida!')
                    continue
                
                regiao_escolhida = list(_fretes.keys())[escolha_regiao - 1]
                frete = _fretes[regiao_escolhida]
                print(f'você escolheu entrega para {regiao_escolhida}. custo do frete: R${frete:.2f}')
                break
            else:
                print('opção inválida! tente novamente.\n')
        except ValueError as e:
            print(f'erro: {e} digite novamente.\n')
        
# resumo final

    print('\nResumo da compra:')
    if not carrinho:
        print('carrinho vazio. nada foi comprado.')
    else:
        for item, quantidade in carrinho:
            preco_unitario = item._cores_precos[item.cor]
            subtotal = preco_unitario * quantidade
            print(f'{quantidade} caixas de caneta {item.cor} ({"botão" if item.acionamento_por_botao else "pressão"}) - R${preco_unitario:.2f} cada - Subtotal: R${subtotal:.2f}')
            total += subtotal