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
THETA = 3       #angulo de giro
SHOT_SPEED = 10 #velocidad del disparo
TANK_RADIO = 30 #para el control de coliciontes
SHOT_RADIO = 3

#-------------------------- Direciones Validas -------------------------------
ISO_NONE = 0        #ninguna
ISO_IZQ = 1         #izquierda
ISO_DER = 2         #derecha
ISO_ADELANTE = 3    #adelante
ISO_ATRAS = 4       #atras


#---------------------- tipos de eventos -------------------------------------
NONE_E = 0
MOVER_E = 1
GIRAR_E = 3
GIRAR_BASE_E = 4
GIRAR_CANON_E = 5
ATACAR_E = 6

NONE_ACTION = 0
MOVER_ATRAS = 1
MOVER_ADELANTE = 2
GIRAR_IZQ = 3
GIRAR_DER = 4
ATACAR = 5

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

#datos por defecto
DEF_DATA = {
    ROJO_X : 100,
    ROJO_Y : 200,
    ROJO_BASE_ANG : 0,
    ROJO_CANON_ANG : 0,
    ROJO_SHOT_X : 0,
    ROJO_SHOT_Y : 0,
    ROJO_SHOT_ANGLE : 0,
    ROJO_SHOT_STATUS : False,
    ROJO_LIFE : 5,
    ROJO_NAME : 'Rojo',

    AZUL_X : 300,
    AZUL_Y : 300,
    AZUL_BASE_ANG : 0,
    AZUL_CANON_ANG : 0,
    AZUL_SHOT_X : 0,
    AZUL_SHOT_Y : 0,
    AZUL_SHOT_ANGLE : 0,
    AZUL_SHOT_STATUS : False,
    AZUL_LIFE : 5,
    AZUL_NAME : 'Azul',

    SERVER_STATUS : True,
    SERVER_MENSAJE : 'NADA'
}
