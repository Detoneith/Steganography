# Stéganographie

## Introduction
Ce code Python implémente une application graphique simple utilisant les modules tkinter et ttkbootstrap pour la stéganographie. Il offre aux utilisateurs la possibilité d'encoder et de décoder les messages cachés dans une image.

## Exigences
Ce code a été écrit avec Python 3.9. Il nécessite l'installation des modules Python suivants :

- numpy
- Pillow (PIL)
- ttkbootstrap
- tkinter

Pour installer ces modules, utilisez la commande suivante dans le terminal :
- pip install numpy Pillow ttkbootstrap

## Utilisation
Pour lancer l'application, lancez simplement le fichier steganographie.py. Cela ouvrira une fenêtre d'interface graphique dans laquelle vous pourrez sélectionner une image, saisir un message à encoder ou à décoder et effectuer l'action correspondante à l'aide du bouton "Encoder" ou "Décoder".

## Menu
Déposer:
- Ouvrir : permet d'ouvrir un fichier image au format .jpg ou .png.
- Enregistrer : Cela vous permet d'enregistrer l'image avec le message encodé sous forme de fichier .png ou .jpg.
- Quitter : Cela vous permet de quitter l'application.

Aider:
- A propos : affiche des informations sur l'application.

## Éléments de l'interface graphique
**Saisie de message :** C'est ici que vous pouvez saisir le message à encoder ou à décoder.

**Canvas :** Ceci affiche le fichier image sélectionné.

**Boutons:**

- Encoder : Ceci encode le message saisi dans le fichier image sélectionné.
- Décoder : Ceci décode le message caché dans le fichier image sélectionné.

# Disclaimer
**Cette application a été conçue à des fins éducatives uniquement. L'auteur ne tolère ni ne promeut l'utilisation de la stéganographie à des fins illégales ou contraires à l'éthique.**
