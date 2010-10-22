#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
lib_name.py
=============
    Version: 0.0.3

    Autor: Ricardo D. Quiroga->L2Radamanthys

    Fecha: 05 de Octubre de 2010

    E-mail:
        l2radamanthys@gmail.com
        l2radamanthys@saltalug.org.ar
        ricardoquiroga.dev@gmail.com

    SitioWeb:
        http://www.l2radamanthys.com.ar
        http://l2radamanthys.blogspot.com

    Descripcion:


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

__version__ = "0.0.5"
__autor__ = "Ricardo D. Quiroga - L2Radamanthys  l2radamanthys@gmailcom"
__date__ = "05 de Octubre de 2010"
__copyright__ = "Copyright (c) 2010 Ricardo D. Quiroga"
__license__ = "GPL2"


import socket
import time
from random import randint
from sys import exit
import json
from thread import start_new_thread

from constantes import *
from enginer import GameEnginer


class Server:
    def __init__(self, host=DEF_HOST, bot_port=DEF_BOT_PORT, client_port=DEF_CLIENT_PORT):
        """
        """
        #dicionario que contendra un identificador a todos los clientes
        self.__clientes = {}

        #dicionario con toda la informacion y status de los tankes
        self.__data = DEF_DATA

        #conecion definido para los bots
        self.bots_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #conecion definida para los clientes
        self.clients_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.abierto = True  #avisa si el servidor sigue aceptando coneciones
        self.loop = True  #correr el servidor

        print "Esperando coneciones de los Bots "

        #Espera a que los bots se conecten
        self.bots_socket.bind((host, bot_port))
        self.bots_socket.listen(2)
        self.__conectar_bots()
        print "ok"

        #Activa la conecion de los clientes
        self.clients_socket.bind((host, client_port))
        self.clients_socket.listen(1)

        #control del juego
        self.game_enginer = GameEnginer()

        #lanzo en un hilo la escuha de nuevas coneciones
        start_new_thread(self.__escuchar_clientes, ())


    def __conectar_bots(self):
        """
        """
        self.red_socket, addr = self.bots_socket.accept()
        self.red_socket.send('SERVER MSJ: Tu Seras el Bot Rojo....\n')
        red_name = self.red_socket.recv(BUFF_SIZE)
        print "Bot Rojo " + red_name + " -> Conectado"
        self.__data[ROJO_NAME] = red_name

        self.blue_socket, addr = self.bots_socket.accept()
        self.blue_socket.send('SERVER MSJ: Tu Seras el Bot Azul...\n')
        blue_name = self.blue_socket.recv(BUFF_SIZE)
        print "Bot Azul" + blue_name + " -> Conectado"
        self.__data[AZUL_NAME] = blue_name

        #cierra la conecion para evitar que otros bots se conecten
        self.bots_socket.close()

        #incializa la informacion de anbos bots
        self.__data[ROJO_X] = 200
        self.__data[ROJO_Y] = 200
        self.__data[AZUL_X] = 400
        self.__data[AZUL_Y] = 200



    def __escuchar_clientes(self):
        """
            Escucha la conecion de nuevos clientes
        """
        #acepta coneciones mientras el servidor este abierto
        id = 0
        while self.abierto:
            self.__clientes[id], addr = self.clients_socket.accept()
            print "Nueva Conecion -> " + str(addr)
            id += 1
        self.clients_socket.close()


    def enviar_datos(self):
        """
            Envian toda la informacion a los bots y clientes.
        """
        #lista que almacenara los clientes desconectados
        borrar = []

        #utilizamos la libreria Json para empaquetar la informacion en un str
        data = json.dumps(self.__data)

        #envio de la informacion a los bots
        self.red_socket.send(data)
        self.blue_socket.send(data)

        self.abierto = False
        #envio de la informacion a los clientes
        for id, cliente in self.__clientes.iteritems():
            try:
                #intenta enviar la informacion al cliente
                cliente.send(data)
            except:
                #caso que el envio falle borrara la conecion con el cliente
                borrar.append(id)

        #eliminamos todas las coneciones que dieron error
        for id in borrar:
            print "se perdio la conecion con.."
            del(self.__clientes[id])
        print 'send ->'
        self.abierto = True


    def recivir_datos(self):
        """
            Intenta actualizar la informacion de la posicion y el estado de los
            bots, en caso de caso que dicha actualizacion falle se usaran los
            datos que existian asimilando que el tanke no realizo acion alguna
        """
        try:
            data_rojo = json.loads(self.red_socket.recv(BUFF_SIZE))
        except:
            data_rojo = self.__data.copy()
        try:
            data_azul = json.loads(self.blue_socket.recv(BUFF_SIZE))
        except:
            data_azul = self.__data.copy()
        print '<- recv'
        return data_rojo, data_azul


    def parse(self, data):
        """
        """
        data_rojo, data_azul = data
        self.game_enginer.parse_red_data(data_rojo)
        self.game_enginer.parse_red_data(data_azul)
        self.__data = self.game_enginer.get_data()


    def enviar_msj(self, data):
        """
        """
        pass


    def run(self):
        """
        """
        print "Servidor corriendo...."
        raw_input('Precione Enter para iniciar Juego...')
        print "Clientes conectados: %d \n" %len(self.__clientes)
        while self.loop:
            self.enviar_datos()
            time.sleep(UPDATE_SPEED)
            data = self.recivir_datos()
            self.parse(data)



