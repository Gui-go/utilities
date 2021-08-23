#!/bin/bash



echo 'one two three' | xargs touch
echo 'one two three' | xargs rm


# xargs - build and execute command lines from standard input
echo $(seq 20) | xargs -n 2