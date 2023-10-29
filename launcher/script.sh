#!/bin/bash

i=0 # Initialize the variable i

while [ $i -lt 1 ]
do
    clear
    #COLOUR
    red='\e[1;31m'
    yellow='\e[0;33m'
    Blue='\e[1;34m'
    Reset='\e[0;0m'
    title="SF E-LAUNCH"
    echo -e '\033]2;'$title'\007'
    echo -e '        ,-:``-`-``-..
      /.-:_,:  ..-:_,`\
     /:   `    ,  _`.- \
    | ``. (`     /` ` \`|
    |:.  `\`-.   \_   / |
    |     (   `,  .`\ ;`|
     \     | .`     `-`/
      `.   ;/        .`
        ``-._____.-``
    '
    echo -e '\e[0m\e[3;36m-------------------------------
\e[3;31m   Orbiting`s selection menu \e[3;36m
------------------------------- \e[3;39m'

    # options
    while true; do

        echo " "
        echo "[1] > Mars        | description"
        echo "[2] > Jupiter     | description"
        echo "[3] > Saturn      | description"
        echo "[4] > Uranus      | description"
        echo "[5] > Rocket      | description"
        echo "[6] > Missile     | description"
        echo "[7] > Satellite   | description"
        echo "[8] > Mothership  | description"
        echo "[i] > Information | description"
        echo " " 
        echo "[*] > Exit script | Ctrl+C"

        echo -e $Blue" ┌─/"$red"Easy$Blue/───/"$yellow"Selection$Blue/"
    read -p      " └─────► " x

        if [ "$x" == "1" ]; then
            clear
            cd /path/mars/
            ./menu.sh
            
        elif [ "$x" == "2" ]; then
            clear
            cd /path/jupiter/
            ./menu.sh
            
        elif [ "$x" == "3" ]; then
            clear
            cd /path/saturn/
            ./menu.sh
            
        elif [ "$x" == "4" ]; then
            clear
            cd /path/uranus/
            ./menu.sh
            
        elif [ "$x" == "5" ]; then
            clear
            cd /path/rocket/
            ./menu.sh
            
        elif [ "$x" == "6" ]; then
            clear
            cd /path/missile/
            ./menu.sh
            
        elif [ "$x" == "7" ]; then
            clear
            cd /path/satellite/
            ./menu.sh
            
        elif [ "$x" == "8" ]; then
            clear
            cd /path/mothership/
            ./menu.sh
            
        elif [ "$x" == "i" ]; then
            clear
            cd /path/
            ./info.sh
            
        else
            clear
            echo "Invalid option. Please try again."
            sleep 2
            
        fi
    done
done
