#!/bin/zsh

cd "$(dirname "$0")" || exit
./target/release/p1 "${1}" "${2}"
