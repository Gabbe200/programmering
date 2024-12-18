import os
os.system('cls')



Fotboll_spelaren = {
    "fotbolls lag": "Chelsea",
    "spelare": "Cole palmer",
    "position" : "central offensiv mittfältare",
    "födelse år" : "2002",
}
print(Fotboll_spelaren["position"])

Fotboll_spelare = [
    {
        "fotbolls lag": "Chelsea"
        "spelare": "Noni Madueke",
        "position" : "Höger ytter",
        "födelse år" : "2002",
    },
    {
        "fotbolls lag": "Chelsea"
        "spelare": "Malo Gusto",
        "position" : "Högerback",
        "födelse år" : "2003",
    },
    {
        "fotbolls lag": "Aresenal"
        "spelare": "Bukayo Saka",
        "position" : "Höger ytter",
        "födelse år" : "2001",
    },
]

print(Fotboll_spelare[0]['fotbolls lag'])

while True:
    for spelare in Fotboll_spelare:
        print(spelare)

    delete = int(input("Vänligen tabort en från listan"))
    
    add = int(input("Vänligen lägg till en till listan"))