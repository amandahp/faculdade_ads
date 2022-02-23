# 1) Criar metodo aplica-desconto

class TV:                                                   #classe # noqa
    def __init__(self, tela, resolucao, fabricante, preco): #funcao # noqa
        self.tela = tela
        self.resolucao = resolucao
        self.fabricante = fabricante
        self.preco = preco
        self.fotos = []
        self.descricao = f'TV {resolucao} {tela}"  - {fabricante}'

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco

    def editar_fotos(self):
        pass

    def editar_descricao(self):
        pass

    def aplicar_desconto(self, desconto):
        porcentagem = desconto/100
        novo_valor = self.preco - (porcentagem * self.preco)
        self.preco = novo_valor
        return self.preco


tv_1 = TV(43, "FullHD", 'Samsung', 2400)
tv_2 = TV(50, "4K", "LG", 3200)

print("fim")


print(f'Preço antigo: R$ {tv_1.preco:.2f}')
tv_1.atualizar_preco(2160)
print(f'Preço novo: R$ {tv_1.preco:.2f}')


print(f'Preço antigo: R$ {tv_1.preco:.2f}')
tv_1.aplicar_desconto(10)
print(f'Preço novo: R$ {tv_1.preco:.2f}')