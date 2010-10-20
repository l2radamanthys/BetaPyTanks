#!/usr/bin/env python
# -*- coding: utf-8 -*-


from math import sin, cos, radians

import pygame
from pygame.locals import *

from constantes import *
from libs.colores import MAGENTA


class Tank:
    def __init__(self, img_base, img_canon, color):
        """
        """
        #base del tanke
        self.__img_base = pygame.image.load(img_base)
        self.img_base = self.__img_base.copy()
        self.img_base.set_colorkey(MAGENTA)
        self.rect_base = self.img_base.get_rect()

        #canon del tanke
        self.__img_canon = pygame.image.load(img_canon)
        self.img_canon = self.__img_canon.copy()
        self.img_canon.set_colorkey(MAGENTA)
        self.rect_canon = self.img_canon.get_rect()

        #angulo y orientacion de la base y el cañon
        self.base_angle = 0
        self.canon_angle = 0

        #informacion adicional
        self.life = 0
        self.__color = color


    def set_pos(self, x, y):
        """
            Traslada el tanke y lo centra en la posicion x, y
        """
        self.rect_base.center = (x, y)
        self.rect_canon.center = self.rect_base.center


    def set_angle(self, base_angle=0, canon_angle=0):
        """
            Define en angulo de la base y el canion del tanke
        """
        self.base_angle = base_angle
        self.canon_angle = canon_angle


    def upd_imagen(self):
        """
            actualiza la imagen
        """
        self.img_base = pygame.transform.rotate(self.__img_base, -self.base_angle)
        self.img_base.set_colorkey(MAGENTA)
        self.img_canon = pygame.transform.rotate(self.__img_canon, -self.canon_angle)
        self.img_canon.set_colorkey(MAGENTA)
        pass


    def upd_posicion(self):
        """
            actualiza la posicion del tanke
        """
        self.rect_canon.w = self.img_canon.get_width()
        self.rect_canon.h = self.img_canon.get_height()

        self.rect_base.w = self.img_base.get_width()
        self.rect_base.h = self.img_base.get_height()

        self.rect_canon.center = self.rect_base.center


    def ctrl(self):
        """
        """
        pass


    def update(self, data):
        """
            Actualiza la posicion del tanke, de acuerdo a los datos recividos
            desde el servidor
        """
        #toma la informacion de acuerdo al color del tanke
        if self.__color == ROJO:
            self.rect_base.center = data[ROJO_X], data[ROJO_Y]
            self.base_angle = data[ROJO_BASE_ANG]
            self.canon_angle = data[ROJO_CANON_ANG]
            self.life = data[ROJO_LIFE]

        elif self.__color == AZUL:
            self.rect_base.center = data[AZUL_X], data[AZUL_Y]
            self.base_angle = data[AZUL_BASE_ANG]
            self.canon_angle = data[AZUL_CANON_ANG]
            self.life = data[AZUL_LIFE]


    def drawn(self, surface):
        """
            Dibuja el tanke en pantalla
        """
        self.upd_imagen()
        self.upd_posicion()
        surface.blit(self.img_base, self.rect_base)
        surface.blit(self.img_canon, self.rect_canon)
