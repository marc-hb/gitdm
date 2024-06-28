This gitdm for is pre-configured to work out-of-the-box when cloned
_inside_ sof.git!

    cd sof
    git clone <this repo>

Sample usage:

    cd sof/

    ./gitdm/per_quarter_csv.sh > _.csv

    git log --numstat --since 2017-01-01 | ./gitdm/gitdm -b ./gitdm/ -s -n -l 15 | less


Do NOT forget -n, otherwise some stats will be _silently_ broken!

For more see the original and main README.
