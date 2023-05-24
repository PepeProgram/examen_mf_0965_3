#  Copyright (c) 2023. José Manuel Abelleira López.
#
#  Copyright (c) 2023. José Manuel Abelleira López.
# 1 - Crea una clase abstracta Empleado que tenga como atributos el nombre y el salario, y
# como método abstracto calcular_salario. Crea una subclase Programador que herede de
# Empleado y que tenga como atributo el número de líneas de código escritas por día, y
# como método calcular_salario que devuelva el salario base más un bonus en función del
# número de líneas de código. Crea otra subclase Gestor Proyectos que herede de
# Empleado y que tenga como atributo el número de proyectos gestionados por mes, y
# como método calcular salario que devuelva el salario base más un bonus en función del
# número de proyectos gestionados.
from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    @abstractmethod
    def calcular_salario(self):
        pass


class Programador(Empleado):
    def __init__(self, nombre, salario, lin_cod):
        super().__init__(nombre, salario)
        self.lin_cod = lin_cod

    def calcular_salario(self):
        bonus = self.lin_cod * 0.05
        return self.salario + bonus


class GestorProyectos(Empleado):
    def __init__(self, nombre, salario, n_proy):
        super().__init__(nombre, salario)
        self.n_proy = n_proy

    def calcular_salario(self):
        bonus = self.n_proy * 50
        return self.salario + bonus


pepe = Programador('Pepe', 5000, 30000)
print(f'Pepe cobra este mes: {"{0:.2f}".format(pepe.calcular_salario())}€')

maria = GestorProyectos('María', 5000, 18)
print(f'María cobra este mes: {"{0:.2f}".format(maria.calcular_salario())}€')

