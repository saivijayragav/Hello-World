files = [open("harry1.txt", 'r', encoding="utf-8"), open("harry2.txt", 'r', encoding="utf-8"),open("harry3.txt", 'r', encoding="utf-8"),
         open("harry4.txt", 'r', encoding="utf-8"), open("harry5.txt", 'r', encoding="utf-8"), open("harry6.txt", 'r', encoding="utf-8"),
         open("harry7.txt", 'r', encoding="utf-8"),]
filew = open("harrypotter.txt", 'w', encoding="utf-8")
for i in range(len(files)):
    file = files[i]
    f = file.readlines()
    for x in f:
        filew.write(x)
