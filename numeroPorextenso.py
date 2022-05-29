
from unicodedata import digit


def numeroPorExtenso(numero):

    escrita = {
        '0' : {'unidade' : '', 'dezena' : '', 'centena' : ''},
        '1' : {'unidade' : 'um', 'dezena' : 'dez', 'centena' : 'cento'},
        '2' : {'unidade' : 'dois', 'dezena' : 'vinte', 'centena' : 'duzentos'},
        '3' : {'unidade' : 'tres', 'dezena' : 'trinta', 'centena' : 'trezentos'},
        '4' : {'unidade' : 'quatro', 'dezena' : 'quarenta', 'centena' : 'quatrocentos'},
        '5' : {'unidade' : 'cinco', 'dezena' : 'cinquenta', 'centena' : 'quinhentos'},
        '6' : {'unidade' : 'seis', 'dezena' : 'sessenta', 'centena' : 'seiscentos'},
        '7' : {'unidade' : 'sete', 'dezena' : 'setenta', 'centena' : 'setecentos'},
        '8' : {'unidade' : 'oito', 'dezena' : 'oitenta', 'centena' : 'oitocentos'},
        '9' : {'unidade' : 'nove', 'dezena' : 'noventa', 'centena' : 'novecentos'},
    }
    unidade = ''
    numeroPE = []
    casa = 1
    centavos = False

    for digito in str(numero)[::-1]:

        if digito == '.': centavos = True; casa = 1; continue
        if (unidade == '0' and digito == '0') or digito == '0': casa += 1; continue
        if casa%3 == 1 and (casa > 3 and casa < 7): numeroPE.append('mil')
        if casa%3 == 1 and (casa > 6 and casa < 10): numeroPE.append('milhao')
        
        if casa%3 == 0:
            try:
                if numeroPE[-1]: numeroPE.append('e'); numeroPE.append(escrita[digito]['centena'])
            except IndexError:
                if digito == '1': numeroPE.append('cem')
                else : numeroPE.append(escrita[digito]['centena'])
                numeroPE.append('e')
                
        if casa%3 == 1: unidade = digito
        if casa%3 == 2:
            if digito != '1' and unidade != '0': numeroPE.append(escrita[unidade]["unidade"])
            if digit == '0': casa+=1; continue
            if digito == '1':
                if unidade == '1': numeroPE.append('onze')
                if unidade == '2': numeroPE.append('doze')
                if unidade == '3': numeroPE.append('treze')
                if unidade == '4': numeroPE.append('catorze')
                if unidade == '5': numeroPE.append('quinze')
                if unidade == '6': numeroPE.append('dezeseis')
                if unidade == '7': numeroPE.append('dezesste')
                if unidade == '8': numeroPE.append('dezoito')
                if unidade == '9': numeroPE.append('deznove')
            
                casa+=1; continue

            numeroPE.append('e')
            numeroPE.append(escrita[digito]["dezena"])
        
        casa += 1

    else:
        if (casa-1)%3 == 1: numeroPE.append(escrita[unidade]['unidade'])

    if centavos : numeroPE.append('centavos')
    
    return(' '.join(numeroPE[::-1]))

numero_por_extenso = numeroPorExtenso(input())
print(numero_por_extenso)
