import os
import csv

class Orcamento:

    def __init__(self, cliente, imovel, parcelas_contrato):

        if parcelas_contrato < 1 or parcelas_contrato > 5:
            raise ValueError("O parcelamento deve ser de 1 a 5 vezes.")

        self.cliente = cliente
        self.imovel = imovel
        self.parcelas_contrato = parcelas_contrato
        self.taxa_contrato = 2000

    def calcular_aluguel(self):
        return self.imovel.calcular_aluguel(
            self.cliente.possui_criancas
        )

    def calcular_parcelas_contrato(self):

        total_centavos = 200000
        valor_base, resto = divmod(
            total_centavos,
            self.parcelas_contrato
        )

        parcelas = []

        for i in range(self.parcelas_contrato):
            valor = valor_base

            if i >= self.parcelas_contrato - resto:
                valor += 1

            parcelas.append(valor / 100)

        return parcelas


    def gerar_csv(self):

        aluguel = self.calcular_aluguel()
        parcelas = self.calcular_parcelas_contrato()

        os.makedirs("relatorios", exist_ok=True)

        with open(
            "relatorios/projecao_12_meses.csv",
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as arquivo:

            escritor = csv.writer(arquivo, delimiter=";")

            escritor.writerow([
                "Mes",
                "Aluguel",
                "Taxa Contratual",
                "Total Mensal"
            ])

            for mes in range(1, 13):

                if mes <= self.parcelas_contrato:
                    taxa = parcelas[mes - 1]
                else:
                    taxa = 0

                total = aluguel + taxa

                escritor.writerow([
                    mes,
                    f"{aluguel:.2f}",
                    f"{taxa:.2f}",
                    f"{total:.2f}"
                ])

        print("\nArquivo CSV gerado com sucesso!")