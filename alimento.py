class Alimento:
    def __init__(self, nome, quantidade_gramas, calorias_por_100g, proteina, carboidrato, gordura):
        self._nome = nome
        self._quantidade_gramas = quantidade_gramas
        self._calorias_por_100g = calorias_por_100g
        self._proteina = proteina
        self._carboidrato = carboidrato
        self._gordura = gordura

    @property
    def nome(self):
        return self._nome

    @property
    def quantidade_gramas(self):
        return self._quantidade_gramas

    @quantidade_gramas.setter
    def quantidade_gramas(self, valor):
        if valor <= 0:
            raise ValueError("Quantidade inválida")
        self._quantidade_gramas = valor

    @property
    def calorias_por_100g(self):
        return self._calorias_por_100g

    @property
    def proteina(self):
        return self._proteina

    @property
    def carboidrato(self):
        return self._carboidrato

    @property
    def gordura(self):
        return self._gordura

    def fator(self):
        return self._quantidade_gramas / 100

    def calorias_totais(self):
        return self.fator() * self._calorias_por_100g

    def proteina_total(self):
        return self.fator() * self._proteina

    def carboidrato_total(self):
        return self.fator() * self._carboidrato

    def gordura_total(self):
        return self.fator() * self._gordura

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nome": self._nome,
            "quantidade_gramas": self._quantidade_gramas,
            "calorias_por_100g": self._calorias_por_100g,
            "proteina": self._proteina,
            "carboidrato": self._carboidrato,
            "gordura": self._gordura
        }

    def __str__(self):
        return f"{self._nome} ({self._quantidade_gramas}g)"


 