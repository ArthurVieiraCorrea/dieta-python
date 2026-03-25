from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nome, idade, peso, altura, sexo, nivel_atividade):
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura
        self._sexo = sexo.upper()
        self._nivel_atividade = nivel_atividade.lower()

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        if valor <= 0:
            raise ValueError("Peso inválido")
        self._peso = valor

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError("Altura inválida")
        self._altura = valor

    @property
    def sexo(self):
        return self._sexo

    @property
    def nivel_atividade(self):
        return self._nivel_atividade

    def calculo_basal(self):
        if self._sexo == "M":
            return 10 * self._peso + 6.25 * self._altura - 5 * self._idade + 5
        return 10 * self._peso + 6.25 * self._altura - 5 * self._idade - 161

    def calculo_gasto_energetico_total(self):
        fatores = {
            "sedentario": 1.2,
            "leve": 1.375,
            "moderado": 1.55,
            "ativo": 1.725,
            "muito_ativo": 1.9
        }
        fator = fatores.get(self._nivel_atividade, 1.2)
        return self.calculo_basal() * fator

    @abstractmethod
    def calorias_objetivo(self):
        pass

    def __str__(self):
        return f"{self._nome} | {self._peso}kg | {self.__class__.__name__}"


class UsuarioEmagrecimento(Usuario):
    def calorias_objetivo(self):
        return self.calculo_gasto_energetico_total() - 500


class UsuarioGanhoMassa(Usuario):
    def calorias_objetivo(self):
        return self.calculo_gasto_energetico_total() + 500


class UsuarioManutencao(Usuario):
    def calorias_objetivo(self):
        return self.calculo_gasto_energetico_total()