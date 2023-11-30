
# Chronobio

## Setup du projet :
### Cloner le projet :
Pour utiliser notre algorithme pour le jeu chronobio il suffit de cloner ce repertoire git dans le dossier teams du jeux chonobio, ensuite il n'y a qu'à lancer le fichier competition.sh qui se trouve dans le repertoire chronobio
```bash
git clone https://github.com/A-lebourch/Chronobio.git
 ```

### installer les dépendance :

```bash
pip install -r requirements.txt
 ```

## Utilisation du code en mode compétition :

Il faut cloner le projet dans le dossier teams d'un jeux chronobio

Pour lancer le jeu il suffit d'utiliser le fichier ```_launch.sh```, ce fichier prend comme paramètre le port de la partie pouvoir s'y connecter

## Documentation du code :

Pour accéder à la couverture des test il faut éxecuter cette commande dans le repertoire principal, cela nous permet de voir uniquement les tests effectués pour les fonctions des classe utilisées dans notre programme

```bash
pytest --cov=algorithme/modules
```

En plus de pytest il y a d'autres plugins que nous avons utilisés, comme flake8 et black, pour voir si nous avons respecté la pep8, on peut utiliser cette commande :

```
flake8 algorithme/ -v
```

[Cliquer ici pour accéder à la documentation du code](https://a-lebourch.github.io/Chronobio/)

# PS (note pour VPoulailleau) :

Désolé j'ai fais les dernière modifications un  peu tard ...
Je ne comprend pas d'où viens mon bug avec l'employée 34 cela fait maintenant 2h que je cherche, je sais que le problème est dû au changement de numéro des employés, mais je n'arrive pas à identifier la source, car avant que ce soit l'employé 34, l'employé 12 faisait très bien son travail. j'imagine qu'il doit sauter une étape quelque part et donc il se retrouve surchargé avec 2 ordres.
