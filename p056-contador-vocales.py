#p056-contador-vocales.py
# Dada una frase, cuenta vocales, consonantes y otros

print ("\033[2J\033[h", end="")
print ('Dada una frase, cuenta vocales, consonantes y otros\n')

frase = input('Introduce una frase : ').lower()
print(f'\nLa frace a analizar es {frase} y tiene {len(frase)} caracteres')

i= vocal = consonante = otro =0
while i < len(frase):
    c = frase[i]
    if 'a' <= c <= 'z':
        print(' Si')
        if c in 'aeiou':
            vocal += 1
        else:
            consonante += 1
    else:
        print(' No')
        otro += 1
    i+=1

print(f'Vocales: {vocal}\nConsonante: {consonante}\nOtros: {otro}')