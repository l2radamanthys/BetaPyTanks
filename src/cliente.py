#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import json

import pygame
from pygame.locals import *

from libs.colores import *
from constantes import *
from tanke import Tank


class Cliente:
    def __init__(self, host, port):
        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUCION)

        self.rojo = Tank('data/imagenes/base.bmp', 'data/imagenes/canon.bmp', ROJO)
        self.azul = Tank('data/imagenes/base.bmp', 'data/imagenes/canon.bmp', AZUL)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.data = DEF_DATA.copy()
        self.a_data = self.data.copy()

        print "------------------------------"
        print "      Conectando Cliente      "
        print "------------------------------"
        print "HOST: %s  (por defecto)" %host
        print "PORT: %d  (por defecto)" %port


    def run(self):
        loop = True
        while loop:
            self.screen.fill(VERDE)

            try:
                buffer = self.sock.recv(BUFF_SIZE)
            except:
                buffer = ""
            #buffer = self.sock.recv(BUFF_SIZE)

            if buffer != "":
                self.a_data = self.data.copy()
                try:
                    self.data = json.loads(buffer)
                except:
                    print buffer + '\n\n'

            else:
                self.data = self.a_data.copy()
                print "Error"

            self.rojo.update(self.data)
            self.azul.update(self.data)

            self.rojo.drawn(self.screen)
            self.azul.drawn(self.screen)

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    loop =False

        pygame.quit()
        self.sock.close()
        print 'Juego Finalizado...\n'
