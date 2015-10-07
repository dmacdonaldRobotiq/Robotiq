#!/bin/bash

PROJECT_HOME=`pwd`/`dirname $0`/../../..
GIT_REPO_NAME=sfl
TOOLS_DIR=$PROJECT_HOME/git/$GIT_REPO_NAME/tools
BUILDOUT_CFG=$TOOLS_DIR/buildout.cfg
PARTS="clean_files_upgrade upgrade patch_files_upgrade"

# Prepare buildout environment
[ ! -d $PROJECT_HOME/bzr ] && mkdir $PROJECT_HOME/bzr
whoami | grep "odoo.dev\|jenkins" > /dev/null
if [ $? != 0 ];
then
	# Create symlink to save space and time
	[ ! -d $PROJECT_HOME/git/odoo ] && ln -s /opt/odoo/8.0/openupgrade $PROJECT_HOME/git/.
fi

[ ! -e $TOOLS_DIR/bin/buildout ] && /usr/bin/env python2 $TOOLS_DIR/bootstrap.py -c $BUILDOUT_CFG

# Prepare OpenUpgrade environment
$TOOLS_DIR/bin/buildout -c $BUILDOUT_CFG install $PARTS

# Create symlink for etc in PROJECT_HOME/etc
[ ! -d $PROJECT_HOME/etc ] && ln -s $TOOLS_DIR/etc $PROJECT_HOME/etc

# Create symlink for bin in PROJECT_HOME/bin
[ ! -d $PROJECT_HOME/bin ] && ln -s $TOOLS_DIR/bin $PROJECT_HOME/bin

# Create .openerp_serverrc file
echo -n "Creating ~/.openerp_serverrc file... "
if [ ! -e ~/.openerp_serverrc ]
then
    cat>~/.openerp_serverrc<<EOF
[options]
admin_passwd = admin
db_password = odoo
EOF
    echo "OK"
else
    echo "File exists!"
fi

# Make sure there's no db_password and admin_passwd in the generated config file
sed -i '/admin_passwd/d' $TOOLS_DIR/etc/upgrade.cfg 
sed -i '/db_password/d' $TOOLS_DIR/etc/upgrade.cfg

# "${PROJECT_HOME}/bin/start_openupgrade" -d upgrade --update all --stop-after-init

exit 0

# EOF
