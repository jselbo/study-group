#!/bin/zsh

cd "$(dirname "$0")" || exit
./gradlew run -q --args="${*:1}"