#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from src.bot import Bot
from src.constantes import *

class MiBot(Bot):
    """
        Bot de pruebas
    """
    def __init__(self, host, port):
        Bot.__init__(self, 'test bot', host, port)

    def update(self):
        self.girar_canon(ISO_DER)


if __name__ == '__main__':
    mi_ia = MiBot(DEF_HOST, DEF_BOT_PORT)
    mi_ia.run()
