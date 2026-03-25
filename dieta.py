import json
from datetime import datetime
print("Dieta carregada versão NOVA")

class Dieta:
    def __init__(self, usuario):
        self._usuario = usuario
        self._objetivo_calorias = usuario.calorias_objetivo()
        self._objetivo_proteina = usuario.peso * 2
        self._objetivo_carboidrato = usuario.peso * 3
        self._objetivo_gordura = usuario.peso * 0.8
        self._consumo = []
        self._historico = []

    @property
    def usuario(self):
        return self._usuario

    def adicionar_alimento(self, alimento):
        self._consumo.append(alimento)

    def calcular_totais(self):
        return {
            "calorias": sum(a.calorias_totais() for a in self._consumo),
            "proteina": sum(a.proteina_total() for a in self._consumo),
            "carboidrato": sum(a.carboidrato_total() for a in self._consumo),
            "gordura": sum(a.gordura_total() for a in self._consumo)
        }

    def comparar_objetivos(self):
        totais = self.calcular_totais()

        print("\n--- Comparação com Objetivos ---")
        print(f"Calorias: {totais['calorias']:.2f} / {self._objetivo_calorias:.2f}")
        print(f"Proteína: {totais['proteina']:.2f} / {self._objetivo_proteina:.2f}")
        print(f"Carboidrato: {totais['carboidrato']:.2f} / {self._objetivo_carboidrato:.2f}")
        print(f"Gordura: {totais['gordura']:.2f} / {self._objetivo_gordura:.2f}")

    def salvar_dia(self):
        registro = {
            "data": datetime.now().strftime("%d/%m/%Y"),
            "usuario": self._usuario.nome,
            "consumo": [a.to_dict() for a in self._consumo]
        }
        self._historico.append(registro)
        self._consumo.clear()

    def exibir_historico(self):
        for registro in self._historico:
            print(f"\nData: {registro['data']} | Usuario: {registro['usuario']}")
            for alimento in registro["consumo"]:
                print(f"- {alimento['nome']} ({alimento['quantidade_gramas']}g)")

    def salvar_json(self, caminho="historico.json"):
        with open(caminho, "w") as f:
            json.dump(self._historico, f, indent=4)

    def carregar_json(self, caminho="historico.json"):
        try:
            with open(caminho, "r") as f:
                self._historico = json.load(f)
        except FileNotFoundError:
            self._historico = []