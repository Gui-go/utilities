#!/bin/bash



echo 'one two three' | xargs touch
echo 'one two three' | xargs rm


# xargs - build and execute command lines from standard input
echo $(seq 20) | xargs -n 2


find . -name "*.png" -type f -print | xargs tar -cvzf pics.tar.gz

cat links.txt | xargs wget # wget a list of urls

# The cat command result is passed to the end of the xargs command.
# What if your command needs the output in the middle
# Just use {} combined with –i parameter to replace the arguments in the place where the result should go like this:
ls /etc/*.conf | xargs -i cp {} /home/likegeeks/Desktop/out

seq 10 13 | xargs -I{} -n 1 echo "Iterador maneiro n{}"