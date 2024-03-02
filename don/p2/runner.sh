#!/bin/zsh

cd "$(dirname "$0")" || exit
../target/release/p2 "${1}"
