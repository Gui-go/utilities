#! /bin/bash

vec=('primeiro' 'segundo' 'terceiro')

echo "Print all vars: \${vec[@]}"
echo "${vec[@]}"
echo ""

echo "Print only the first: \${vec[0]} (Starts from zer0)"
echo "${vec[0]}"
echo ""

echo "Print only the third: \${vec[2]}"
echo "${vec[2]}"
echo ""

echo "Remove: unset vec[1]"
unset vec[1]
echo "${vec[@]}"
echo ""

echo "List all possible indexes: \${!vec[@]} (Note que o index removido permanece removido)"
echo "${!vec[@]}"
echo ""

echo "List missing indexes: \${#vec[@]}"
echo "${#vec[@]}"
echo ""

echo "You can set a variable again"
vec[1]="VOLTEI!"
echo "${vec[@]}"