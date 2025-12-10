def main():
    print("=== MENU DU RESTAURANT ===")

if __name__ == "__main__":
    main()

def afficher_entrees():
    entrees = ["Salade ", "Ailes de poulet", "Tartare"]
    print("====ENTRÉE====")
    for i, entree in enumerate(entrees, 1):
        print(f"{i}.{entree}")

afficher_entrees()