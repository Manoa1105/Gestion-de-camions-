materiaux_fixes = ["gravillon", "sable fin", "brique", "4/7", "moellon", "gros sable"]

def saisir_entier(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("  ❌ Entrée invalide. Réessaye avec un nombre.")

def afficher_materiaux_fixes():
    print("\n📋 Matériaux disponibles :")
    for i, mat in enumerate(materiaux_fixes, 1):
        print(f"  [{i}] {mat}")

def choisir_materiaux_fixes():
    afficher_materiaux_fixes()
    selection = input("\n🔢 Entrez les numéros des matériaux utilisés (ex: 1,3,6) : ")
    numeros = [s.strip() for s in selection.split(",")]
    choisis = []

    for num in numeros:
        if num.isdigit():
            index = int(num) - 1
            if 0 <= index < len(materiaux_fixes):
                choisis.append(materiaux_fixes[index])
            else:
                print(f"  ⚠️ Numéro {num} invalide.")
        else:
            print(f"  ⚠️ '{num}' n’est pas un nombre valide.")

    return choisis

def saisir_materiaux():
    materiaux = {}

    # Choix des matériaux fixes
    selection_fixes = choisir_materiaux_fixes()
    for mat in selection_fixes:
        prix = saisir_entier(f"    - Prix pour {mat} : ")
        materiaux[mat] = prix

    # Ajouter des matériaux personnalisés
    ajouter = input("\n➕ Ajouter d'autres matériaux ? (o/n) : ").lower()
    if ajouter == 'o':
        nb = saisir_entier("    Combien ? ")
        for _ in range(nb):
            nom = input("      - Nom du nouveau matériau : ")
            prix = saisir_entier(f"        Prix pour {nom} : ")
            materiaux[nom] = prix

    return materiaux

def saisir_depenses_jour():
    print("  >> Saisie des matériaux :")
    materiaux = saisir_materiaux()
    main_oeuvre = sum(materiaux.values())

    print("\n  >> Saisie des repas :")
    repas_midi = saisir_entier("    - Prix repas midi (Ar) : ")
    repas_soir = saisir_entier("    - Prix repas soir (Ar) : ")
    repas_total = repas_midi + repas_soir

    reste = main_oeuvre - repas_total

    return {
        "materiaux": materiaux,
        "main_oeuvre": main_oeuvre,
        "repas": repas_total,
        "reste": reste
    }

def afficher_resultats(resultats):
    print("\n============================")
    print(" RÉSUMÉ DES DÉPENSES HEBDO")
    print("============================")

    total_general_reste = 0

    for camion, jours in resultats.items():
        print(f"\n--- {camion} ---")
        total_main = total_repas = total_reste = 0
        for jour, data in jours.items():
            print(f"{jour}:")
            print(f"  Main d'œuvre : {data['main_oeuvre']} Ar")
            print(f"  Repas        : {data['repas']} Ar")
            print(f"  Reste        : {data['reste']} Ar")
            total_main += data['main_oeuvre']
            total_repas += data['repas']
            total_reste += data['reste']

        # ✅ DIMANCHE : total des restes pour ce camion
        print(f"\n🟩 DIMANCHE - Total des Restes (Lun-Sam) : {total_reste} Ar")

        print(f"\n🧮 TOTAL SEMAINE pour {camion} :")
        print(f"  Main d'œuvre : {total_main} Ar")
        print(f"  Repas        : {total_repas} Ar")
        print(f"  Reste        : {total_reste} Ar")

        total_general_reste += total_reste

    print("\n============================")
    print(f"📊 TOTAL GÉNÉRAL DES RESTES (DIMANCHE) : {total_general_reste} Ar")
    print("============================\n")

def main():
    jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    camions = ["Camion 1", "Camion 2", "Camion 3", "Camion 4"]
    resultats = {}

    for camion in camions:
        print(f"\n==============================")
        print(f" Saisie des dépenses - {camion}")
        print(f"==============================")
        resultats[camion] = {}
        for jour in jours:
            print(f"\n--- {jour} ---")
            resultats[camion][jour] = saisir_depenses_jour()

    afficher_resultats(resultats)

if __name__ == "__main__":
    main()
