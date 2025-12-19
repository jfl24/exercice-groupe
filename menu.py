def afficher_entrees():
    entrees = ["Salade ", "Ailes de poulet", "Tartare"]
    print("====ENTRÉE====")
    for i, entree in enumerate(entrees, 1):
        print(f"{i}.{entree}")
        
def afficher_plats_principaux():
    print("\n=== Plats Principaux ===")
    print("1. Poulet rôti et légumes grillés")
    print("2. Lasagnes maison")
    print("3. Saumon grillé avec riz basmati")

def afficher_desserts():
    print("\n=== DESSERTS ===")
    print("1. Tiramisu")
    print("2. Crème brûlée")
    print("3. Tarte aux pommes")

def main():
    print("=== MENU DU RESTAURANT ===\n")
    afficher_entrees()
    afficher_plats_principaux()
    afficher_desserts()

if __name__ == "__main__":
    main()



