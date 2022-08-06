Projet de wordlist Francophone
Depuis le début des années 2000 la complexité des mots de passes des utilisateurs n'a cessée d'augmenter, en parti grace à l'éducation et à la sensbilisation des principaux intéressés
mais aussi à cause du renforcement des politiques de complexité des mots de passes.
Cela concerne tous les SI, notament les annuaires de comptes utilisateurs (AD) dans les entreprises et les administrations. 

Pour établir les politiques de mots de passes les administrateurs et les RSSI se basent sur les recommandations de l'ANSSI : 
https://www.ssi.gouv.fr/administration/precautions-elementaires/calculer-la-force-dun-mot-de-passe/ 

Ainsi on peut définir les critères suivants pour créer un mot de passe "fort" : 

Mot de passe de 12 caractères dans un alphabet de 90 symboles : A à Z, a à z et ! #$*% ? &[|]@^µ§ :/ ;.,<>°²³

Dans le cadre d'une entreprise on utilise le plus souvent des services SSO, l'objectif est d'utiliser un seul couple login / mot de passe pour accéder à l'ensemble des services.
Cela est certe très pratique mais cela augmente d'autant la valeur des identifiants de l'utilisateur. 
Un identifiant compromis = un accès à tous les services utilisant SSO. 

Maintenant, dans le cadre d'un retex je peux affirmer qu'une grande part des utilisateurs utilisent des formats de mot de passe prédictibles. 
Vous pouvez aussi le constater en cherchant des leaks de mot de passes en clair sur le clear ou le deep web ... 

Voici les structures à éviter : 

[mot] + [nombre]
[mot] + [nombre] + [caractère spécial]
[nombre] + [mot] + [caractère spécial]
[mot] + [caractère spécial] + [nombre]
[nombre] + [mot] + [caractère spécial]

et bien etendu toutes les permutations de ces structures sont à prendre en compte. 


Voici maintenant

[mot] : 
Nom de l'entreprise
Ville de l'entreprise
Ville
Nom de famille
Prénom
Pseudo
Surnom
Marque
Nom commun
Mot du dictionnaire

[nombre] : 
Code Postal
Date (DD/MM/YY ou YYYY)
de 0 à 99999
de 0000
 à 99999


