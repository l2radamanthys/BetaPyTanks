#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

from constantes import *

from colores import MAGENTA

"""
frame.py
========
    Version: 0.1.1 (beta)

    Autor: Ricardo D. Quiroga->L2Radamanthys

    Fecha: 18 de Febrero de 2010

    E-mail:
        l2radamanthys@gmail.com
        ricardoquiroga.dev@gmail.com
        l2radamanthys@saltalug.org.ar

    Web:
        http://www.l2radamanthys.com.ar
        http://www.l2radamanthys.tk
        http://l2radamanthys.unlugar.com
        http://l2radamanthys.blogspot.com

    Descripcion:
        frame.py es una clase derivada de basic_guiu, la cual es estable pero
        actualmente se encuentra en pleno desarrollo en modo testing. La misma
        esta orientada al manejo de ventanas pero con una idea mas sencilla
        la misma no sigue un patron de desarrollo estandar por lo que puede que no sea
        compatible con otras verciones anteriores...

    Terminos y Condiciones:
        Este Script es Sofware Libre y esta vajo terminos de la GNU General Public Licence
        publicada por la Free Sofware Foundation (http://www.fsf.org) vercion 2
        de la licencia o (opcinalmente) otras verciones de la licencia.

        Usted puede redistribuir y/o modificar este Script
        siguiendo los terminos de la GNU General Public Licence
        para mayor informacion lease la copia de la licencia que
        se adjunta con estos script.
"""

import pygame
from pygame.locals import *

from colores import *

from constantes import *
from basic_guiu import *


class Frame(object):
    """
        Clase base para el disenio de ventanas, por razones de uso se decidio
    que la implementacion y control de las mismas sea manejado casi por
    completo por el usuario. A partir de la version 0.0.8 esta habilitado
    el soporte para multiples ventanas.
    """
    def __init__(self, x=0, y=0, w=0, h=0, bgcolor=GRIS, enable=True):
        """
            Este modelo de ventana no posee bordes.
        """
        self.background = pygame.Surface((w, h)).convert()
        self.rect = self.background.get_rect()
        self.rect.x = x
        self.rect.y = y

        #color de fondo de la ventana
        self.bgcolor = bgcolor
        #se implementara un contenedor generico
        self.elementos = {}
        #caracteristica que se agrega para utilizar en proximas versiones
        self.enable = enable


    def resize(self, w, h):
        """
            Redimenciona el tamanio de la ventana
        """
        self.background = pygame.Surface((w, h)).convert()
        self.rect.w = self.background.get_width()
        self.rect.h = self.background.get_height()


    def mueve(self, x, y):
        """
            Mueve la ventana a la posicion (x,y) esta posicion representa
        el margen isquierdo superior del mismo.
        """
        self.rect.x = x
        self.rect.y = y


    def centrar(self, x, y):
        """
            Centra la ventana en un punto determinado,
            nuevo en version 0.1.6
        """
        self.rect.center = (x,y)

    """
            Los siguientes metodos sirvern para inserar objectos dentro de la
        ventana de acuerdo a su tipo aunque esta nueva version agrega un metodo
        generco para insertar objectos.
            Algo importante a recalcar es que dos objectos no pueden tener el
        mismo nombre, es mas el ultimo objecto que se ingrese con el mismo nombre
        remplazara al anterior.
    """

    def insert_boton(self, name='', imagen=None, enable=True, converter=False):
        #elemento Boton
        self.elementos[name] = Boton(imagen, enable, converter)


    def insert_switch_btn(self, name='', imagen=None, enable=True, converter=False):
        #mas parecido a un check_box
        self.elementos[name] = SwitchBtn(imagen, enable, converter)


    def insert_label(self, name='', value='', font=None, size=10, color=NEGRO, bgcolor=None):
        #etiqueta
        self.elementos[name] = Label(value, font, size, color, bgcolor)


    def insert_edt(self, name='', value='', font=None, size=10, ancho=100):
        #texto editable
        self.elementos[name] = EditableText(value, font, size, ancho, enable=False)


    def insert_img(self, name='', imagen=None, x=0, y=0, converter=False):
        #una imagen estatica
        self.elementos[name] = Bitmap(imagen, converter, x, y)


    def insert_progress_bar(self, name='', ancho=104, alto=24, min=0, max=100, b_w=2 ,color=AZUL ,bgcolor=GRIS):
        #una barra de Progrecion
        self.elementos[name] = ProgressBar(ancho,alto,min,max,b_w,color,bgcolor)


    def insert_image_list(self, name='', ruta='', offsheet=0, px=0, py=0, mode=HORIZONTAL):
        #inserta una lista de imagenes, nuevo en version 0.1.7
        self.elementos[name] = ImagenList(ruta, offsheet, px, py, mode)


    def insert_new_boton(self, name='', imagen=None, enable=True, converter=False):
        #elemento Boton
        self.elementos[name] = NewBoton(imagen, enable, converter)


    def insert(self, tipe=None, name='', *argv):
        """
            Inserta un objecto especificando el tipo, nombre y argumentos
            del mismo. nuevo en version 0.1.0
        """
        new_object = {
            BOTON : Boton,
            LABEL : Label,
            EDITABLE : EditableText,
            IMAGEN : Bitmap,
            SWICTH_BTN : SwitchBtn,
            PROGRESS_BAR : ProgressBar,
            IMAGEN_LIST: ImagenList,
            NEW_BOTON: NewBoton
        }

        self.elementos[name] = new_object[tipe](*argv)


    def __getitem__(self, key):
        """
        Nuevo en version 0.0.9, devuelve el objecto llamandolo directamente por
        su identificador
        """
        return self.elementos[key]


    def mueve_obj(self, name='', x=0, y=0):
        """
            Mueve el objecto a la posicion (x,y) esta posicion representa
        el margen isquierdo superior del mismo.
        """
        self.elementos[name].mueve(x,y)


    def centrar_obj(self, name='', x=0, y=0):
        """
           Centra el objecto en la posicion (x,y). nuevo en version 0.1.0
        """
        self.elementos[name].centrar(x,y)


    def get_type(self, name):
        """
            devuelve el tipo especifico de un objecto determinado
        """
        return self.elementos[name].get_type()


    def update(self):
        """
            solo actualiza el comportamiento de los edt y de los switch_btn
        """
        for obj in self.elementos:
            if self.get_type(obj) == EDITABLE:
                self.elementos[obj].update(self.rect.x, self.rect.y)
            if self.get_type(obj) == SWICTH_BTN:
                    self.elementos[obj].on_click(self.rect.x,self.rect.y)


    def on_click(self):
        """
        retorna un dicionario con todos los identificadores de los
        botones y switc_btn con su estado (precionado o no) osea
        True si se clickeo sobre el boton false en caso contrario
        """
        result = {}
        if self.enable:
            for obj in self.elementos:
                if self.get_type(obj) == BOTON:
                    result[obj] = self.elementos[obj].on_click(self.rect.x, self.rect.y)
                elif self.get_type(obj) == SWICTH_BTN:
                    result[obj] = self.elementos[obj].get_estado()
                elif self.get_type(obj) == NEW_BOTON:
                    result[obj] = self.elementos[obj].on_click(self.rect.x, self.rect.y)
        return result


    def a_hover(self):
        """
        retorna un listado con todos los botones y su estado,
        true si el cursor esta encina del mismo, false en caso contrario
        """
        result = {}
        if self.enable:
            for obj in self.elementos:
                if self.get_type(obj) == BOTON:
                    result[obj] = self.elementos[obj].a_hover(self.rect.x,self.rect.y)
                elif self.get_type(obj) == NEW_BOTON:
                    result[obj] = self.elementos[obj].a_hover(self.rect.x,self.rect.y)
        return result


    def drawn(self, surface):
        """Dibuja la ventana con todos los elementos que contiene"""
        if self.enable:
            self.background.fill(self.bgcolor)
            for obj in self.elementos:
                self.elementos[obj].drawn(self.background)
            surface.blit(self.background, self.rect)


class xFrame(Frame):
    """
        Derivado de Frame que la unica mejora es que la misma se dibuja el borde
    """
    def __init__(self, x, y, w, h, ruta='', color=GRIS_CLARO, t_w=16, t_h=16):
        """
            imagen = se refiere a la ruta que contiene las paleta de imagenes
            con los bordes de la ventana.
            t_w, t_h : ancho y alto respectivamente de los bordes
        """
        Frame.__init__(self, x, y, w, h, color)

        self.imagen = cargar_imagen(ruta, True, MAGENTA)
        self.imagen.set_colorkey(MAGENTA)
        self.tile_ancho = t_w
        self.tile_alto = t_h


    def dibuja_borde(self):
        """
            Funcion que le agrega borde a la ventana
        """
        x = 0
        y = 0
        while x < self.rect.w:
            self.background.blit(self.imagen, (x, 0), (0, 0, self.tile_ancho, self.tile_alto))
            self.background.blit(self.imagen, (x, self.rect.h - self.tile_alto), (1 * self.tile_ancho, 0, self.tile_ancho, self.tile_alto))
            x += self.tile_ancho
        while y < self.rect.h:
            self.background.blit(self.imagen, (0, y), (2 * self.tile_ancho, 0, self.tile_ancho, self.tile_alto))
            self.background.blit(self.imagen, (self.rect.w - self.tile_ancho, y), (3 * self.tile_ancho, 0, self.tile_ancho, self.tile_alto))
            y += self.tile_alto

        self.background.blit(self.imagen, (0, 0), (0, 1 * self.tile_alto, self.tile_ancho, self.tile_alto))
        self.background.blit(self.imagen, (self.rect.w - self.tile_ancho,0), (1 * self.tile_ancho, 1 * self.tile_alto, self.tile_ancho, self.tile_alto))
        self.background.blit(self.imagen, (0,self.rect.h - self.tile_alto), (2 * self.tile_ancho, 1 * self.tile_alto, self.tile_ancho, self.tile_alto))
        self.background.blit(self.imagen, (self.rect.w - self.tile_ancho,self.rect.h - self.tile_alto), (3 * self.tile_ancho, 1 * self.tile_alto, self.tile_ancho, self.tile_alto))


    def drawn(self, surface):
        """
            dibuja la ventana con todas sus caracteristicas y elementos
        """
        if self.enable:
            self.background.fill(self.bgcolor)
            self.dibuja_borde()
            for obj in self.elementos:
                self.elementos[obj].drawn(self.background)
            surface.blit(self.background, self.rect)

