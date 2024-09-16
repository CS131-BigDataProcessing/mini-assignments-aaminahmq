#!/bin/bash

#activity 1
echo "The time and date are: $(date)"
echo "Let’s see who is logged into the system:"
who 
user_me=$(echo $USER)
h_dir=$(echo $HOME)
echo "For $user_me, the home directory is $h_dir"

#activity 2
name=$1
money=$2
echo "My name is $name and I have \$${money} in my wallet."

#activity 3

mathvar1=$((1+5))
mathvar2=$((mathvar1 * 20))
mathvar3=10
mathvar4=$((mathvar1 * (mathvar2 + mathvar3)))
echo "Variable 1 is $mathvar1. Variable 2 is $mathvar2. Using $mathvar3 for Variable 3, our final Variable 4 is $mathvar4."

#activity 4

floating=$(echo "scale=3; 4.5/1.7" | bc)
echo "Our floating variable is $floating"

