# Chronobio

## Installation
### Installation du répertoire GIT :
``` shell
git clone https://github.com/A-lebourch/Chronobio.git
```
OU
```shell
git clone git@github.com:A-lebourch/Chronobio.git
```
### Installation des dépendances :

```shell
pip install arcade
pip install pytest
```

## Exécution du jeux en local

Ouvrir 3 terminaux et executer une commande dans un terminal

```shell
python3 -m chronobio.game.server 
```

```shell
python3 -m chronobio.viewer 
```

Remplacer USERNAME par un pseudo

```shell
python3 sample_player_client.py -u USERNAME
```

## Exécuter les tests du code

Grace au paquet python pytest nous avons la possibilité de tester le code pour detecter des erreurs 

```shell
cd /tests
pytest
```

Pour ce faire il faut configurer un fichier python dans le repertoire tests, voir le fichier test_loan.py dans /tests/chronobio/game (c'est une façon de faire, il y a d'autres possinilités)

