import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from langdetect import detect
import pandas as pd
def ouvrir_bdd():
    bdd_location = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv"), ("Fichiers Excel", "*.xlsx")])
    print("Emplacement de la BDD:", bdd_location)
    # Vérifier si un fichier a été sélectionné
    if bdd_location:
        # Extraire l'extension du fichier
        extension = bdd_location.split('.')[-1]

        # Afficher le type de fichier sélectionné
        print("Type de fichier sélectionné:", extension)
    else:
        print("Aucun fichier sélectionné.")


# Fonction pour charger les données
def charger_donnees():
    # Logique pour charger les données
    print("Chargement des données...")

# Fonction pour ouvrir la base de données


# Fonction pour afficher les informations générales
def afficher_infos_generales():
    # Charger les données à partir du fichier sélectionné
    bdd_location = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv"), ("Fichiers Excel", "*.xlsx")])
    if bdd_location:
        # Lire le fichier CSV ou Excel en utilisant pandas
        if bdd_location.endswith('.csv'):
            data = pd.read_csv(bdd_location)
        elif bdd_location.endswith('.xlsx'):
            data = pd.read_excel(bdd_location)
        else:
            print("Format de fichier non pris en charge.")
            return

        # Calculer les informations requises
        langue = detect_language(data)  # Fonction pour détecter la langue des données
        longueur = len(data)
        description_generale = data.describe()  # Description générale des données

        # Afficher les informations dans une boîte de dialogue ou une zone de texte
        messagebox.showinfo("Informations de la base de données", f"Langue : {langue}\nLongueur : {longueur}\nDescription générale :\n{description_generale}")

def detect_language(data):
    # Implémentez votre logique de détection de la langue ici
    # Par exemple, vous pouvez utiliser des bibliothèques comme langdetect
    # Voici un exemple simple pour illustrer :

    return detect(data.iloc[0, 0])  # Détecte la langue du premier texte dans la colonne




# Fonction pour afficher le Word Cloud
def afficher_wordcloud():
    # Logique pour afficher le Word Cloud
    print("Affichage du Word Cloud...")

# Fonction pour afficher les N-Grammes
def afficher_ngram():
    # Logique pour afficher les N-Grammes
    print("Affichage des N-Grammes...")

# Fonction pour appliquer le prétraitement des données
def appliquer_pretraitement():
    # Logique pour appliquer le prétraitement des données
    print("Prétraitement des données appliqué.")

# Fonction pour appliquer la modélisation thématique
def appliquer_modelisation():
    # Logique pour appliquer la modélisation thématique
    print("Modélisation thématique appliquée avec le modèle", var_modele.get())

# Fonction pour appliquer la détection de langage abusif
def appliquer_detection_abus():
    # Logique pour détecter le langage abusif dans le texte saisi
    texte_saisi = entry_texte.get()
    print("Texte saisi :", texte_saisi)
    print("Détection du langage abusif...")

# Fonction pour afficher les mots abusifs
def afficher_mots_abusifs():
    # Logique pour afficher les mots abusifs
    print("Affichage des mots abusifs...")

# Fonction pour afficher les textes abusifs
def afficher_textes_abusifs():
    # Logique pour afficher les textes abusifs
    print("Affichage des textes abusifs...")

# Fonction pour afficher un autre résultat
def afficher_autre_resultat():
    # Logique pour afficher un autre résultat
    print("Affichage d'un autre résultat...")

# Couleurs
background_color = "#F0F0F0"
title_color = "#333333"
button_color = "#4CAF50"
button_text_color = "white"
label_color = "#333333"

# Création de la fenêtre principale
root = tk.Tk()
root.title("Topic Modeling Fenetre")
root.configure(background=background_color)

# Cadre principal pour toutes les parties
frame_principal = tk.Frame(root, bg=background_color)
frame_principal.pack(pady=10)

# Partie 1 : Charger les données
frame_charger_donnees = tk.Frame(frame_principal, bg=background_color)
frame_charger_donnees.pack(pady=10)

# Titre "Option 1: Charger les données"
label_option1 = tk.Label(frame_charger_donnees, text="Option 1: Charger les données", font=("Helvetica", 12, "bold"), fg=title_color, bg=background_color)
label_option1.grid(row=0, column=0, padx=5, sticky="w")

# Champ d'entrée pour l'emplacement de la BDD
entry_bdd = tk.Entry(frame_charger_donnees)
entry_bdd.grid(row=0, column=1, padx=5)

# Bouton pour ouvrir la BDD
btn_open_bdd = tk.Button(frame_charger_donnees, text="Ouvrir", command=ouvrir_bdd, bg=button_color, fg=button_text_color)
btn_open_bdd.grid(row=0, column=2, padx=5)

# Partie 2 : Affichage des informations générales, Word Cloud, et N-Grammes
frame_infos_generales = tk.Frame(frame_principal, bg=background_color)
frame_infos_generales.pack(pady=10)

# Titre "Infos sur les données"
label_option2 = tk.Label(frame_infos_generales, text="Infos sur les données", font=("Helvetica", 12, "bold"), fg=title_color, bg=background_color)
label_option2.grid(row=0, column=0, padx=5, sticky="w")

# Boutons "Afficher"
btn_afficher = tk.Button(frame_infos_generales, text="Afficher", command=afficher_infos_generales, bg=button_color, fg=button_text_color)
btn_afficher.grid(row=0, column=1, padx=5)

btn_wordcloud = tk.Button(frame_infos_generales, text="Word Cloud", command=afficher_wordcloud, bg=button_color, fg=button_text_color)
btn_wordcloud.grid(row=0, column=2, padx=5)

btn_ngram = tk.Button(frame_infos_generales, text="N-Gram", command=afficher_ngram, bg=button_color, fg=button_text_color)
btn_ngram.grid(row=0, column=3, padx=5)

# Partie 3 : Prétraitement des données et Modélisation Thématique
frame_pretraitement_modelisation = tk.Frame(frame_principal, bg=background_color)
frame_pretraitement_modelisation.pack(pady=10)

# Titre "Pré-traitement des données"
label_pretraitement = tk.Label(frame_pretraitement_modelisation, text="Pré-traitement des données", font=("Helvetica", 14, "bold"), fg=title_color, bg=background_color)
label_pretraitement.grid(row=0, column=0, columnspan=2, padx=10, sticky="w")

# Cases à cocher pour différentes options de prétraitement
var_stopwords = tk.IntVar()
check_stopwords = tk.Checkbutton(frame_pretraitement_modelisation, text="Stopwords", variable=var_stopwords, bg=background_color)
check_stopwords.grid(row=1, column=0, padx=10, sticky="w")

var_caracteres_speciaux = tk.IntVar()
check_caracteres_speciaux = tk.Checkbutton(frame_pretraitement_modelisation, text="Caractères spéciaux", variable=var_caracteres_speciaux, bg=background_color)
check_caracteres_speciaux.grid(row=2, column=0, padx=10, sticky="w")

var_ponctuation = tk.IntVar()
check_ponctuation = tk.Checkbutton(frame_pretraitement_modelisation, text="Ponctuation", variable=var_ponctuation, bg=background_color)
check_ponctuation.grid(row=3, column=0, padx=10, sticky="w")

var_tashkeel_tatweel_hamza_ligature = tk.IntVar()
check_tashkeel_tatweel_hamza_ligature = tk.Checkbutton(frame_pretraitement_modelisation, text="Tashkeel+Tatweel+Hamza+Ligature", variable=var_tashkeel_tatweel_hamza_ligature, bg=background_color)
check_tashkeel_tatweel_hamza_ligature.grid(row=4, column=0, padx=10, sticky="w")

var_tokenization = tk.IntVar()
check_tokenization = tk.Checkbutton(frame_pretraitement_modelisation, text="Tokenization", variable=var_tokenization, bg=background_color)
check_tokenization.grid(row=5, column=0, padx=10, sticky="w")

# Bouton "Appliquer" pour le prétraitement des données
btn_appliquer_pretraitement = tk.Button(frame_pretraitement_modelisation, text="Appliquer", command=appliquer_pretraitement, bg=button_color, fg=button_text_color)
btn_appliquer_pretraitement.grid(row=6, column=0, columnspan=2, pady=10)

# Titre "Modélisation thématique"
label_modelisation = tk.Label(frame_pretraitement_modelisation, text="Modélisation thématique", font=("Helvetica", 14, "bold"), fg=title_color, bg=background_color)
label_modelisation.grid(row=7, column=0, columnspan=2, padx=10, sticky="w")

# Menu déroulant pour choisir le modèle
var_modele = tk.StringVar()
var_modele.set("Machine Learning")  # Par défaut
option_modele = tk.OptionMenu(frame_pretraitement_modelisation, var_modele, "Machine Learning", "Deep Learning", "Transfer Learning", "Ensemble Learning")
option_modele.grid(row=8, column=0, padx=10, sticky="w")


btn_appliquer_modelisation = tk.Button(frame_pretraitement_modelisation, text="Appliquer", command=appliquer_modelisation, bg=button_color, fg=button_text_color)
btn_appliquer_modelisation.grid(row=9, column=0, columnspan=2, pady=10)

# Partie 4 : Détection de langage abusif
frame_detection_abus = tk.Frame(frame_principal, bg=background_color)
frame_detection_abus.pack(pady=10)

# Titre "Détection de langage abusif"
label_detection_abus = tk.Label(frame_detection_abus, text="Détection de langage abusif", font=("Helvetica", 14, "bold"), fg=title_color, bg=background_color)
label_detection_abus.grid(row=0, column=0, columnspan=2, padx=10, sticky="w")

# Champ de texte pour saisir le texte à analyser
label_texte = tk.Label(frame_detection_abus, text="Ecrire votre texte ici :", font=("Helvetica", 12), fg=label_color, bg=background_color)
label_texte.grid(row=1, column=0, padx=10, sticky="w")
entry_texte = tk.Entry(frame_detection_abus, width=50)
entry_texte.grid(row=1, column=1, padx=10)

# Bouton "Appliquer" pour la détection de langage abusif
btn_appliquer_detection_abus = tk.Button(frame_detection_abus, text="Appliquer", command=appliquer_detection_abus, bg=button_color, fg=button_text_color)
btn_appliquer_detection_abus.grid(row=2, column=0, columnspan=2, pady=10)

# Boutons pour les résultats de la détection automatique
frame_resultats = tk.Frame(frame_principal, bg=background_color)
frame_resultats.pack(pady=10)

# Bouton "Mots abusifs"
btn_mots_abusifs = tk.Button(frame_resultats, text="Mots abusifs", command=afficher_mots_abusifs, bg=button_color, fg=button_text_color)
btn_mots_abusifs.grid(row=0, column=0, padx=10)

# Bouton "Textes abusifs"
btn_textes_abusifs = tk.Button(frame_resultats, text="Textes abusifs", command=afficher_textes_abusifs, bg=button_color, fg=button_text_color)
btn_textes_abusifs.grid(row=0, column=1, padx=10)

# Bouton "Autre résultat"
btn_autre_resultat = tk.Button(frame_resultats, text="Autre résultat", command=afficher_autre_resultat, bg=button_color, fg=button_text_color)
btn_autre_resultat.grid(row=0, column=2, padx=10)

# Boucle principale Tkinter
root.mainloop()
