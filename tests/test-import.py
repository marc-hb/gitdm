#!/usr/bin/env python

import sys
sys.path.extend('.')
# Warning: this is not your usual "import" at all; it:
# - "hijacks" sys.argv and parses them
# - reads and parses the git log from stdin
import gitdm
import reports

# Everything else will be gathered in "Others"
# TODO: use "GroupMap" config files and "more real" employers for more
# coverage
EMPLOYERS = [
    "enselic@gmail.com", "punk.rocker@example.com", "Others",
]

def PerEmployerStats(elist, lines_changed=False):
    "Returns commit numbers unless lines_changed is True"
    values = {empl: 0 for empl in EMPLOYERS}
    for empl in elist:
        assert(empl.name != "Others")
        key = empl.name if empl.name in EMPLOYERS else "Others"

        if lines_changed:
            values[key] += empl.changed

        else: # commit numbers
            values[key] += empl.count

    return values

def main():
    hlist = gitdm.database.AllHackers()
    elist = gitdm.database.AllEmployers()

    # print everything
    gitdm.PrintReports(hlist, elist)

    # Top commit numbers per employer
    # gitdm.reports.ReportByPCEmpl(elist, gitdm.CSCount)
    # Top lines changed per employer
    # gitdm.reports.ReportByELChanged(elist, gitdm.TotalChanged)

    # Commit numbers
    # stats = PerEmployerStats(elist)
    # Lines changed
    stats = PerEmployerStats(elist, lines_changed=True)

    # CSV header
    reports.Write("\n" + ", ".join(EMPLOYERS) + "\n")
    # CSV data
    reports.Write(", ".join([str(stats[empl]) for empl in EMPLOYERS]) + "\n")

if __name__ == "__main__":
    main()
