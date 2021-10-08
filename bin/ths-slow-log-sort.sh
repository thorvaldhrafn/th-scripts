#!/bin/bash
slow_path="/var/log/mariadb/slow-query.log"
sorted_log_path="."

#lines_nb=`grep -n "^use" $slow_path | awk -F: '{ print $1 }'`

for a in $(grep -n "^use" $slow_path | awk -F: '{ print $1 }')
    do
        b=$(grep -n "^use" $slow_path | awk -F: '{ print $1 }'| grep -A1 -w "$a" | grep -vw "$a")
        db_name=$(grep -n "^use" $slow_path | grep -w "$a" | awk '{ print $2 }' | sed 's/;//g')
        #echo $a
        #echo $b
        let "c = b - 1 - 3"
        let "d = b - a"
        #echo $a $b $c
        head -"$c" $slow_path | tail -"$d" | grep -vw "^use" >> $sorted_log_path/"$db_name"
        echo "$db_name"
        #exit 0
    done
