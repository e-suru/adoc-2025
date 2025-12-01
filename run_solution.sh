#!/bin/bash

POS_ARGS=()

while [[ $# -gt 0 ]]
do
    case $1 in
        -n|--num)
            NUM="$2"
            shift
            shift
            ;;
        -t|--test)
            TEST=YES
            shift
            ;;
        *)
            POS_ARGS+=("$1")
            shift
            ;;
    esac
done

if [[ "${TEST}" == YES ]]; then
    python -t -m ${NUM}.${NUM}.py
else
    python ${NUM}/${NUM}.py -m pkg.handle_test
fi