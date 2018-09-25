__author__ = 'Сафин Ильшат'

# coding: utf-8

# Сделал только easy задачи, с основными буду разбираться в отпуске.

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round(math.sqrt(int((((b_y - a_y) ** 2) + ((b_x - a_x) ** 2)))), 2)
        self.BC = round(math.sqrt(int((((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int((((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def tria_perimetr(self):
        self.tria_perimetr = (self.AB + self.BC + self.CA)
        return (self.tria_perimetr)

    def tria_area(self):
        self.tria_perimetr /=2
        self.tria_area =  round(math.sqrt(self.tria_perimetr*(self.tria_perimetr - self.AB)*(self.tria_perimetr - self.BC)* (self.tria_perimetr - self.CA)),2)
        return (self.tria_area)

    def tria_height(self):
        self.tria_area *=2
        self.tria_height =  round((self.tria_area / self.CA),2)
        return (self.tria_height)

my_triangle = Triangle(1,2,4,7,8,5)

print('Длина строны АВ = {}, ВС = {}, СА = {}'.format(my_triangle.AB, my_triangle.BC,my_triangle.CA))
print('Периметр треугольника АВС равен {}'.format(my_triangle.tria_perimetr()))
print('Площадь треугольника АВС равна {}'.format(my_triangle.tria_area()))
print('Высота треугольника АВС, проведенная из угла В равна {}'.format(my_triangle.tria_height()))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class Trapezoid:
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.d_x = d_x
        self.d_y = d_y
        self.AB = round(math.sqrt(int((((b_y - a_y) ** 2) + ((b_x - a_x) ** 2)))), 2)
        self.BC = round(math.sqrt(int((((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CD = round(math.sqrt(int((((c_y - d_y) ** 2) + ((c_x - d_x) ** 2)))), 2)
        self.DA = round(math.sqrt(int((((a_y - d_y) ** 2) + ((a_x - d_x) ** 2)))), 2)
        self.AC = round(math.sqrt(int((((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)
        self.BD = round(math.sqrt(int((((d_y - b_y) ** 2) + ((d_x - b_x) ** 2)))), 2)

 
    def trap_perimetr(self):
        self.trap_perimetr = round((self.AB + self.BC + self.CD + self.DA), 2)
        return (self.trap_perimetr)
    
    def trap_area(self):
        self.trap_height = round(math.sqrt(self.AB ** 2 - (((self.CD - self.AB) ** 2 + self.DA ** 2 - self.BC ** 2) / (2 * (self.AB - self.CD))) ** 2), 2)
        self.trap_area = round(0.5 * (self.AB + self.CD) * self.trap_height, 2)
        return (self.trap_area)
    
    def isTrapezoidEqu(self):
        if self.AC == self.BD:
            return True
        return False
    
my_trap = Trapezoid(2,4,4,5,6,1,1,1)

print('Длина строны АВ = {}, ВС = {}, СD = {}, DA = {}'.format(my_trap.AB,my_trap.BC,my_trap.BC,my_trap.DA))
print('Периметр трапеции АВСD равен {}'.format(my_trap.trap_perimetr()))
print('Площадь трапеции АВСD равна {}'.format(my_trap.trap_area()))

