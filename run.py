#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from src.server import Server
from src.constantes import DEF_HOST, DEF_BOT_PORT, DEF_CLIENT_PORT

def main():
    os.system('clear')
    host = DEF_HOST
    bot_port = DEF_BOT_PORT
    client_port = DEF_CLIENT_PORT

    if len(sys.argv) == 2:
        host = sys.argv[1]

    if len(sys.argv) == 3:
        host = sys.argv[1]
        bot_port  = int(sys.argv[2])

    elif len(sys.argv) == 4:
        host = sys.argv[1]
        bot_port  = int(sys.argv[2])
        client_port = int(sys.argv[3])

    else:
        print "parametros invalidos"

    print """
    ---------------------------------
            Iniciando Servidor
    ---------------------------------
    SERVER HOST     %s
    BOT PORT        %s
    CLIENT PORT     %s
    ---------------------------------
    """%(host, bot_port, client_port)

    mi_servidor = Server(host, bot_port, client_port)
    raw_input('Precione Enter - Para Comenzar')
    mi_servidor.run()


if __name__ == '__main__':
    main()
