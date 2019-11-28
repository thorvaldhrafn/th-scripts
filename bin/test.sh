#!/usr/bin/env bash

__nginx_conf_paths() {
chck_path="$1"
includes=`cat ${chck_path} | egrep "(\s*|\t*)include.*" | awk '{ print $2 }' | sed -r 's/;$//'`
for i in ${includes}
    do
        dname=`dirname ${i} | head -n1`
        if [[ "${dname}" = "." ]]
            then
                dname=`dirname ${chck_path}`
        fi
        fname_tmp=`basename ${i}`
        confs=`find ${dname} -type f -name "$fname_tmp" | xargs`
        check=`echo "$confs" | wc -w`
        if [[ ${check} -eq 1 ]]
            then
                CONF_LIST="$CONF_LIST $confs"
                fname=`basename ${i}`
                full_fname="${dname}/$fname"
                cat ${full_fname} | egrep "(\s*|\t*)include.*" > /dev/null
                if [[ $? -eq 0 ]]
                    then
                        nginx_conf_paths ${full_fname}
                fi
            else
                for j in ${confs}
                    do
                        CONF_LIST="${CONF_LIST} ${confs}"
                        fname=`basename ${i}`
                        full_fname="${dname}/$fname"
                        if [[ $? -eq 0 ]]
                            then
                                nginx_conf_paths ${full_fname}
                        fi
                    done
        fi
done
}

echo ${CONF_LIST}