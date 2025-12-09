#!/usr/bin/env bash
set -euo pipefail

source .env

day="$1"

if [ -d ./day$day ]; then
  # NO-OP
else
  cp -r ./template "./day$day"
fi
cd "./day$day"

# Requires env var AOC_SESSION to be set
curl -s \
  -H "Cookie: session=$AOC_SESSION" \
  "https://adventofcode.com/2025/day/${day}/input" \
  -o input.txt
