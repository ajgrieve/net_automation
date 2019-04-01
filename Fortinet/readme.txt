fnt_compare

Performs a high level comparison of two Fortigate firewall configurations. Specifically, compares the existence of various firewall address objects between a source and destination configuration file.

It does not check that the configuration of the objects is identical.

fnt_compare.py -h
usage: fnt_compare.py [-h] [--verbose] [--fwaddr] [--fwaddrgrp] [--fwsvc]
                      [--fwsvcgrp] [--fwnat] [--all]
                      source destination

Checks for the existence of Fortinet firewall configuration objects, between a
source and destination configuration file. Note - does not check that the
configuration of the objects is the same

positional arguments:
  source       Source device config file
  destination  Destination device config file

optional arguments:
  -h, --help   show this help message and exit
  --verbose    Print verbose output
  --fwaddr     Compare firewall address objects
  --fwaddrgrp  Compare firewall address groups
  --fwsvc      Compare firewall service objects
  --fwsvcgrp   Compare firewall service groups
  --fwnat      Compare firewall NAT objects
  --all        Run all comparisons

