class Pessoa:
    def __init__(self, nome, sobrenome, identidade):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__identidade = identidade

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @property
    def identidade(self):
        return self.__identidade


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, identidade, salario):
        super().__init__(nome, sobrenome, identidade)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @property
    def salario_liquido(self):
        return self.__salario * 0.95

    @property
    def nome_completo(self):
        return f'{self.sobrenome} {self.nome}'

    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario


class FuncionarioPublico(Funcionario):
    def __init__(self, nome, sobrenome, identidade, salario):
        super().__init__(nome, sobrenome, identidade, salario)

    @property
    def salario_liquido(self):
        return self.salario * 0.98


if __name__ == '__main__':
    pessoa1 = FuncionarioPublico('Thales', 'Lopes', 123456789, 1000.00)

    print(pessoa1.nome_completo)
    pessoa1.salario = 2000.00
    print(pessoa1.salario_liquido)
