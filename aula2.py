# \r\n -> CRLF   \r\n - Quebra de linha
# \n ->  Utilizado mo Sistema Linux - quebra de linha.

# sep='' - Argumento separador nomeado
# end='' - Final de linha, quebra ou insere um caractere

print(12, 34, sep="-", end='#')   # Argumentos não nomeados que ficam entre os parênteses
print(56, 78, sep='-', end='\n')   # Estou passamos vários argumentos e quero a função print exiba no ambiente virtual
print(9, 10, sep='-', end='\n')

