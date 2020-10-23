# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:38:08 2020

@author: Omar
"""

from caso_D import caso_D
from caso_L import caso_L

ret_D = caso_D()
ret_L = caso_L()

"""
de la 0 a la 34 en combinación muerta no cumple
desde los 0 hasta los 90 metros fortalecer

de la 0 a la 50 y de la 149 a la 166 no cumple en viva
desde los 0 hasta los 130 metros
desde los 37 hasta los 127 metros
"""
#Peso propio
ret_D.ensamblar_sistema()
ret_D.resolver_sistema()
f_D = ret_D.recuperar_fuerzas()

#Carga Viva
ret_L.ensamblar_sistema()
ret_L.resolver_sistema()
f_L = ret_L.recuperar_fuerzas()

#Combinaciones de carga
f_1 = 1.4*f_D           #Combinacion 1
f_2 = 1.2*f_D + 1.6*f_L #Combinacion 2


# Calcular factores 
cumple_combinacion_1 = ret_D.chequear_diseño(f_1)
cumple_combinacion_2 = ret_L.chequear_diseño(f_2)


peso_D = ret_D.calcular_peso_total()

if cumple_combinacion_1:
    print("Combinación de carga 1 : cumple ")
else:
    print("Combinación de carga 1 : NO cumple ")

if cumple_combinacion_2:
    print("Combinación de carga 2 : cumple ")
else:
    print("Combinación de carga 2 : NO cumple ")


if cumple_combinacion_1 and cumple_combinacion_2:
    print(f"Peso total = {peso_D}")


    
    
    
    
    
    
    
    
    
    
    
    
    
    