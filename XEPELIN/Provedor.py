#!/usr/bin/python
#-*- coding: utf-8 -*-

from Provedor import Provedor
from Factura import Factura
from Provedor import Provedor

class Provedor(Provedor, Factura, Provedor):
    def __init__(self):
        self.Id provedor = None
        self.nombre = None
        self.tel_prov = None
        self.direccion = None

    def Leer_provedor(self, ):

        print("Clase provedor")
        pass

    def Modificar__Provedor(self, ):
        print("Modificar el probedor")
        pass
