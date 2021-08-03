#! /bin/bash

function func1()
{
    returnValue="I love Linux"
}

returnValue="I love Mac"
echo $returnValue

func1
echo $returnValue

echo "Note that we set over it"

declare -r returnValue="abc"
echo $returnValue
returnValue="sgsrghsrthethsrths"
echo $returnValue