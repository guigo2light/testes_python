veni = open("veni.txt","r")
novo_veni = open("novo_veni.txt", "a")
for linha in veni.readlines():
        novo_veni.write(linha)
veni.close()
novo_veni.close()
