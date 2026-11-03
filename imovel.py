class Imovel:

    def __init__(self, tipo, quartos, aluguel_base, vagas=0):

        if vagas < 0:
            raise ValueError("A quantidade de vagas não pode ser negativa.")

        if tipo in ["Apartamento", "Casa"] and vagas > 1:
            raise ValueError("Casas e apartamentos permitem até uma vaga.")

        if tipo == "Estúdio" and vagas == 1:
            raise ValueError("Estúdios possuem pacote inicial de 2 vagas.")

        self.tipo = tipo
        self.quartos = quartos
        self.aluguel_base = aluguel_base
        self.vagas = vagas

    def detalhar_aluguel(self, possui_criancas=True):

        adicional_quartos = 0
        adicional_garagem = 0
        desconto = 0

        if self.tipo == "Apartamento" and self.quartos == 2:
            adicional_quartos = 200

        elif self.tipo == "Casa" and self.quartos == 2:
            adicional_quartos = 250

        if self.tipo in ["Apartamento", "Casa"] and self.vagas == 1:
            adicional_garagem = 300

        elif self.tipo == "Estúdio" and self.vagas >= 2:
            adicional_garagem = 250 + (self.vagas - 2) * 60

        subtotal = (
            self.aluguel_base
            + adicional_quartos
            + adicional_garagem
        )

        if self.tipo == "Apartamento" and not possui_criancas:
            desconto = subtotal * 0.05

        total = subtotal - desconto

        return {
            "aluguel_base": self.aluguel_base,
            "adicional_quartos": adicional_quartos,
            "adicional_garagem": adicional_garagem,
            "desconto": desconto,
            "total": total
        }

    def calcular_aluguel(self, possui_criancas=True):
        return self.detalhar_aluguel(possui_criancas)["total"]