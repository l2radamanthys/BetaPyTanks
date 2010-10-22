#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
basic_guiu.py
=============

    Version: 0.1.8b (Beta)

    Autor: Ricardo D. Quiroga->L2Radamanthys

    Fecha: 18 de Febrero de 2010

    e-mail:
        l2radamanthys@gmail.com
        l2radamanthys@saltalug.org.ar
        ricardoquiroga.dev@gmail.com

    web:
        http://www.l2radamanthys.com.ar
        http://www.l2radamanthys.tk
        http://l2radamanthys.unlugar.com
        http://l2radamanthys.blogspot.com

    Descripcion:
        basic_guiu es una libreria pensada en principio para crear y manejar
        pequenios y simples menues, este modulo solo ofrece el manejo por
        separado de cada elemento de la guiu, por ende el uso del mismo solo
        se recomienda cuando se utilizan muy pocos elementos, aunque siempre
        es mas util y funcional utilizar el modulo frame.py que permite un
        manejo mas elegantes de grandes cantidades de elementos.

    Terminos y Condiciones:
        Este Script es Software Libre y esta bajo terminos de la GNU General
        Public Licence publicada por la Free Software Foundation
        (http://www.fsf.org) version 2 de la licencia u/o (opcionalmente)
        otras versiones de la licencia.

        Usted puede redistribuir y/o modificar este Script
        siguiendo los terminos de la GNU General Public Licence
        para mayor informacion vease la copia de la licencia que
        se adjunta con estos Script.
"""


import pygame
from pygame.locals import *

from colores import *

from constantes import *


def cargar_imagen(img_path, convert=False, alfa=None):
    """
        Funcion para Cargar una imagen desde un archivo optimiza el manejo
        ademas de aplicar un canal alfa (solo imagenes png, converter=True)
        si es que se necesita.

        ultimo cambio en: 0.1.8b
    """
    try:
        imagen = pygame.image.load(img_path)
    except pygame.error, message:
        print 'No se pudo cargar la imagen: ', img_path
        raise SystemExit, message

    if convert:
        if '.png' in img_path:
            imagen.convert_alpha()
        elif alfa != None:
            imagen.set_colorkey(alfa)
        else:
            imagen.set_colorkey(imagen.get_at((0, 0)))
    return imagen


class Boton:
    """
        Elemento indispensable para la creacion de menus, el boton no se genera
    autmomaticamente, se deve cargar una imagen con 2 partes la primera parte de
    la imagen es para el estado sin precion la segunda parte es para la img de
    precionado.
        El objecto boton responde a dos eventos basicos:
        -on_click()
        -a_hover()
    """
    def __init__(self, imagen=None, enable=True, converter=False):
        """
            imagen: corresponde al archivo con las dos partes del boton
            enable: si esta activo osea si respondera a los diferentes eventos
            converter: se coloca en True si se va a usar una imagen con canal alfa.
        """
        self.imagen = cargar_imagen(imagen, converter)
        self.rect = pygame.Rect(0, 0, self.imagen.get_width()/ 2, self.imagen.get_height())
        self.enable = enable
        self.precionado = False


    def mueve(self, x, y):
        """
            Mueve el objecto a la posicion (x,y) esta posicion representa
        el margen isquierdo superior del mismo.
        """
        self.rect.x = x
        self.rect.y = y


    def centrar(self, x, y):
        """
           Centra el objecto en la posicion (x,y).
        """
        self.rect.center = (x, y)


    def set_status(self, enable=True):
        """
            Habilita o desabilita el boton, esta funcion viene a remplazar
        a set_enable() en versiones anterior.
        """
        self.enable = enable


    def on_click(self, dx=0, dy=0, evt_btn=BTN_ISQ):
        """
            dx y dy representan el desplazamiento del boton por lo que no se
        necesita ni se deve modificar dichos argumentos solo se agregaron para
        mantener la compatibilidad con el modulo frame sin tener que crear un
        nuevo evento. Otra cosa importante a destacar es que por defecto el boton
        responde al click del boton isquierdo del mouse.
        """
        if self.enable:
            self.precionado = False
            btn = pygame.mouse.get_pressed()
            if btn[evt_btn]: #si se preciono con el boton primario
                x,y = pygame.mouse.get_pos()
                if self.rect.collidepoint(x-dx, y-dy):
                    self.precionado = True
                    return True
        return False


    def a_hover(self, dx, dy):
        """
            dx y dy representan el desplazamiento del boton por lo que no se
        necesita ni se deve modificar dichos argumentos solo se agregaron para
        mantener la compatibilidad con el modulo frame sin tener que crear un
        nuevo evento. Este evento se refiere a si el mouse esta por encima del
        boton
        """
        if self.enable:
            self.precionado = False
            btn = pygame.mouse.get_pressed()
            x,y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x-dx, y-dy):
                self.precionado = True
                return True
        return False


    def drawn(self, surface):
        """
            Metodo generico para dibujar el boton sobre una superficie.
        """
        if self.enable:
            rect = (self.rect.w * self.precionado, 0, self.rect.w, self.rect.h)
            surface.blit(self.imagen, self.rect, rect)


    def get_type(self):
        """
            Retorna un valor entero correspondiente al tipo de Objecto
        """
        return BOTON


class SwitchBtn(Boton):
    """
        El Switch Boton solo se diferencia en que no cambia automaticamente
        su valor de precionado a False si se deja de precionar el mouse, ademas
        no responde al evento a_hover, solo podra responder al evento on_click
    """
    def __init__(self, imagen=None, enable=True, converter=False):
        Boton.__init__(self, imagen, enable, converter=False)


    def set_estado(self, estado=None):
        """
            Determina el estado del boton, si no se pasa algun parametro el
            mismo invierte el estado actual del mismo
        """
        if estado == None:
            self.precionado = not(self.precionado)
        else:
            self.precionado = estado


    def cambiar_estado(self, estado=None):
        """
            invierte el estado actual
        """
        self.precionado = not self.precionado


    def get_estado(self):
        """
            Retorna el estado actual del objecto
        """
        if self.enable:
            return self.precionado


    def on_click(self, dx=0, dy=0, evt_btn=BTN_ISQ):
        """
            dx y dy representan el desplazamiento del boton por lo que no se
        necesita ni se deve modificar dichos argumentos solo se agregaron para
        mantener la compatibilidad con el modulo frame sin tener que crear un
        nuevo evento. Otra cosa importante a destacar es que por defecto el boton
        responde al click del boton isquierdo del mouse.
        """
        if self.enable:
            btn = pygame.mouse.get_pressed()
            if btn[evt_btn]: #si se preciono con el boton primario
                x,y = pygame.mouse.get_pos()
                if self.rect.collidepoint(x-dx, y-dy):
                    self.cambiar_estado()
        return self.get_estado()


    def click(self, dx=0, dy=0, evt_btn=BTN_ISQ):
        """
            Captura el evento click retornando True en caso que se hubiese
            hecho click sobre el boton en caso contrario devuelve None
            sirve cuando se desea simular el SpinBoton.
        """
        if self.enable:
            btn = pygame.mouse.get_pressed()
            if btn[0]:
                x,y = pygame.mouse.get_pos()
                if self.rect.collidepoint(x-dx,y-dy):
                    self.precionado = True
                    return self.precionado


    def a_hover(self, dx=0, dy=0):
        """
            Este evento se anulo para este tipo de objecto.
        """
        return None


    def get_type(self):
        """
            Retorna un valor entero correspondiente al tipo de Objecto
        """
        return SWICTH_BTN


class NewBoton:
    """
        Nueva version del objecto Boton que se vasa en 3 imagenes de estado
        a comparacion del boton normal que usa 2 imagenes de estado:
        -la primera es para vista cuando no se hizo click ni mouse encima
        -la segunda es para vista cuando no se hizo click y el mouse encima
        -la tercera es para vista cuando el mouse esta encima y hace click
    """

    def __init__(self, imagen=None, enable=True, converter=False):
        """
            Constructor de la clase
            imagen: corresponde al archivo con las dos partes del boton
            enable: si esta activo osea si respondera a los diferentes eventos
            converter: se coloca en True si se va a usar una imagen con canal alfa.
        """
        self.imagen = cargar_imagen(imagen, converter)
        self.rect = pygame.Rect(0, 0, self.imagen.get_width() / 3, self.imagen.get_height())
        self.enable = enable #estado del boton activo o no
        self.hover = False #si el mouse esta encima
        self.precionado = False #si se ha precionado


    def mueve(self, x, y):
        """
            Mueve el objecto a la posicion (x,y) esta posicion representa
        el margen isquierdo superior del mismo.
        """
        self.rect.x = x
        self.rect.y = y


    def centrar(self, x, y):
        """
           Centra el objecto en la posicion (x,y).
        """
        self.rect.center = (x, y)


    def on_click(self, dx=0, dy=0, evt_btn=BTN_ISQ):
        """
            dx y dy representan el desplazamiento del boton por lo que no se
        necesita ni se deve modificar dichos argumentos solo se agregaron para
        mantener la compatibilidad con el modulo frame sin tener que crear un
        nuevo evento. Otra cosa importante a destacar es que por defecto el boton
        responde al click del boton isquierdo del mouse.
        """
        if self.enable:
            self.hover = False
            self.precionado = False
            btn = pygame.mouse.get_pressed()
            x,y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x-dx, y-dy):
                self.hover = True
                if btn[evt_btn]: #si se preciono con el boton primario
                    self.precionado = True
                    return True
        return False


    def a_hover(self, dx=0, dy=0):
        """
            dx y dy representan el desplazamiento del boton por lo que no se
        necesita ni se deve modificar dichos argumentos solo se agregaron para
        mantener la compatibilidad con el modulo frame sin tener que crear un
        nuevo evento. Este evento se refiere a si el mouse esta por encima del
        boton
        """
        if self.enable:
            self.hover = False
            self.precionado = False
            x,y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x-dx, y-dy):
                self.hover = True
                return True
        return False


    def drawn(self, surface):
        """
            Metodo generico para dibujar el boton sobre una superficie.
        """
        if self.enable:
            if self.hover and not(self.precionado):
                dx = self.rect.w * 1
            elif self.precionado and self.precionado:
                dx = self.rect.w * 2
            else:
                dx = 0
            rect = (dx, 0, self.rect.w, self.rect.h)
            surface.blit(self.imagen, self.rect, rect)


    def get_type(self):
        """
        Retorna un valor entero correspondiente al tipo de Objecto
        """
        return NEW_BOTON


class Label:
    """
        Clase para modelar el elemento Etiqueta, este elemento por defecto
        no tiene ningun evento asociado a ella.
    """
    def __init__(self, value='', font=None, size=15, color=NEGRO, bgcolor=None):
        """
            -value: valor inicial
            -font: ruta de la fuente que se utilizara para renderizar
            -size: tamanio de la fuente
            -color: color del texto
            -bgcolor: color de fondo
        """
        self.value = value
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.bgcolor = bgcolor

        self.imagen = self.font.render(self.value,1,self.color)
        self.rect = self.imagen.get_rect()


    def bold(self, value=False):
        """
            Habilita el dibujado de la fuente en Negrita mientras que esta
            lo soporte.
        """
        self.font.set_bold(value)


    def italic(self, value=False):
        """
            Habilita la imitacion que da de texto en cursiva, por ende como en
            el caso de bold() el tipo de fuente tiene que poder soportar el
            mismo.
        """
        self.font.set_italic(value)


    def set_bgcolor(self, color):
        """
            Define el color de la barra de progreso
        """
        self.bgcolor = color
        print '>'

    def set_color(self, color):
        """
            Define el color de fondo de la barra de progreso
        """
        self.color = color


    def render(self):
        """
            Renderiza(dibuja) el texto con la Fuente y el formato especificado.
        """
        if self.bgcolor != None:
            self.imagen = self.font.render(self.value, 1, self.color, self.bgcolor)
        else:
            self.imagen = self.font.render(self.value, 1, self.color)
        self.rect.w = self.imagen.get_width()
        self.rect.h = self.imagen.get_height()


    def mueve(self, x, y):
        """
            Mueve el objecto a la posicion (x,y) esta posicion representa
            el margen isquierdo superior del mismo.
        """
        self.rect.x = x
        self.rect.y = y


    def centrar(self, x, y):
        """
           Centra el objecto en la posicion (x,y).
        """
        self.rect.center = (x, y)


    def drawn(self, surface):
        """
            Metodo generico para dibujar el boton sobre una superficie.
        """
        self.render()
        surface.blit(self.imagen, self.rect)


    def get_type(self):
        """
            Retorna un valor entero correspondiente al tipo de Objecto
        """
        return LABEL


class EditableText:
    """
        Clase que simula el funcionamiento de una caja de texto editable,
    la misma solo soporta letras ,numeros y algunos signos tales como ((),.=
    -_:;).
    """
    def __init__(self, value='', font=None, size=15, ancho=100, enable=True):
        """
            -value: valor inicial
            -font: ruta de la fuente que se utilizara para renderizar
            -size: tamanio de la fuente
            -ancho: ancho en pixeles del campo del editable
            -enabe: si esta activo o no
        """
        self.font = pygame.font.Font(font, size)
        self.value = value
        self.color = NEGRO #color principal
        self.bgcolor = BLANCO #color de fondo
        self.imagen = self.font.render(self.value,1,self.color)
        self.rect = self.imagen.get_rect()
        self.rect.width = ancho
        self.enable = enable  #si esta activa

        self.keydown = False
        self.keyup = False

    def set_color(self, color=None, bgcolor=None):
        """
            Funcion para determinar el color principal como el color de fondo
        """
        if color != None:
            self.color = color
        if bgcolor != None:
            self.bgcolor = bgcolor


    def colores(*argv):
        """
            Solo se define el metodo para mantener compatibilidad con versiones
            anteriores
        """
        self.set_color(*argv)


    def bold(self, value=False):
        """
            Habilita el dibujado de la fuente en Negrita mientras que esta
            lo soporte, en caso contrario pygame emula dicho modo.
        """
        self.font.set_bold(value)


    def italic(self, value=False):
        """
            Habilita la imitacion que da de texto en cursiva, por ende como en
            el caso de bold() el tipo de fuente tiene que poder soportar el
            mismo.
        """
        self.font.set_italic(value)


    def mueve(self, x, y):
        """
            Mueve el objecto a la posicion (x,y) esta posicion representa
            el margen isquierdo superior del mismo.
        """
        self.rect.x = x
        self.rect.y = y


    def centrar(self, x, y):
        """
           Centra el objecto en la posicion (x,y).
        """
        self.rect.center = (x, y)


    def set_enable(self, enable=True):
        """
            Habilitar o desabilitar manualmente el editable
        """
        self.enable = enable


    def get_caracter(self):
        """
            Funcion que reconoce si se preciono alguna tecla, por desgracia
            es muy sencible y para que funcione dicho objecto hay que mermar
            el frame rate.
        """
        value = ''
        key = pygame.key.get_pressed()

        #conjunto de caracteres agregados
        #nuevo en vesrion 0.1.6
        if key[K_MINUS]:
            value = '-'
        elif key[K_PLUS]:
            value = '+'
        elif key[K_PERIOD]:
            value = '.'
        elif key[K_COMMA]:
            value = ','
        elif key[K_LEFTPAREN]:
            value = '('
        elif key[K_RIGHTPAREN]:
            value = ')'
        elif key[K_ASTERISK]:
            value = '*'
        elif key[K_UNDERSCORE]:
            value = '_'
        elif key[K_KP_EQUALS]:
            value = '='
        elif key[K_COLON]:
            value = ':'
        elif key[K_SEMICOLON]:
            value = ';'

        elif key[K_a]:
            value = 'a'
        elif key[K_b]:
            value = 'b'
        elif key[K_c]:
            value = 'c'
        elif key[K_d]:
            value = 'd'
        elif key[K_e]:
            value = 'e'
        elif key[K_f]:
            value = 'f'
        elif key[K_g]:
            value = 'g'
        elif key[K_h]:
            value = 'h'
        elif key[K_i]:
            value = 'i'
        elif key[K_j]:
            value = 'j'
        elif key[K_k]:
            value = 'k'
        elif key[K_l]:
            value = 'l'
        elif key[K_m]:
            value = 'm'
        elif key[K_n]:
            value = 'n'
        elif key[K_o]:
            value = 'o'
        elif key[K_p]:
            value = 'p'
        elif key[K_q]:
            value = 'q'
        elif key[K_r]:
            value = 'r'
        elif key[K_s]:
            value = 's'
        elif key[K_t]:
            value = 't'
        elif key[K_u]:
            value = 'u'
        elif key[K_v]:
            value = 'v'
        elif key[K_w]:
            value = 'w'
        elif key[K_x]:
            value = 'x'
        elif key[K_y]:
            value = 'y'
        elif key[K_z]:
            value = 'z'

        #reconocimiento del teclado Numerico
        #nuevo en version 0.1.6
        elif (key[K_1] or key[K_KP1]):
            value = '1'
        elif (key[K_2] or key[K_KP2]):
            value = '2'
        elif (key[K_3] or key[K_KP3]):
            value = '3'
        elif (key[K_4] or key[K_KP4]):
            value = '4'
        elif (key[K_5] or key[K_KP5]):
            value = '5'
        elif (key[K_6] or key[K_KP6]):
            value = '6'
        elif (key[K_7] or key[K_KP7]):
            value = '7'
        elif (key[K_8] or key[K_KP8]):
            value = '8'
        elif (key[K_9] or key[K_KP9]):
            value = '9'
        elif (key[K_0] or key[K_KP0]):
            value = '0'
        elif key[K_SPACE]:
            value = ' '
        elif key[K_BACKSPACE]:
            value = 'del'

        #---detecion de mayusculas  minuscula (a partir de version 0.1.6)
        #--si se preciono la telcla mayus y shift no esta precionada
        #if (key[KMOD_CAPS] and not(key[KMOD_SHIFT])):
        #    value = value.upper()
        #--inverso a lo anterior
        #if (not(key[KMOD_CAPS]) and (key[KMOD_SHIFT])):
        #    value = value.upper()
        return value


    def del_ult(self):
        """
            Funcion algo mala que elimina el ultimo caracter, mejorada en
            version 0.1.7
        """
        #tengo que hacer un metodo mejor que esto :(
        #cad = ""
        #for i in range(len(self.value)-1):
        #    cad = cad + self.value[i]
        #self.value = cad

        self.value = self.value[:len(self.value)-1]


    def update(self, dx=0, dy=0):
        """
            Funcion para leer el teclado y actualiza el contenido
            del editable.
        """
        btn = pygame.mouse.get_pressed()
        if btn[0]:
            x,y = pygame.mouse.get_pos()
            #si se preciono l mouse sobre la caja del editable
            #se activa la posibilidad de modificar su contenido
            if self.rect.collidepoint(x - dx, y - dy):
                self.enable = True
            #caso contrario se desactiva esa posibilidad
            else:
                self.enable = False

        if self.enable:
            #if not(self.keydown):
            car = self.get_caracter()
            w,h = self.font.size(self.value + car)
            if car != 'del':
                if w <= (self.rect.w - 5):
                    self.value = self.value + car
            else:
                self.del_ult()


    def drawn(self,surface):
        """
            Muestra en pantalla
        """
        pygame.draw.rect(surface, self.bgcolor, self.rect, 0) #fondo
        pygame.draw.rect(surface, self.color, self.rect, 2) #borde

        self.imagen = self.font.render(self.value, 1, self.color)

        surface.blit(self.imagen, (self.rect.x + 3, self.rect.y))
        w,h = self.font.size(self.value)
        x1 = w + self.rect.x + 5
        y1 = self.rect.y
        pygame.draw.rect(surface, self.color,((x1,y1+3),(1,h-6)), 0)


    def get_type(self):
        """
            Retorna un valor entero correspondiente al tipo de Objecto
        """
        return EDITABLE


class Bitmap:
    """
        Simple contenedor de imagenes, solo que se puede manejar un poco
        mas facil
    """
    def __init__(self, imagen=None, converter=False, x=0, y=0,alfa=None):
        """
            imagen: ruta del archivo, puede ser bmg o png
            converter: si se usrara un color como canal alfa
            alfa: color que se utilizara como canal alfa
        """
        self.imagen = cargar_imagen(imagen, converter, alfa)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y


    def cambiar(self, imagen=None, converter=False, tipe=IMAGENFILE):
        """
            Cambia la imagen actual, el parametro imagen puede ser tanto una
            direcion de un archivo como un objecto mapa de bits.

            tipe: se refiere a que si se tomara la imagen desde una direcion
            o se tomara en base a un objecto existente.
        """
        if type:
            self.imagen = imagen
        else:
            self.imagen = pygame.image.load(imagen)


    def mueve(self, x, y):
        """
            Mueve el objecto a la posicion (x,y) esta posicion representa
            el margen isquierdo superior del mismo.
        """
        self.rect.x = x
        self.rect.y = y


    def centrar(self, x, y):
        """
           Centra el objecto en la posicion (x,y).
        """
        self.rect.center = (x, y)


    def drawn(self, surface):
        """
            Metodo de dibujo
        """
        surface.blit(self.imagen, self.rect)


    def get_type(self):
        """
            Retorna un valor entero correspondiente al tipo de Objecto
        """
        return IMAGEN


class ProgressBar:
    """
        Elemento Barra de Progreso, simula el funcionamiento de la misma
    """
    def __init__(self, ancho=104, alto=24, min=0, max=100, b_w=2 ,color=AZUL ,bgcolor=GRIS):
        """
            ancho, alto = tamanio en pixeles de la barra
            min = valor minimo normalmente es 0 (no acepta valores negativos)
            max = valor maximo de la mismo, no puede ser menor que min
            b_w = grosor del borde
            color = color principal
            bgcolor = color de fondo
        """
        self.rect = pygame.Rect(0, 0, ancho, alto)
        self.border_w = b_w
        self.bgcolor = bgcolor
        self.color = color

        self.value = 0
        self.max_value = max
        self.min_value = min
        self.dx = float(self.rect.w - self.border_w * 2) / float(max - min)


    def __ctrl(self):
        """
            Ccontrola que el valor no se valla fuera del rango establecido por
            min_value y max_value
        """
        if self.value > self.max_value:
            self.value = self.max_value

        elif self.value < self.min_value:
            self.value = self.min_value


    def set_bgcolor(self, color):
        """
            Define el color de la barra de progreso
        """
        self.bgcolor = color


    def set_color(self, color):
        """
            Define el color de fondo de la barra de progreso
        """
        self.color = color


    def inc(self, dx=None):
        """
            Incrementa el valor de la barra de progrecion
        """
        if dx == None:
            self.value += 1
        else:
            self.value += dx
        self.__ctrl()


    def set_value(self, val):
        """
            Asigna un valor determinado a la barra de progreso
        """
        self.value = val
        self.__ctrl()


    def mueve(self, x, y):
        """
            Mueve el objecto a la posicion (x,y) esta posicion representa
        el margen isquierdo superior del mismo.
        """
        self.rect.x = x
        self.rect.y = y


    def centrar(self, x, y):
        """
           Centra el objecto en la posicion (x,y).
        """
        self.rect.center = (x, y)


    def drawn(self, surface):
        """
            Metodo de dibujo del objecto
        """
        pygame.draw.rect(surface, self.bgcolor, self.rect, 0)
        if self.value != self.min_value:
            w = int(self.value * self.dx)
            h = self.rect.h - (self.border_w * 2)
            x = self.rect.x + self.border_w
            y = self.rect.y + self.border_w
            pygame.draw.rect(surface, self.color, (x, y, w, h), 0)


    def get_type(self):
        """
            Retorna un valor entero correspondiente al tipo de Objecto
        """
        return PROGRESS_BAR


class ImagenList: #nuevo en version 0.1.7
    """
        Objecto que maneja una imagen que posee varios clips ya sean estos
        en verticalu horizontal
    """
    def __init__(self, ruta='', offsheet=0, px=0, py=0, mode=HORIZONTAL):
        """
            Constructor de la clase ImagenList
            ruta: direcion de la imagen con los frames
            offsheet: desplazaminto de cada frame
            px, py: posicion dentro de pantalla
            mode: modo del offsheet puede ser HORIZONTAL o VERTICAL
        """
        self.imagen = cargar_imagen(ruta, True, MAGENTA)

        if mode == HORIZONTAL:
            w = offsheet
            h = self.imagen.get_height()
            nf = self.imagen.get_width() / w
        else:
            w = self.imagen.get_width()
            h = offsheet
            nf = self.imagen.get_height() / h

        self.rect = pygame.Rect(0, 0, w, h) #area de recorte
        self.offsheet = offsheet #desplazaminto
        self.mode = mode #si se desplazara horizontal o verticalmete

        self.frame_act = 0 #idicador del frame actual que se mostrara
        self.num_frames = nf #cantidad de cuadros que tiene la imagen

        self.x, self.y = px, py #posicion x,y de la imagen


    def __ctrl(self):
        """
            Funcion interna que controla que el valor no se salga de rango
        """
        if self.frame_act < 0 or self.frame_act >= self.num_frames:
            print "Valor fuera de rango: %d max: %d" %(self.frame_act, self.num_frames)
            self.frame_act = 0


    def set_frame(self, f=0):
        """
            Define un frame especifico dentro de la tira de imagenes
        """
        self.frame_act = f
        self.__ctrl()


    def get_frame(self):
        """
            Retorna el frame actual que se esta utilizando
        """
        return self.frame_act


    def inc(self, dx=None):
        """
            Incrementa o drecremente apuntador del frame de acuerdo al valor
            pasado por parametro
        """
        if dx == None:
            self.frame_act += 1
        else:
            self.frame_act += dx
        self.__ctrl()


    def mueve(self, px, py):
        """
            Mueve el objecto a la posicion (x,y) esta posicion representa
            el margen isquierdo superior del mismo.
        """
        self.x = x
        self.y = y


    def centrar(self, x, y):
        """
           Centra el objecto en la posicion (x,y).
        """
        if self.mode == HORIZONTAL:
            self.x = x - self.offsheet / 2
            self.y = y - self.imagen.get_height() / 2
        else:
            self.x = x - self.imagen.get_width() / 2
            self.y = y - self.offsheet / 2


    def drawn(self, surface):
        """
            Metodo generico para dibujar el boton sobre una superficie.
        """
        if self.mode == HORIZONTAL:
            self.rect.x = self.frame_act * self.offsheet
        else:
            self.rect.y = self.frame_act * self.offsheet
        surface.blit(self.imagen, (self.x, self.y), self.rect)


    def get_type(self):
        """
            Retorna un valor entero correspondiente al tipo de Objecto
        """
        return IMAGEN_LIST


# los componentes que aqui se nombran corresponden a aquellos que por cuestiones
#de estilo de codigo se los renombro pero se quiere mantener cierta compatibilidad
#con versiones anteriores, Ademas los unicos cambios importantes son con respecto
#al nombre de la clase ya que aunque se agreguen nuevos metodos los anteriores
#siguen estando (en su mayoria) vigentes.

def Switch_btn(*argv):
    return SwitchBtn(*argv)

def Editable_text(*argv):
    return EditableText(*argv)

def Static_Bitmap(*argv):
    return Bitmap(*argv)

def Progress_bar(*argv):
    return ProgressBar(*argv)

