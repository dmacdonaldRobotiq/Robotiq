#!/bin/bash

PROJECT_HOME=`pwd`/`dirname $0`/../../..
DATABASE=""
TAG=SFL-MEP-`date "+%Y%m%d-%H%M%S"`

# usage `rollback SFL-MEP20140102-030405`
if [ $1 ]; then
    TAG=$1
fi

# Restore database
cd $PROJECT_HOME
gunzip -c backup/last | psql $DATABASE

cd $PROJECT_HOME/git
for i in `ls -d */`; do
    if [ $i != sfl ]
    then
        cd $i
        git checkout $TAG
        cd ..
    fi
done

exit 0

# EOF
