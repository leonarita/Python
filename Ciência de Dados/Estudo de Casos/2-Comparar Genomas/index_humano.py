entrada = open('human.fasta').read()
saida = open("18s_humano.html", "w")

cont = {}

# zera todas as quantidades de pares de nucleotídeos
for i in ["A", "T", "C", "G"]:
    for j in ["A", "T", "C", "G"]:
        cont[i + j] = 0
# print(cont)

# Remove as quebras de linhas do conteudo do arquivo
entrada = entrada.replace("\n", "")

# Conta a quantidade de cada par de nucleotídeos
for k in range(len(entrada)-1):
    cont[entrada[k] + entrada[k+1]] += 1

i = 1

saida.write('<div>')

for k in cont:
    transparencia = cont[k] / max(cont.values())

    saida.write("<div style='width:100px; border:1px solid #111; height:100px; float:left; color:#fff;"
                "background-color:rgba(0, 0, 255, " + str(transparencia) + "')>" + k + "</div>")

    if i % 4 == 0:
        saida.write("<div style='clear:both'></div>")

    i += 1

saida.close()
