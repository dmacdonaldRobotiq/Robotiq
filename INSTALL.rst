Requirements
============

# Install dependencies 

  sudo apt-get install git python-pip postgresql python-dev postgresql-server-dev-9.3 libldap2-dev \
      libsasl2-dev libjpeg-dev libxml2-dev libxslt1-dev zlib1g-dev postfix libgeoip-dev
  sudo pip install setuptools zc.buildout

# Add a PostgreSQL user

  sudo -s
  su - postgres -c "createuser --superuser --createdb --username postgres --no-createrole -w odoo8dev"

# and change its password 

  su - postgres -c "psql -c \"ALTER USER odoo8dev WITH PASSWORD 'openerp'\""

Installation steps
==================

# Prepare the environment

  mkdir -p <client>/git
  cd <client>/git

# Retrieve the git repository

  git clone git@git.savoirfairelinux.com:<repository_name>.git sfl

# Install the environnement

  cd ..
  ./git/sfl/tools/install.sh

# Start Odoo

  ./bin/start_openerp.sh

# and connect to http://localhost:9999

New Release
===========
1. in git
    * set a tag at the last commit of the branch
    * create new remote branch

2. in gitlab (https://gitlab.savoirfairelinux.com/odoo/robotiq)
    * close previous milestone
    * create new milestone
    * set new branch as default branch (settings > projects > Default Branch)
    * protect new branch (settings > protected branches > branch)

3. in jenkins-test (https://test.savoirfairelinux.com/view/Odoo/job/Robotiq-Tests)
    * configure to use the new branch (configure > gitlabTargetBranch)

4. in git (again)
    * delete previous remote branch

5. in the project:
    * pump up the version of the client module to the release number
    * pump up the version of the database to the release number
        in tools/VERSION.txt
    * update the upgrade.py script if needed to use the new version of
        the database.
