#!/usr/bin/python
# -*- coding: utf-8 -*-


fich=open("/etc/passwd","r")
longitud = len(fich.readlines())

fich=open("/etc/passwd","r")

while 1:
    informacion = fich.readline()
    usuario =  informacion.split(":") 
    print usuario[0], usuario[-1][:-1]
    if not informacion:
        break

print "Hay ", longitud, "usuarios"

fich.close()

