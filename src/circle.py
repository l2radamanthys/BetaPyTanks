#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    version: 0.0.2
"""


from libs.vector2d import Vector2D


class Circle:
    """
        Objecto circunferencia creado para remplazar el control de coliciones
        rectangulares.
    """
    def __init__(self, radio=1):
        """
            constructor de la clase
        """
        self.centro = Vector2D()
        self.radio = radio


    def set_pos(self, x, y):
        """
            define la posicion central del circulo
        """
        self.centro.pos = (float(x), float(y))


    def get_pos(self):
        """
            obtiene la posicion central del circulo
        """
        #el valor de la posicion de un objecto Vector2D es una tupla
        #con valores en coma flotantes
        fx, fy = self.centro.pos
        x = int(round(fx))
        y = int(round(fy))
        return x,y


    def colicion(self, circle):
        """
            comprueba si coliciono contra otro circulo
        """
        #calculo la distancia entre los 2 vectores
        dist = distancia(circle.centro)
        #sumo los radios de ambos circulos
        sum_radios = self.radio + circle.radio

        #si la distancia es menor que la suma de los radios, entonces
        #colicionaron, caso contrario no.
        if dist < sum_radios:
            return True
        else:
            return False
