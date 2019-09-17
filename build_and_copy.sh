#!/bin/sh

npm run build
rm -rf ../egarbarino.github.io/vuejs-hangman/*
cp -R dist/* ../egarbarino.github.io/vuejs-hangman

