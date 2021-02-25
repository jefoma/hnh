# -*- coding: utf-8 -*-

# @autor: Jesus Fontana
class Calculador(object):
    """Clase responsable de realizar todos los cálculos con calculadora"""
    
    def calculation(self, calc):
        """Responsable de recibir el cálculo a realizar, devolviendo
           el resultado o un mensaje de error en caso de falla.

        """
        return self.__calculation_validation(calc=calc)

    def __calculation_validation(self, calc):
        """Responsable de verificar si es posible realizar el cálculo informado"""

        try:
            result = eval(calc)

            return self.__format_result(result=result)
        except (NameError, ZeroDivisionError, SyntaxError, ValueError):
            return 'Erro' 

    def __format_result(self, result):
        """Formatea el resultado en notación científica si es demasiado grande
           y devuelve el valor formateado en tipo de cadena"""

        result = str(result)
        if len(result) > 15:
            result = '{:5.5E}'.format(float(result))
            
        return result
