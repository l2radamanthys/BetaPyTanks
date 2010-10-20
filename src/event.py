#!/usr/bin/env python
# -*- coding: utf-8 -*-


from constantes import *


class Event:
    def __init__(self, type=NONE_E, action=NONE_ACTION):
        self.type = type
        self.action = action

    def __eq__(self, evt):
        if self.type == evt.type:
            return True
        else:
            return False


    def __str__(self):
        return "Event - %d-%d" %(self.tipo, self.acion)


class EventQueue:
    def __init__(self):
        self.__eventos = []


    def push(self, evt):
        if not(self._in(evt)):
            self.__eventos.append(evt)
            return evt


    def pop(self, id=0):
        return self.__eventos.pop(0)


    def head(self):
        return self.__eventos[0]


    def tail(self):
        return self.__eventos[-1]


    def __len__(self):
        return len(self.__eventos)


    def _in(self, evt):
        return evt in self.__eventos


    def pos(self, evt):
        return self.__eventos.index(evt)


    def clear(self):
        self.__eventos = []
