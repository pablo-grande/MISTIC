#!/bin/bash

stop="/bin/catalina.sh stop"
start="/bin/catalina.sh start"

function stop() {
	sh "APP"$stop;
	sh "CAS"$stop;
}

if [ "$1" == "stop" ]; then
	stop
elif [ "$1" == "run" ]; then
	stop
	sh "APP"$start;
	sh "CAS"$start;
else
	echo "ERROR: No argument provided. Valid arguments are 'stop' and 'run'";
fi
