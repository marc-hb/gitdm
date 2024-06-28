#!/usr/bin/env python

# Warning: this is not your usual "import" at all; it:
# - "hijacks" sys.argv and parses them
# - reads and parses the git log from stdin
import gitdm

# See "GroupMap" config files.
# Everything else will be gathered in "Others"
EMPLOYERS = [
    "Intel Linux Audio", "Intel IPG", "Intel CCG", "Intel Zephyr",
    "Intel unknown", "NXP", "Google", "Others"
]

def EmployersStats(elist, lines_changed=False):
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
    # for debug
    # gitdm.PrintSummary(gitdm.database)

    hlist = gitdm.database.AllHackers()
    elist = gitdm.database.AllEmployers()

    # print everything
    #gitdm.PrintReports(hlist, elist)

    # Top commit numbers per employer
    # gitdm.reports.ReportByPCEmpl(elist, gitdm.CSCount)
    # Top lines changed per employer
    # gitdm.reports.ReportByELChanged(elist, gitdm.TotalChanged)

    # Commit numbers
    stats = EmployersStats(elist)
    # Lines changed
    # stats = EmployersStats(elist, lines_changed=True)

    # CSV header
    print(", ".join(EMPLOYERS))
    # CSV data
    print(", ".join([str(stats[empl]) for empl in EMPLOYERS]))

if __name__ == "__main__":
    main()
