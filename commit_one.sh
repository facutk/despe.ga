#!/bin/bash
ARCHIVO=$1
COMENTARIO=$2
git add $1
git commit -m "$2"
git push origin master
