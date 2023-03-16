import pytest

from codigo.bytebank import Funcionario

class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000' # Given - CONTEXTO
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 2000)
        resultado = funcionario_teste.idade() # When - AÇÃO

        assert resultado == esperado # Then - DESFECHO

    def test_quando_sobrenome_recebe_silveira_deve_retornar_silveira(self):
        entrada = ' Lucas Silveira '
        esperado = 'Silveira'

        funcionario_lucas = Funcionario(entrada, '13/03/2000', 5000)
        resultado = funcionario_lucas.sobrenome()

        assert resultado == esperado

    def test_quando_recebe_mais_de_cem_mil_deve_retornar_decrescimo_salario_de_dez_porcento(self):
        entrada_salario = 900000 #GIVEN
        entrada_nome = 'Paulo Coelho'
        decrescimo = entrada_salario * 0.1
        esperado = entrada_salario - decrescimo

        funcionario_teste = Funcionario(entrada_nome, '18/02/1993', entrada_salario)
        funcionario_teste.decrescimo_salario()     # WHEN
        resultado = funcionario_teste.salario

        assert resultado == esperado #THEN

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000 #GIVEN
        esperado = 100

        funcionario_teste = Funcionario('teste', '18/02/1993', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 100000 # GIVEN

            funcionario_teste = Funcionario('teste', '18/02/1993', entrada_salario)
            resultado = funcionario_teste.calcular_bonus() # WHEN

            assert resultado # THEN