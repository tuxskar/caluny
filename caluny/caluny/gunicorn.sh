#!/bin/bash
NAME="caluny # Name of the application
BASE_DIR=/home/django/caluny/caluny
DJANGODIR=BASE_DIR # Django project directory
SOCKFILE=DJANGODIR/gunicorn.sock # we will communicate using this unix socket

USER=django # the user to run as
GROUP=django # the group to run as
NUM_WORKERS=4 # how many worker processes should Gunicorn spawn

MAX_REQUESTS=1 # reload the application server for each request
DJANGO_SETTINGS_MODULE=caluny.settings.common # which settings file should Django use
DJANGO_WSGI_MODULE=caluny.wsgi # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ~/.virtualenvs/caluny/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn’t exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn

# Programs meant to be run under supervisor should not daemonize themselves (do not use –daemon)
exec ~/.virtualenvs/caluny/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
–name $NAME \
–workers $NUM_WORKERS \
–max-requests $MAX_REQUESTS \
–user=$USER –group=$GROUP \
–bind=0.0.0.0:3000 \
–log-level=error \
–log-file=-