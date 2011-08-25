Kill Anton
=============

A very simple ticket system for posting tasks for system administrators.

Installation
------------------

::
        mkdir killanton
        virtualenv --distribute --no-site-packages -p /path/to/python2.7/or/less killanton
        cd killanton
        source bin/activate #activate the environment
        git clone git://github.com/eaudeweb/killanton.git
        pip install -r killanton/requirements.txt
        cd killanton
        ./manage.py syncdb 
        ./manage.py runserver
