#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Conjunto de constantes del juego
    version: 0.0.3
"""

#--------------------- Datos de conecion por defecto -------------------------
DEF_HOST = '127.0.0.1'  #host del servidor por defecto
DEF_BOT_PORT = 1111     #puerto de conecion para los bots por defecto
DEF_CLIENT_PORT = 2222  #puerto de conecion para los clientes por defecto
BUFF_SIZE = 2048       #tamanio del buff en bites
UPDATE_SPEED = 0.0

#--------------------- Datos de Pantalla (Resolucion)-------------------------
ANCHO = 800
ALTO = 600
RESOLUCION = (ANCHO, ALTO)
MARG_SUP = 40
MARG_ISQ = 40
MARG_DER = ANCHO - 40
MARG_INF = ALTO - 40

#----------------------- Constantes del Juego --------------------------------
LIFE_INI = 5    #define el valor incial de vida de los bots, por defecto es 3
SPEED = 5       #velocidad de movimiento de los tankes
SHOT_SPEED = 10 #velocidad del disparo
TANK_RADIO = 30 #para el control de coliciontes
SHOT_RADIO = 3

#-------------------------- Direciones Validas -------------------------------
ISO_NONE = 0        #ninguna
ISO_IZQ = 1         #izquierda
ISO_DER = 2         #derecha
ISO_ADELANTE = 3    #adelante
ISO_ATRAS = 4       #atras


#----------------------- Identificadores varios-------------------------------
ROJO = 0
AZUL = 1

#identificadores del tanke Rojo
ROJO_X = 'ROJO_X'
ROJO_Y = 'ROJO_Y'
ROJO_BASE_ANG = 'ROJO_BASE_ANG'
ROJO_CANON_ANG = 'ROJO_CANON_ANG'

ROJO_SHOT_X = 'ROJO_SHOT_X'
ROJO_SHOT_Y = 'ROJO_SHOT_Y'
ROJO_SHOT_ANGLE = 'ROJO_SHOT_ANGLE'
ROJO_SHOT_STATUS = 'ROJO_SHOT_STATUS'

ROJO_LIFE = 'ROJO_LIFE'
ROJO_NAME = 'ROJO_NAME'

#identificadores del tanke Azul
AZUL_X = 'AZUL_X'
AZUL_Y = 'AZUL_Y'
AZUL_BASE_ANG = 'AZUL_BASE_ANG'
AZUL_CANON_ANG = 'AZUL_CANON_ANG'

AZUL_SHOT_X = 'AZUL_SHOT_X'
AZUL_SHOT_Y = 'AZUL_SHOT_Y'
AZUL_SHOT_ANGLE = 'AZUL_SHOT_ANGLE'
AZUL_SHOT_STATUS = 'AZUL_SHOT_STATUS'

AZUL_LIFE = 'AZUL_LIFE'
AZUL_NAME = 'AZUL_NAME'

#estado de la conecion del servidor
SERVER_STATUS = 'SERVER_STATUS'
SERVER_MENSAJE = 'SERVER_MENSAJE'

