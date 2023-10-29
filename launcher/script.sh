#!/bin/bash
clear
#COLOUR
red='\e[1;31m'
yellow='\e[0;33m'
Blue='\e[1;34m'
Reset='\e[0;0m'
title="Orbit Attacking tool"
echo -e '\033]2;'$title'\007'
echo -e '\e[0m\e[3;36m-------------------------------
\e[3;31m Orbit Online DoS tool \e[3;36m

# logo
echo "
    ,-:``-`-``'-, 
  .'-:_,:  ':-:_,'.
 /:   '/    ,  _`.-\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-.--_-_. -`
"

# options
while true; do
    echo "Menu Options:"
    echo "1. Option 1"
    echo "2. Option 2"
    echo "3. Option 3"
    echo "4. Exit"
    echo -e $Blue" ┌─["$red"Easy$Blue]──[$red~$Blue]─["$yellow"Selection$Blue]"
    read -p      " └─────► " n

    case $choice in
        1)
            echo "You selected Option 1"
            # Add your actions for Option 1 here
            ;;
        2)
            echo "You selected Option 2"
            # Add your actions for Option 2 here
            ;;
        3)
            echo "You selected Option 3"
            # Add your actions for Option 3 here
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    esac
done
