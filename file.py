arquivo = open("arquivo.txt")

arquivoCompleto = arquivo.read()
print(arquivoCompleto)

linhas = arquivo.readlines()

for linha in linhas:
    print(linha)

arquivo.close()