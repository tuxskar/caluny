#!/bin/bash
NAME="caluny" # Name of the application
BASE_DIR=/home/django/caluny/caluny
DJANGODIR=$BASE_DIR # Django project directory
SOCKFILE=$DJANGODIR/gunicorn.sock # we will communicate using this unix socket
LOGSDIR=$BASE_DIR/caluny/logs
ENVBINDIR=/home/django/.virtualenvs/caluny/bin

USER=django # the user to run as
GROUP=django # the group to run as
NUM_WORKERS=4 # how many worker processes should Gunicorn spawn

MAX_REQUESTS=1 # reload the application server for each request
DJANGO_SETTINGS_MODULE=caluny.settings.local # which settings file should Django use
DJANGO_WSGI_MODULE=caluny.wsgi # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source $ENVBINDIR/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn’t exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
test -d $LOGSDIR || mkdir -p $LOGSDIR

# Start your Django Unicorn

exec $ENVBINDIR/gunicorn \
	-b 0.0.0.0:9000 \
	--worker-class gevent \
	--workers 3 \
	--log-level info \
	--log-file $LOGSDIR/gunicorn.log \
	--access-logfile $LOGSDIR/gunicorn.access \
	caluny.wsgi
