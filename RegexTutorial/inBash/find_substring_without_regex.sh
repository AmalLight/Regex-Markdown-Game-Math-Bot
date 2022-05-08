#!/bin/bash

if (( ${#@} >= 3 )) ;

then

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    
    regex=$1 ; groups=($2) ; string="${@:3:999}"
    
    count=0 ; findcount=()
    
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
    
    for i in `seq $count`
    do
    
        [[ ${groups[@]} != *"$i"*  ]] && [[ ${findcount[@]} == *"$i"* ]] && echo -n ' '
        
        [[ ${groups[@]} != *"$i"*  ]] && echo -n ${BASH_REMATCH[$i]}

    done
    echo ''

else

    echo ''
    echo 'regex=$1'
    echo "groups=\$2 , starting from 1 , to set as '1 2 3' "
    echo 'string=from $3 on next ...'
    echo ''
    echo 'ps1: use (§) group in regex for [[:space:]]'
    echo ''
    echo 'ps2: count works only with ()() not for ( ()() )'
    echo ''
    echo 'ps3: from RIGHT to LEFT'
    echo ''
    echo ''
fi
