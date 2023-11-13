
parametre=$1

if [ $parametre -eq 1 ]; then
    python3 -m chronobio.game.server --fast

elif [ $parametre -eq 2 ] ;then
    python3 -m chronobio.viewer

elif [ $parametre -eq 3 ]; then
    cd algorithme/modules
    python3 client.py -u username
fi
