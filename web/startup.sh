#!/bin/sh
while getopts p: flag
do
    case "${flag}" in
        p) port=${OPTARG};;
    esac
done
source venv/bin/activate
gunicorn -b :$port --access-logfile - --error-logfile - wsgi:app
