#!/bin/bash

factorial()
{
    if [ $1 -lt 0 ]
    then 
        echo "It doenst not exist"
    elif [ $1 -ge 0 ] && [ $1 -lt 2 ]
    then
        echo 1
    else
        last=$(( $1 - 1 ))
        last=$(factorial $(( $1 - 1)))
        echo $(( $1 * $last ))
    fi
}
factorial $1


# From 24 onwards it doesnt work, dunno why