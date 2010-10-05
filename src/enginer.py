#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    version: 0.0.1
    desc:

"""

from constantes import *
from circle import Circle


class GameEnginer:
    """
        en esta version los tankes se representaran mediantes
        circulos directamentea al igual que los disparos.
    """
    def __init__(self):
        """
            constructor
        """
        self.tanke_rojo = Circle(TANK_RADIO)
        self.tanke_azul = Circle(TANK_RADIO)

        self.disp_rojo = Circle(SHOT_RADIO)
        self.disp_azul = Circle(SHOT_RADIO)

        self.__data = DEF_DATA


    def parse_red_data(self, data):
        """
            carga la informacion proporcionada por el tanke rojo
        """
        self.__data[ROJO_X] = data[ROJO_X]
        self.__data[ROJO_Y] = data[ROJO_Y]
        self.__data[ROJO_BASE_ANG] = data[ROJO_BASE_ANG]
        self.__data[ROJO_CANON_ANG] = data[ROJO_CANON_ANG]
        self.__data[ROJO_SHOT_X] = data[ROJO_SHOT_X]
        self.__data[ROJO_SHOT_Y] = data[ROJO_SHOT_Y]
        self.__data[ROJO_SHOT_ANGLE] = data[ROJO_SHOT_ANGLE]
        self.__data[ROJO_SHOT_STATUS] = data[ROJO_SHOT_STATUS]


    def parse_blue_data(self, data):
        """
            carga la informacion proporcionada por el tanke azul
        """
        self.__data[AZUL_X] = data[AZUL_X]
        self.__data[AZUL_Y] = data[AZUL_Y]
        self.__data[AZUL_BASE_ANG] = data[AZUL_BASE_ANG]
        self.__data[AZUL_CANON_ANG] = data[AZUL_CANON_ANG]
        self.__data[AZUL_SHOT_X] = data[AZUL_SHOT_X]
        self.__data[AZUL_SHOT_Y] = data[AZUL_SHOT_Y]
        self.__data[AZUL_SHOT_ANGLE] = data[AZUL_SHOT_ANGLE]
        self.__data[AZUL_SHOT_STATUS] = data[AZUL_SHOT_STATUS]


    def get_data(self):
        """
            retorna la informacion del juego
        """
        return self.__data


    def ctrl_tankes(self):
        """
            actualiza el estado de los tankes
        """
        pass


    def ctrl_shots(self):
        """
            actualiza y controla las posiciones y estados de los disparos
        """
        pass


