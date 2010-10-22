#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    version: 0.0.5
"""

import sys
import socket
import json
from math import cos, sin

from event import Event, EventQueue
from constantes import *


class Bot(object):
    """
    """
    def __init__(self, name='Default', host=DEF_HOST, port=DEF_BOT_PORT):
        """
            Constructor de la clase

            name: nombre del bot
            host: direcion del servidor
            port: nro de puerto de conecion
        """
        if len(name) <= 16:
            self.__name = name
        else:
            self.__name = name[:16]
        self.__color = None

        #dicionario usado para manejar las aciones
        self.__eventos = EventQueue()

        #dicionario que contiene toda la informacion del juego
        self.__data = DEF_DATA
        #conector con el servidor
        self.__socket = None
        #variable que indica el estado de la conecion
        self.__conectado = False
        #intenta establecer la conecion con el servidor
        self.__conectar(host, port)


    def __conectar(self, host, port):
        """
            crea la conecion entre el bot y el servidor ademas de cargar
            toda la informacion necesaria
        """

        print "Conectando con el Servidor: %s en el Puerto: %s " %(host, port),
        #creando la conecion
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect((host, port))
        print "[OK]"

        #definiendo color
        data = self.__socket.recv(BUFF_SIZE)
        if 'rojo' in data.lower():
            self.__color = ROJO
        if 'azul' in data.lower():
            self.__color = AZUL

        print data

        #enviar el nombre del bot al servidor
        self.__socket.send(self.__name)

        #inicializar la informacion del bot
        self.__recivir_datos()
        self.__conectado = True


    def girar_base(self, dir=ISO_NONE):#, grados=1):
        """
            Comando que sirve para girar la base del tanke
            dir:  direcion en la cual girara la base
        """
        #especifica la direcion de giro
        if dir == ISO_IZQ:
            evt = Event(GIRAR_BASE_E, GIRAR_IZQ)
        elif dir == ISO_DER:
            evt = Event(GIRAR_BASE_E, GIRAR_DER)
        else:
            evt = Event(NONE_E, NONE_ACTION)
        self.__eventos.push(evt)
        del evt
        #if grados < 1:
        #    grados = 0
        #elif grados > 5:
        #    grados = 5
        #especifica la cantidad de grados que girara el canon
        #self.aciones['BASE_GIRO'] = grados


    def girar_canon(self, dir=ISO_NONE):#, grados=1):
        """
            Comando que sirve para girar la torre del tanke
            dir:  direcion en la que se girara la torre
        """
        #especifica la direcion de giro
        if dir == ISO_IZQ:
            evt = Event(GIRAR_CANON_E, GIRAR_IZQ)
        elif dir == ISO_DER:
            evt = Event(GIRAR_CANON_E, GIRAR_DER)
        else:
            evt = Event(NONE_E, NONE_ACTION)
        self.__eventos.push(evt)
        del evt
        #if grados < 1:
        #    grados = 0
        #elif grados > 5:
        #    grados = 5
        #especifica la cantidad de grados que girara el canon
        #self.aciones['CANON_GIRO'] = grados


    def girar(self, dir):#, grados):
        """
            Comando para gira tanto la base como el canion
            dir:  direcion en la que se girara la torre puede
        """
        if dir == ISO_IZQ:
            evt = Event(GIRAR_E, GIRAR_IZQ)
        elif dir == ISO_DER:
            evt = Event(GIRAR_E, GIRAR_DER)
        else:
            evt = Event(NONE_E, NONE_ACTION)
        self.__eventos.push(evt)
        del evt


    def mover(self, dir):
        """
            Comando para mover el tanke hacia adelante o atras el movimiento
            del mismo dependera directamente del angulo de la base del tanke.
        """
        #self.aciones['MOVER'] = dir
        if dir == ISO_ADELANTE:
            evt = Event(GIRAR_CANON_E, MOVER_ATRAS)
        elif dir == ISO_ATRAS:
            evt = Event(GIRAR_CANON_E, MOVER_ATRAS)
        else:
            evt = Event(NONE_E, NONE_ACTION)
        self.__eventos.push(evt)
        del evt


    def disparar(self):
        """
            Comando para Disparar una municion, la direcion de la misma es la
            misma que la direcion de la torre del canion al momento de
            efectuarse la acion
        """
        evt = Event(ATACAR_E, ATACAR)
        self.__eventos.push(evt)
        del evt


    def update(self):
        """
            Este metodo deve ser redefinido en la implementacion de la IA
        """
        pass


    def __inc(self, key_r, key_b, dx):
        """
        """
        if self.__color == ROJO:
            self.__data[key_r] += dx

        elif self.__color == AZUL:
            self.__data[key_b] += dx


    def __get(self, key_r, key_b):
        """
            key_r: indentificador que usara si el color es ROJO
            key_b: identificador que usara si el color es AZUL
        """
        if self.__color == ROJO:
            return self.__data[key_r]
        if self.__color == AZUL:
            return self.__data[key_b]


    def __borrar_aciones(self):
        """
        """
        self.__eventos.clear()


    def get(self, key):
        """
            Metodo especifico para devolver informacion diversa del estado
            posicion de los bots, es el unico metodo que puede ser invocado
            por las IA.
        """
        if key == BOT_X:
            info = self.__get(ROJO_X, AZUL_X)
        elif key == BOT_Y:
            info = self.__get(ROJO_Y, AZUL_Y)
        elif key == BOT_SX:
            info = self.__get(ROJO_SX, AZUL_SX)
        elif key == BOT_SY:
            info = self.__get(ROJO_SY, AZUL_SY)
        elif key == BOT_SS:
            info = self.__get(ROJO_SS, AZUL_SS)
        elif key == BOT_BA:
            info = self.__get(ROJO_BASE_ANG, AZUL_BASE_ANG)
        elif key == BOT_CA:
            info = self.__get(ROJO_CANON_ANG, AZUL_CANON_ANG)
        elif key == BOT_HP:
            info = self.__get(ROJO_LIFE, AZUL_LIFE)


        elif key == ENE_X:
            info = self.__get(AZUL_X, ROJO_X)
        elif key == ENE_Y:
            info = self.__get(AZUL_Y, ROJO_Y)
        elif key == ENE_SX:
            info = self.__get(AZUL_SX, ROJO_SX)
        elif key == ENE_SY:
            info = self.__get(AZUL_SY, ROJO_SY)
        elif key == ENE_SS:
            info = self.__get(AZUL_SS, ROJO_SS)
        elif key == ENE_BA:
            info = self.__get(AZUL_SS, ROJO_SS)
        elif key == ENE_CA:
            info = self.__get(AZUL_CA, ROJO_CA)
        elif key == ENE_HP:
            info = self.__get(AZUL_HP, ROJO_HP)

        else:
            print "Error: Clave Invalida " + key
            info = None

        return info


    def __manejar_aciones(self):
        """
            Funcion que sirver para manejar el conjunto de aciones definidas
            por la IA y convertirlas en Datos
        """
        #mientras haya eventos sin procesar
        while len(self.__eventos) > 0:
            evt = self.__eventos.pop()

            if evt.type == MOVER_E:
                ang = self.get(BOT_BA)
                dx = cos(ang) * SPEED
                dy = sin(ang) * SPEED
                if evt.action == MOVER_ADELANTE:
                    self.__inc(ROJO_X, AZUL_X, dx)
                    self.__inc(ROJO_Y, AZUL_Y, dy)
                elif evt.action == MOVER_ATRAS:
                    self.__inc(ROJO_X, AZUL_X, -dx)
                    self.__inc(ROJO_Y, AZUL_Y, -dy)

            elif evt.type == GIRAR_E:
                pass

            elif evt.type == GIRAR_BASE_E:
                pass

            elif evt.type == GIRAR_CANON_E:
                pass

            elif evt.type == ATACAR_E:
                pass

        #girar la base del tanke
        #inc = self.aciones['BASE_GIRO']
        #if self.aciones['GIRAR_BASE'] == ISO_IZQ:
        #    self.__inc(ROJO_BASE_ANG, AZUL_BASE_ANG, inc)

        #elif self.aciones['GIRAR_BASE'] == ISO_DER:
        #    self.__inc(ROJO_BASE_ANG, AZUL_BASE_ANG, -inc)

        #girar el canon del tanke
        #inc = self.aciones['CANON_GIRO']
        #if self.aciones['GIRAR_CANON'] == ISO_IZQ:
        #    self.__inc(ROJO_BASE_ANG, AZUL_BASE_ANG, -inc)

        #elif self.aciones['GIRAR_CANON'] == ISO_DER:
        #    self.__inc(ROJO_CANON_ANG, AZUL_CANON_ANG, -inc)

        #mover el tanke
        #ang = self.get(BOT_BA)
        #dx = cos(ang) * SPEED
        #dy = sin(ang) * SPEED

        #if self.aciones['MOVER'] == ISO_ADELANTE:
        #    self.__inc(ROJO_X, AZUL_X, dx)
        #    self.__inc(ROJO_Y, AZUL_Y, dy)

        #elif self.aciones['MOVER'] == ISO_ATRAS:
        #    self.__inc(ROJO_X, AZUL_X, -dx)
        #    self.__inc(ROJO_Y, AZUL_Y, -dy)
        #atacar


    def __recivir_datos(self):
        """
            Funcion para recibir los datos del servidor
        """
        try:
            data = self.__socket.recv(BUFF_SIZE)
            self.__socket.settimeout(1.0)
        except:
            data = None

        if data != None:
            self.__data = json.loads(data)

        else:
            #el servidor se ha desconectado, finaliza la conecion
            print "Resultado: " + self.__data[SERVER_MENSAJE]
            self.__finalizar_conecion()
        print '<- recv'


    def __enviar_datos(self):
        """
            Funciones para enviar los datos al servidor
        """
        data = json.dumps(self.__data)
        self.__socket.send(data)
        print 'send ->'


    def __finalizar_conecion(self):
        """
            Finaliza la conecion con el servidor
        """
        self.__conectado = False


    def run(self):
        """
            Metodo que hace correr al bot
        """
        while self.__conectado:
            self.__borrar_aciones()
            self.__recivir_datos()
            self.update()
            self.__manejar_aciones()
            self.__enviar_datos()
            #compruebo el estado del servidor
            self.__conectado = self.__data[SERVER_STATUS]


