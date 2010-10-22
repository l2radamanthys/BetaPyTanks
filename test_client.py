#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.cliente import Cliente
from src.constantes import DEF_HOST, DEF_CLIENT_PORT

if __name__ == '__main__':
    c = Cliente(DEF_HOST, DEF_CLIENT_PORT)
    c.run()
    raw_input('\nPrecione Enter para salir...')
