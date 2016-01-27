#!/bin/bash

set -x

cd $(dirname $0)
echo $(pwd)
sleep 10

/giddyup leader check
if [ "$?" -eq "0" ]; then
  /usr/local/bin/python create_db.py
fi

sleep 5

cd $(dirname $0)
echo $(pwd)
exec /usr/local/bin/gunicorn -w 2 -b :8000 app:app
