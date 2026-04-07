# =========================
# MINI COMERCE - SISTEMA
# =========================

# -------- FRETE --------
def calcular_frete(cep):
    if cep == "":
        return "CEP obrigatório"

    if not cep.isdigit():
        return "CEP inválido"

    if len(cep) != 8:
        return "Formato inválido"

    if cep.startswith("00"):
        return "Não entregamos fora do país"

    return 20


# -------- PARCELAMENTO --------
def pode_parcelar(valor):
    if valor < 0:
        return "Valor inválido"

    if valor >= 100:
        return True

    return False


# -------- PEDIDO --------
def criar_pedido(status_pagamento, pedido_existente=False):
    if pedido_existente:
        return "Pedido duplicado"

    if status_pagamento == "aprovado":
        return "Pedido criado"

    return "Pedido não criado"


# -------- GATEWAY --------
def processar_pagamento(status_gateway):
    if status_gateway == "ok":
        return "Pagamento processado"

    if status_gateway == "indisponivel":
        return "Falha de comunicação"

    if status_gateway == "timeout":
        return "Falha"

    return "Erro"


# -------- CARRINHO --------
class Carrinho:
    def __init__(self):
        self.itens = {}

    def adicionar(self, produto, quantidade):
        if quantidade <= 0:
            return "Quantidade inválida"
        self.itens[produto] = quantidade

    def remover_todos(self):
        self.itens = {}

    def esta_vazio(self):
        return len(self.itens) == 0


# =========================
# TESTES (CENÁRIOS BDD)
# =========================

def rodar_testes():
    print("=== TESTES FRETE ===")
    print(calcular_frete("77000000") == 20)  # válido
    print(calcular_frete("abc") == "CEP inválido")
    print(calcular_frete("00123456") == "Não entregamos fora do país")
    print(calcular_frete("") == "CEP obrigatório")
    print(calcular_frete("123") == "Formato inválido")
    print(calcular_frete("77000001") == 20)  # recalcular

    print("\n=== TESTES PARCELAMENTO ===")
    print(pode_parcelar(150) is True)
    print(pode_parcelar(80) is False)
    print(pode_parcelar(100) is True)
    print(pode_parcelar(0) is False)
    print(pode_parcelar(-10) == "Valor inválido")
    print(pode_parcelar(120) is True)

    print("\n=== TESTES PEDIDO ===")
    print(criar_pedido("aprovado") == "Pedido criado")
    print(criar_pedido("recusado") == "Pedido não criado")
    print(criar_pedido("pendente") == "Pedido não criado")
    print(criar_pedido("erro") == "Pedido não criado")
    print(criar_pedido("aprovado", True) == "Pedido duplicado")
    print(criar_pedido("aprovado") == "Pedido criado")

    print("\n=== TESTES GATEWAY ===")
    print(processar_pagamento("ok") == "Pagamento processado")
    print(processar_pagamento("indisponivel") == "Falha de comunicação")
    print(processar_pagamento("timeout") == "Falha")
    print(processar_pagamento("erro") == "Erro")
    print(processar_pagamento("ok") == "Pagamento processado")
    print(processar_pagamento("timeout") == "Falha")

    print("\n=== TESTES CARRINHO ===")
    c = Carrinho()

    print(c.esta_vazio() == True)  # vazio

    c.adicionar("produto", 1)
    print(c.esta_vazio() == False)  # com item

    c.remover_todos()
    print(c.esta_vazio() == True)  # removido

    c.adicionar("produto", 2)
    print("produto" in c.itens)

    print(c.adicionar("produto", -1) == "Quantidade inválida")

    c.adicionar("produto", 5)
    print(c.itens["produto"] == 5)


# =========================
# EXECUÇÃO
# =========================

rodar_testes()