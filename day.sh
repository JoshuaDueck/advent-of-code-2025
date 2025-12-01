#!/usr/bin/env bash
set -euo pipefail

source .env

day="$1"

cp -r ./template "./day$day"
cd "./day$day"

# Requires env var AOC_SESSION to be set
curl -s \
  -H "Cookie: session=$AOC_SESSION" \
  "https://adventofcode.com/2025/day/${day}/input" \
  -o input.txt
