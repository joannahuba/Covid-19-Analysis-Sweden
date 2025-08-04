#!/bin/bash
# this script will show all the plots if you call it with -d/--display 
# or save all the plots if you call it with -s/--save

DISPLAY_MODE=  # 0 for display, 1 for save

while [[ $# -gt 0 ]]; do
  case $1 in
    -d|--display)
      DISPLAY_MODE=0
      shift
      ;;
    -s|--save)
      DISPLAY_MODE=1
      shift
      ;;
    -*|--*)
      echo "Unknown option $1"
      exit 1
      ;;
    *)
      echo "Invalid argument: $1"
      exit 1
      ;;
  esac
done

if [ -z "$DISPLAY_MODE" ]; then
  echo "Usage: $0 [-d|--display] [-s|--save]"
  exit 1
fi

for i in *.py; do
  if [ -f "$i" ] && [ "$i" != "${0##*/}" ]; then
    echo "Processing $i with mode $DISPLAY_MODE"
    python3 "$i" "$DISPLAY_MODE"
  fi
done