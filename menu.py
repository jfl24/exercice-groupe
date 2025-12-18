def afficher_entrees():
    entrees = ["Salade ", "Ailes de poulet", "Tartare"]
    print("====ENTRÉE====")
    for i, entree in enumerate(entrees, 1):
        print(f"{i}.{entree}")
        
def afficher_plats_principaux():
    print("=== Plats Principaux ===")
    print("- Poulet rôti et légumes grillés")
    print("- Lasagnes maison")
    print("- Saumon grillé avec riz basmati")

def main():
    print("=== MENU DU RESTAURANT ===")
    afficher_entrees()
    afficher_plats_principaux()

if __name__ == "__main__":
    main()

def afficher_desserts():
    print("\n--- DESSERTS ---")
    print("1. Tiramisu")
    print("2. Crème brûlée")
    print("3. Tarte aux pommes")

def main():
    print("=== MENU DU RESTAURANT ===")

    try:
        afficher_entrees()  
    except NameError:
        pass

    try:
        afficher_plats_principaux() 
    except NameError:
        pass

    afficher_desserts()

if __name__ == "__main__":
    main()
