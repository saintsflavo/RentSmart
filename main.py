from imovel import Imovel
from cliente import Cliente
from orcamento import Orcamento


def ler_inteiro(mensagem, minimo, maximo=None):

    while True:
        try:
            valor = int(input(mensagem))

            if valor < minimo:
                print(f"Digite um número maior ou igual a {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"Digite um número menor ou igual a {maximo}.")
                continue

            return valor

        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


print("===== RENTSMART =====")

# dados do cliente
nome = input("Digite seu nome: ").strip()

while not nome:
    print("O nome não pode ficar vazio!")
    nome = input("Digite seu nome: ").strip()

criancas = input("Possui crianças? (s/n): ").lower().strip()

while criancas not in ["s", "n"]:
    print("Opção inválida!")
    criancas = input("Possui crianças? (s/n): ").lower().strip()

cliente = Cliente(nome, criancas == "s")

# escolha do imóvel
print("\nEscolha o tipo de imóvel:")
print("1 - Apartamento")
print("2 - Casa")
print("3 - Estúdio")

opcao = ler_inteiro("Digite sua opção: ", 1, 3)

if opcao == 1:
    tipo = "Apartamento"
    quartos = 1
    aluguel_base = 700

elif opcao == 2:
    tipo = "Casa"
    quartos = 1
    aluguel_base = 900

else:
    tipo = "Estúdio"
    quartos = 0
    aluguel_base = 1200

# quantidade de quartos
if tipo != "Estúdio":
    quartos = ler_inteiro(
        "Quantidade de quartos (1 ou 2): ", 1, 2
    )

# quantidade de vagas
if tipo in ["Apartamento", "Casa"]:
    vagas = ler_inteiro(
        "Quantidade de vagas (0 ou 1): ", 0, 1
    )

else:
    print("\nEstúdios possuem pacote inicial de 2 vagas.")
    vagas = ler_inteiro(
        "Quantidade de vagas (0 ou a partir de 2): ", 0
    )

    while vagas == 1:
        print("Estúdios permitem 0 ou pelo menos 2 vagas.")
        vagas = ler_inteiro(
            "Quantidade de vagas: ", 0
        )

imovel = Imovel(tipo, quartos, aluguel_base, vagas)

# parcelamento
parcelas = ler_inteiro(
    "\nEm quantas vezes deseja parcelar a taxa? (1 a 5): ", 1, 5
)

# orçamento
orcamento = Orcamento(cliente, imovel, parcelas)

# resultado
detalhes = imovel.detalhar_aluguel(cliente.possui_criancas)

print("\n===== ORÇAMENTO RENTSMART =====")
print("Cliente:", cliente.nome)
print("Imóvel:", imovel.tipo)
print("Quartos:", imovel.quartos)
print("Vagas:", imovel.vagas)

print("\n--- DETALHAMENTO DO ALUGUEL ---")
print(f"Aluguel-base: R$ {detalhes['aluguel_base']:.2f}")
print(f"Adicional de quartos: R$ {detalhes['adicional_quartos']:.2f}")
print(f"Adicional de garagem: R$ {detalhes['adicional_garagem']:.2f}")
print(f"Desconto: R$ {detalhes['desconto']:.2f}")
print(f"\nALUGUEL MENSAL: R$ {detalhes['total']:.2f}")

print("\n--- TAXA CONTRATUAL ---")
print(f"Taxa total: R$ {orcamento.taxa_contrato:.2f}")
parcelas_contrato = orcamento.calcular_parcelas_contrato()

print("Parcelamento:")

for numero, valor in enumerate(parcelas_contrato, start=1):
    print(f"{numero}ª parcela: R$ {valor:.2f}")

orcamento.gerar_csv()
