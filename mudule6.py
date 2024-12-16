import os
os.system('cls')

fotbolls_spelare = ["Zlatan, Ronaldo, Messi, Neymar, William, Tiago Silva,"]

fotbolls_spelare[2]= "Pessi"

ny_fotbolls_spelare = input("lägg till en fotbolls spelare:")
fotbolls_spelare.append(ny_fotbolls_spelare)

index_to_remove = int(input("vilken vill du ta bort (0 till {})? ".format(len(fotbolls_spelare) - 1)))

if 0 <= index_to_remove < len(fotbolls_spelare):
    bortagen_fotbolls_spelare = fotbolls_spelare.pop(index_to_remove)
    print("{bortagen_fotbolls_spelare} är nu inte med i listan.")

print("Upptaterad lista") 
for fotbolls_spelare in fotbolls_spelare:
    print(fotbolls_spelare)

    print("Numbers of names:", len(fotbolls_spelare))