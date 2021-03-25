import csv

# в книге не было encoding='utf-8' без нее не работает на русском тексте

with open("st.csv", "r", encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
