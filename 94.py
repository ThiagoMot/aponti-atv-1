d = dict()
d["Nome"] = str(input("Digite o nome: "))
d["Sexo"] = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
d["Idade"] = int(input("Digite a idade: "))
l = list()
f = list()
i = 0
i += d["Idade"]
l.append(d.copy())
if d["Sexo"] == "F":
    f.append(d.copy())
while True:
    q = str(input("Quer continuar? [S/N]: "))
    if q in "Ss":
        d["Nome"] = str(input("Digite o nome: "))
        d["Sexo"] = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
        d["Idade"] = int(input("Digite a idade: "))
        i += d["Idade"]
        if d["Sexo"] == "F":
            f.append(d.copy())
        l.append(d.copy())
        d.clear()
    elif q in "Nn":
        print("Finalizando...")
        break
print(l)
y = i/len(l)
print(f"Foram {len(l)} pessoas cadastradas.")
print(f)
print(f"A media de idade é {i/len(l)}")
for c in l:
    if c["Sexo"] in "Ff":
        print(f"{c["Nome"]} tem {c["Idade"]}")
for j, b in enumerate(l):
    if y < b["Idade"]:
        print(f"Posição {j+1} {b["Nome"]}, {b["Idade"]}")





