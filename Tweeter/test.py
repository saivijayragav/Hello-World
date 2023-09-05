file = open("harrypotter3.txt", 'r', encoding='utf-8')
f = file.readlines()
#filew = open("harrypotter3.txt", 'w', encoding="utf-8")
spells = [
    "Accio", "Aguamenti", "Alohomora", "Anapneo", "Aparecium", "Avada Kedavra", "Avifors", "Avis", "Colloportus",
    "Confringo", "Confundus", "Crucio", "Defodio", "Deletrius", "Densaugeo", "Depulso", "Descendo", "Diffindo",
    "Dissendium", "Duro", "Engorgio", "Episkey", "Erecto", "Evanesco", "Expecto Patronum", "Expelliarmus", "Expulso",
    "Ferula", "Fidelius Charm", "Finite Incantatem", "Flagrate", "Flipendo", "Furnunculus", "Geminio", "Glisseo",
    "Homorphus", "Horcrux", "Impedimenta", "Imperio", "Impervius", "Incarcerous", "Incendio", "Langlock",
    "Legilimens", "Levicorpus", "Liberacorpus", "Lumos", "Lumos Solem", "Morsmordre", "Muffliato", "Nox", "Obliviate",
    "Orchideous", "Petrificus Totalus", "Point Me", "Portus", "Prior Incantato", "Protego", "Reducto", "Relashio",
    "Rennervate", "Reparo", "Repello Muggletum", "Repello Inimicum", "Revelio", "Rictusempra", "Ridikkulus",
    "Salvio Hexia", "Scourgify", "Sectumsempra", "Serpensortia", "Silencio", "Sonorus", "Specialis Revelio",
    "Stupefy", "Tarantallegra", "Tergeo", "Unbreakable Vow", "Ventus", "Verdimillious", "Wingardium Leviosa", "Expulso", "Mucus and Nauseam", "Pestis Incendium", "Flagrante", "Petrificus Totalus", "Furnunculus", "Geminio", "Calvorio", "Imperio", "Locomotor Wibbly", "Locomotor Mortis", "Reducto", "Sectumsempra", "Slugulus Eructo", "Mimble Wimble"
]

print(len(spells))
count = 0
spelll = [x + 'V' for x in spells]
for i in range(len(f)):
    if "Harry Potted" in f[i]:
        print(i)
print(count)
'''for x in range(len(f)):
    filew.write(f[x])
filew.close()'''