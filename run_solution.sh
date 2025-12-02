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
        -p|--print-test)
            PRINT=YES
            shift
            ;;
        *)
            POS_ARGS+=("$1")
            shift
            ;;
    esac
done

if [[ "${TEST}" == YES ]]; then
    if [[ "${PRINT}" == YES ]]; then
        python -m ${NUM}.${NUM} -t -p
    else
        python -m ${NUM}.${NUM} -t
    fi
else
    python -m ${NUM}.${NUM}
fi