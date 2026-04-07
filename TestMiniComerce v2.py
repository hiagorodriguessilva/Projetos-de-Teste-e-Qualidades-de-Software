# =========================
# MINI COMERCE V2
# =========================

total_testes = 0
testes_ok = 0


def validar(teste):
    global total_testes, testes_ok
    total_testes += 1
    if teste:
        testes_ok += 1
        print("OK")
    else:
        print("FALHOU")


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
def criar_pedido(status, duplicado=False):
    if duplicado:
        return "Pedido duplicado"

    if status == "aprovado":
        return "Pedido criado"

    return "Pedido não criado"


# -------- GATEWAY --------
def gateway(status):
    if status == "ok":
        return "Pagamento processado"

    if status == "indisponivel":
        return "Falha de comunicação"

    if status == "timeout":
        return "Falha"

    return "Erro"


# -------- CARRINHO --------
class Carrinho:
    def __init__(self):
        self.itens = {}

    def adicionar(self, produto, qtd):
        if qtd <= 0:
            return "Quantidade inválida"
        self.itens[produto] = qtd

    def remover_todos(self):
        self.itens = {}

    def vazio(self):
        return len(self.itens) == 0


# =========================
# TESTES BDD
# =========================

def testes():

    print("\nFRETE")
    validar(calcular_frete("77000000") == 20)
    validar(calcular_frete("abc") == "CEP inválido")
    validar(calcular_frete("00123456") == "Não entregamos fora do país")
    validar(calcular_frete("") == "CEP obrigatório")
    validar(calcular_frete("123") == "Formato inválido")
    validar(calcular_frete("77000001") == 20)

    print("\nPARCELAMENTO")
    validar(pode_parcelar(150) is True)
    validar(pode_parcelar(80) is False)
    validar(pode_parcelar(100) is True)
    validar(pode_parcelar(0) is False)
    validar(pode_parcelar(-1) == "Valor inválido")
    validar(pode_parcelar(120) is True)

    print("\nPEDIDO")
    validar(criar_pedido("aprovado") == "Pedido criado")
    validar(criar_pedido("recusado") == "Pedido não criado")
    validar(criar_pedido("pendente") == "Pedido não criado")
    validar(criar_pedido("erro") == "Pedido não criado")
    validar(criar_pedido("aprovado", True) == "Pedido duplicado")
    validar(criar_pedido("aprovado") == "Pedido criado")

    print("\nGATEWAY")
    validar(gateway("ok") == "Pagamento processado")
    validar(gateway("indisponivel") == "Falha de comunicação")
    validar(gateway("timeout") == "Falha")
    validar(gateway("erro") == "Erro")
    validar(gateway("ok") == "Pagamento processado")
    validar(gateway("timeout") == "Falha")

    print("\nCARRINHO")
    c = Carrinho()
    validar(c.vazio() == True)

    c.adicionar("produto", 1)
    validar(c.vazio() == False)

    c.remover_todos()
    validar(c.vazio() == True)

    c.adicionar("produto", 2)
    validar("produto" in c.itens)

    validar(c.adicionar("produto", -1) == "Quantidade inválida")

    c.adicionar("produto", 5)
    validar(c.itens["produto"] == 5)


    print("\nCOBERTURA:")
    porcentagem = (testes_ok / total_testes) * 100
    print(f"{porcentagem:.2f}% dos testes passaram")


# EXECUÇÃO
testes()