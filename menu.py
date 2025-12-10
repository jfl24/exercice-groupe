def afficher_plats_principaux():
    print("=== Plats Principaux ===")
    print("- Poulet rôti et légumes grillés")
    print("- Lasagnes maison")
    print("- Saumon grillé avec riz basmati")

def main():
    print("=== MENU DU RESTAURANT ===")
    afficher_plats_principaux()

if __name__ == "__main__":
    main()

def afficher_entrees():
    entrees = ["Salade ", "Ailes de poulet", "Tartare"]
    print("====ENTRÉE====")
    for i, entree in enumerate(entrees, 1):
        print(f"{i}.{entree}")

afficher_entrees()
