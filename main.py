import unittest

UNIDADES = {
    'cero' : 0,
    'uno' : 1,
    'dos' : 2,
    'tres' : 3,
    'cuatro' : 4,
    'cinco' : 5,
    'seis' : 6,
    'siete' : 7,
    'ocho' : 8,
    'nueve' : 9
}

DECENAS_DIEZ = {
    'diez' : 10,
    'once' : 11,
    'doce' : 12,
    'trece' : 13,
    'catorce' : 14,
    'quince' : 15,
    'dieciseis' : 16,
    'diecisiete' : 17,
    'dieciocho' : 18,
    'diecinueve' : 19
}
DECENAS_VEINTE = {
    'veinte' : 20,
    'veintiuno' : 21,
    'veintidos' : 22,
    'veintitres' : 23,
    'veinticuatro' : 24,
    'veinticinco' : 25,
    'veintiseis' : 26,
    'veintisiete' : 27,
    'veintiocho' : 28,
    'veintinueve' : 29
}


DIEZ_DIEZ = {
    'diez' : 10,
    'veinte' : 20,
    'treinta' : 30,
    'cuarenta' : 40,
    'cincuenta' : 50,
    'sesenta' : 60,
    'setenta' : 70,
    'ochenta' : 80,
    'noventa' : 90
}

CIENTOS = {
    '_' : '_',
    'cien' : 100,
    'ciento' : 100,
    'doscientos' : 200,
    'trescientos' : 300,
    'cuatroscientos' : 400,
    'quinientos' : 500,
    'seiscientos' : 600,
    'setecientos' : 700,
    'ochocientos' : 800,
    'novecientos' : 900
}

def unidades(numero_str):
    return UNIDADES[numero_str]

def decenas_diez(numero_str):
    return DECENAS_DIEZ[numero_str]

def decenas_veinte(numero_str):
    return DECENAS_VEINTE[numero_str]

def resto_decenas_unidad(numero_str):
    numero_int = 0
    if type(numero_str) == str:
        numero_str = numero_str.split(' ')
    numero_int += DIEZ_DIEZ[numero_str[0]]
    numero_int += unidades(numero_str[2])
    return numero_int

def centenas_decena_unidad(numero_str):
    numero_int = 0
    if type(numero_str) == str:
        numero_str = numero_str.split(' ')
    numero_int += CIENTOS[numero_str[0]]
    numero_int += resto_decenas_unidad(numero_str[1:])
    return numero_int

def centenas_decena(numero_str):
    numero_int = 0
    if type(numero_str) == str:
        numero_str = numero_str.split(' ')
    numero_int += centena(numero_str[0])
    numero_int += decenas_cero(numero_str[1])
    return numero_int

def centena(numero_str):
    return CIENTOS[numero_str]

def decenas_cero(numero_str):
    return DIEZ_DIEZ[numero_str]

def calcular(numero_str):
    numero_int = 0
    if type(numero_str) == str:
        numero_str = numero_str.split(' ')
    if len(numero_str) == 1:
        if numero_str[0] in UNIDADES:
            return unidades(numero_str[0])
        elif numero_str[0] in DIEZ_DIEZ:
            return decenas_cero(numero_str[0])
        elif numero_str[0] in DECENAS_VEINTE:
            return decenas_veinte(numero_str[0])        
        elif numero_str[0] in DECENAS_DIEZ:
            return decenas_diez(numero_str[0])
        elif numero_str[0] == CIENTOS[1]:
            return CIENTOS[1]

    elif len(numero_str) == 2:
        if numero_str[0] in CIENTOS:
            numero_int += centena(numero_str[0])
        elif numero_str[0] in DIEZ_DIEZ:
            numero_int += decenas_diez(numero_str[0])
        if numero_str[1] in UNIDADES:
            numero_int += unidades(numero_str[1])
        elif numero_str[1] in DECENAS_DIEZ:
            numero_int += decenas_diez(numero_str[1])
        elif numero_str[1] in DECENAS_VEINTE:
            numero_int += decenas_veinte(numero_str[1])
        return numero_int

    elif len(numero_str) == 3:
        if numero_str[0] in DIEZ_DIEZ:
            numero_int += decenas_cero(numero_str[0])
        if numero_str[2] in UNIDADES:
            numero_int += unidades(numero_str[2])
        return numero_int

    elif len(numero_str) == 4:
        if numero_str[0] in CIENTOS:
            numero_int += centena(numero_str[0])
        if numero_str[1] in DIEZ_DIEZ:
            numero_int += decenas_cero(numero_str[1])
        if numero_str[3] in UNIDADES:
            numero_int += unidades(numero_str[3])
        return numero_int
    return "ERROR"


class TestLetrasANumeros(unittest.TestCase):

    def test_unidades(self):
        numero = 'uno'
        self.assertEqual(unidades(numero), 1)
        numero = 'tres'
        self.assertEqual(unidades(numero), 3)
        numero = 'nueve'
        self.assertEqual(unidades(numero), 9)


    def test_decena_diez(self):
        numero = 'quince'
        self.assertEqual(decenas_diez(numero), 15)
        numero = 'diecisiete'
        self.assertEqual(decenas_diez(numero), 17)
        numero = 'diecinueve'
        self.assertEqual(decenas_diez(numero), 19)

    def test_decena_veinte(self):
        numero = 'veintitres'
        self.assertEqual(decenas_veinte(numero), 23)
        numero = 'veintiseis'
        self.assertEqual(decenas_veinte(numero), 26)
        numero = 'veintiuno'
        self.assertEqual(decenas_veinte(numero), 21)

    def test_menores_cien(self):
        numero = 'treinta y dos'
        self.assertEqual(resto_decenas_unidad(numero), 32)
        numero = 'setenta y tres'
        self.assertEqual(resto_decenas_unidad(numero), 73)
        numero = 'ochenta y nueve'
        self.assertEqual(resto_decenas_unidad(numero), 89)

    def test_decenas_cero(self):
        numero = 'treinta'
        self.assertEqual(decenas_cero(numero), 30)
        numero = 'setenta'
        self.assertEqual(decenas_cero(numero), 70)
        numero = 'ochenta'
        self.assertEqual(decenas_cero(numero), 80)
    
    def test_centenas(self):
        numero = 'ciento sesenta y siete'
        self.assertEqual(centenas_decena_unidad(numero), 167)
        numero = 'setecientos treinta y cinco'
        self.assertEqual(centenas_decena_unidad(numero), 735)
        numero = 'ochocientos noventa y nueve'
        self.assertEqual(centenas_decena_unidad(numero), 899)

    def test_calcular(self):
        numero = 'diez'
        self.assertEqual(calcular(numero), 10)
        numero = 'veinte'
        self.assertEqual(calcular(numero), 20)
        numero = 'cinco'
        self.assertEqual(calcular(numero), 5)
        numero = 'ciento cinco'
        self.assertEqual(calcular(numero), 105)        
        numero = 'doscientos veintitres'
        self.assertEqual(calcular(numero), 223)
        numero = 'setenta y tres'
        self.assertEqual(resto_decenas_unidad(numero), 73)
        numero = 'ochenta y nueve'
        self.assertEqual(resto_decenas_unidad(numero), 89)
        numero = 'doscientos treinta y dos'
        self.assertEqual(calcular(numero), 232)
        numero = 'ciento cuarenta y uno'
        self.assertEqual(calcular(numero), 141)
        numero = 'doscientos cincuenta y dos'
        self.assertEqual(calcular(numero), 252)
        numero = 'novecientos treinta y cinco'
        self.assertEqual(calcular(numero), 935)
        numero = 'treinta y dos'
        self.assertEqual(calcular(numero), 32)

        numero = 'setenta y siete'
        self.assertEqual(calcular(numero), 77)

        numero = 'treinta y dos'
        self.assertEqual(calcular(numero), 32)

        numero = 'ochenta y cuatro'
        self.assertEqual(calcular(numero), 84)

        numero = 'ciento quince'
        self.assertEqual(calcular(numero), 115)

        numero = 'ciento sesenta y siete'
        self.assertEqual(centenas_decena_unidad(numero), 167)
        numero = 'setecientos treinta y cinco'
        self.assertEqual(centenas_decena_unidad(numero), 735)
        numero = 'ochocientos noventa y nueve'
        self.assertEqual(centenas_decena_unidad(numero), 899)
        
        numero = 'novecientos noventa y nueve'
        self.assertEqual(calcular(numero), 999)

if __name__ == '__main__':
    unittest.main()
