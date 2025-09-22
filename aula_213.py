class Caneta:

    _cores_validas = {'azul', 'vermelha', 'dourada'}

    def __init__(self, cor, acionamento_por_botão=False):
        self.cor_tinta = cor
        self._acionamento_por_botao = acionamento_por_botão

#cor

    @property
    def cor(self):
        print("executa uma tarefa: validação, log, etc")
        return self.cor_tinta

    @cor.setter
    def cor(self, cor):
        if cor not in self._cores_validas:
            raise ValueError("não fabricamos!")
        self.cor_tinta = cor

# tampada

    @property
    def acionamento_por_botao(self):
        return self._acionamento_por_botao
    
    @acionamento_por_botao.setter
    def acionamento_por_botao(self, acionamento_por_botao):
        if cor == 'vermelha':
            raise ValueError("Caneta vermelha só com acionamento por botao!")
        else:
            self._acionamento_por_botao = False
    
caneta = Caneta('azul')

print(caneta.cor)
caneta.cor ='vermelha'
print(caneta.cor)
caneta.cor = 'verde'
print(caneta.cor)
print()
caneta.acionamento_por_botao = 'verde'
print(caneta.acionamento_por_botao)
