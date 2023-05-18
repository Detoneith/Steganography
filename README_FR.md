# Steganography

Ce code contient une classe Steganographie qui permet de cacher des messages dans des images et de les récupérer ensuite. Voici les différentes fonctionnalités de cette classe :

## Création de la fenêtre principale
Lorsque la classe est initialisée, elle crée une fenêtre principale et y ajoute différents éléments :

- Un menu avec des options de fichiers et d'aide
- Un formulaire d'entrée de texte
- Un canevas pour afficher l'image
- Des boutons pour encoder et décoder le message

## Menu
Le menu permet d'effectuer différentes actions :

- "Open" : ouvre une boîte de dialogue pour sélectionner une image à afficher
- "Save" : sauvegarde l'image actuelle sur le disque dur
- "Exit" : ferme la fenêtre

## Formulaire d'entrée de texte
Le formulaire d'entrée de texte permet de saisir le message à cacher dans l'image. Il est initialisé avec le texte "Enter a message" qui est effacé lorsqu'on clique dessus.

## Canevas
Le canevas est utilisé pour afficher l'image sélectionnée. Lorsqu'on sélectionne une nouvelle image, elle est automatiquement redimensionnée pour tenir dans le canevas.

## Boutons
Les boutons "Encode" et "Decode" permettent d'encoder et de décoder le message dans l'image. Lorsqu'on clique sur "Encode", le message est caché dans l'image et l'image modifiée est affichée sur le canevas. Lorsqu'on clique sur "Decode", le message caché dans l'image est affiché dans le formulaire d'entrée de texte.

# Disclaimer
**Cette application a été conçue à des fins éducatives uniquement. L'auteur ne tolère ni ne promeut l'utilisation de la stéganographie à des fins illégales ou contraires à l'éthique.**
