#!/bin/bash

PROJECT_HOME=`pwd`/`dirname $0`/../../..
GIT_REPO_NAME=sfl
TOOLS_DIR=$PROJECT_HOME/git/$GIT_REPO_NAME/tools
BUILDOUT_CFG=$TOOLS_DIR/frozen.cfg
PARTS="prod webkit"
# Name of the database that will be back up during the deploy process.
DATABASE="prod_robotiq"

# Backup database
[ ! -d $PROJECT_HOME/backup ] && mkdir backup
pg_dump -C $DATABASE | gzip -c > backup/$DATABASE-`date '+%Y%m%d-%H%M%S'`.sql.gz
[ -e backup/last ] && rm backup/last && ln -s backup/$DATABASE-`date '+%Y%m%d-%H%M%S'`.sql.gz backup/last

# Prepare buildout environment
[ ! -e $TOOLS_DIR/bin/buildout ] && python2 $TOOLS_DIR/bootstrap.py -c $BUILDOUT_CFG

if [ -d $PROJECT_HOME/git ]
then
    cd $PROJECT_HOME/git
    for i in `ls -d */`; do
        cd $i
        git tag SFL-MEP-`date "+%Y%m%d-%H%M%S"`
        cd ..
        done
else
    mkdir $PROJECT_HOME/git
fi

# Prepare or update Odoo environment
$TOOLS_DIR/bin/buildout -c $BUILDOUT_CFG install $PARTS

# Create symlink for etc
[ ! -d $PROJECT_HOME/etc ] && ln -s $TOOLS_DIR/etc $PROJECT_HOME/etc

# Create symlinks for bin
[ ! -d $PROJECT_HOME/bin ] && ln -s $TOOLS_DIR/bin $PROJECT_HOME/bin

# Create .openerp_serverrc file
echo -n "Creating ~/.openerp_serverrc file... "
if [ ! -e ~/.openerp_serverrc ]
then
    cat>~/.openerp_serverrc<<EOF
[options]
admin_passwd =
db_password =
EOF
    echo "OK"
else
    echo "File exists!"
fi

# Make sure there's no db_password and admin_passwd in the generated config file
sed -i '/db_password/d' $TOOLS_DIR/etc/prod.cfg
sed -i '/admin_passwd/d' $TOOLS_DIR/etc/prod.cfg

exit 0

# EOF
