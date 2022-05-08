#!/bin/bash

if (( ${#@} >= 4 )) ;

then

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    
    regex=$1 ; groups=($2) ; replaces=($3) ; string="${@:4:999}"
    
    count=0 ; findcount=() ; oldvalues=()

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    
    if (( ${#groups[@]} > ${#replaces[@]} )) ; then echo 'len groups > len replaces' && exit ; fi
    
    for group in ${groups[@]}
    do
            
        if [[ $oldvalues =~ $group ]] ; then echo 'least two group of groups are equal' && exit ; fi
        
        oldvalues+=($group)
        
    done
    
    # ------------------------------------------------------------
    # ------------------------------------------------------------
    
    for (( i=0; i<${#regex}; i++ ))
    do
        if [[ ${regex:$i:1} =~ '(' ]] ; then count=$((count+1)) ; fi
        
        if [[ ${regex:$i:1} =~ '§' ]] ;
        then
            
            findcount+=($count)
            
            regex=${regex/'§'/'[[:space:]]'}
        fi
        
    done
    
    [[ $string =~ $regex ]]
    
    # ------------------------------------------------------------
    # ------------------------------------------------------------
    
    posx=(-1)
   
    for i in `seq $count`
    do
    
       i2=0 ; flag=0
       
       for group in ${groups[@]}
       do
           if [[ "$i" == "$group" ]] ; then posx+=($i2) && flag=1 ; fi
           
           i2=$((i2+1))
           
       done
       
       if [[ $flag == 0 ]] ; then posx+=(-1) ; fi
    
    done
    
    # ------------------------------------------------------------
    # ------------------------------------------------------------
    
    for i in `seq $count`
    do
    
        if (( ${posx[$i]} < 0 )) ;
        then
                
            [[ ${findcount[@]} == *"$i"* ]] && echo -n ' ' ; echo -n ${BASH_REMATCH[$i]}

        else
        
            echo -n ${replaces[${posx[$i]}]}
            
        fi

    done
    echo ''

else

    echo ''
    echo 'regex=$1'
    echo "groups=\$2 , starting from 1 , to set as '1 2 3' "
    echo 'replaces=$3'
    echo 'string=from $4 on next ...'
    echo ''
    echo 'ps1: use (§) group in regex for [[:space:]]'
    echo ''
    echo 'ps2: count works only with ()() not for ( ()() )'
    echo ''
    echo 'ps3: replace variables works for group in groups'
    echo ''
    echo 'ps4: from RIGHT to LEFT'
    echo ''
    echo ''
fi
