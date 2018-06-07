#!/bin/bash

counter=3

while [ $counter -le 21 ] 

    do 
          echo $counter
          ((counter = $counter+3))
    done

echo "All done!"


