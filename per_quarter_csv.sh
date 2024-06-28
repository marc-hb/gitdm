#!/bin/bash

MYDIR=$(cd "$(dirname "$0")" && pwd)

dates=()

init_dates()
{
    for year in $(seq 2016 2024); do
        for month in $(seq 1 3 12); do
            dates+=( "$(printf '%d-%02d-01' "$year" "$month")" )
        done
    done
    # debug
    # declare -p dates
}

print_quarter()
{
    if true; then # gitdm

        git log --numstat "$@" |
            "$MYDIR"/sof_stats.py -n -b "$MYDIR"

    else # just the number of commits in this quarter

        printf "Total number of commits\n"
        git log --format=tformat:%h "$@" | wc -l

    fi
}

main()
{
    init_dates
    local len=${#dates[*]}
    local from=0  to=1

    # just the header, discard the data
    printf "Quarter start, "
    print_quarter --since='1 day ago' | head -n 1

    while [ "$to" -lt "$len" ]; do
        interval_start="${dates[$from]}"
        interval_end="${dates[$to]}"
        local git_log_args=(--since="$interval_start}" --until="$interval_end")
        printf '%s, ' "${interval_start}"
        # just the data, discard the header
        print_quarter "${git_log_args[@]}" | tail -n +2

        from=$to; to=$((to+1))
    done
}

main "$@"
