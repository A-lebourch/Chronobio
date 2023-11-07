
parametre=$1

if [ $parametre -eq 1 ]; then
    python3 -m chronobio.game.server
 
elif [ $parametre -eq 2 ] ;then
    python3 -m chronobio.viewer
 
elif [ $parametre -eq 3 ]; then
    python3 sample_player_client.py -u username
fi
