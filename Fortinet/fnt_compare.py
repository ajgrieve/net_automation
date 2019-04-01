import argparse
import sys


def run(args, startDelimiter, description):
    f = open(args.source, 'r')

    vdomName = ''

    sourceDict = {}
    print('-' * 40)
    print('Verifying ' + description + ' objects')
    print('-' * 40)
    print('Source ' + description + ' counts:')
    for line in f:
        if 'config vdom' in line:
            text = f.readline()
            vdomName = text.strip()[5:]
            sourceDict[vdomName] = []
        if line.strip() == startDelimiter:
            policyEnd = False
            count = 0
            while not policyEnd:
                text = f.readline()
                if text.strip()[:4] == 'edit':
                    arr = sourceDict.get(vdomName)
                    arr.append(text.strip()[5:])
                    count += 1
                    continue
                if text.strip() == 'end':
                    policyEnd = True
            format_str = '{: <15} {: <5}'
            print(format_str.format(vdomName, count))

    print()

    f = open(args.destination, 'r')

    vdomName = ''

    destDict = {}
    print('Destination ' + description + ' counts:')
    for line in f:
        if 'config vdom' in line:
            text = f.readline()
            vdomName = text.strip()[5:]
            destDict[vdomName] = []
        if line.strip() == startDelimiter:
            policyEnd = False
            count = 0
            while not policyEnd:
                text = f.readline()
                if text.strip()[:4] == 'edit':
                    arr = destDict.get(vdomName)
                    arr.append(text.strip()[5:])
                    count += 1
                    continue
                if text.strip() == 'end':
                    policyEnd = True
            format_str = '{: <15} {: <5}'
            print(format_str.format(vdomName, count))
    print()

    print('Source VDOMs: ', len(sourceDict), 'Dest VDOMs: ', len(destDict))
    print('VDOMs on source and not dest:')
    for vdom in sourceDict.keys():
        if vdom not in destDict.keys():
            print(vdom)
    print()

    print('VDOM ' + description + ' summary:')
    for vdom in sourceDict.keys():
        if vdom in destDict.keys():
            print(vdom)
            sourceArr = list(sourceDict.get(vdom))
            destArr = list(destDict.get(vdom))
            for x in sourceArr[:]:
                if x in destArr[:]:
                    sourceArr.remove(x)
                    destArr.remove(x)
            print('On source but not dest', sourceArr)
            print('On dest but not source', destArr)
            print()

    if (args.verbose):
        print('Full arrays:')
        print(sourceDict)
        print(destDict)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Checks for the existence of Fortigate firewall configuration objects, between a source and destination configuration file. Note - does not check that the configuration of the objects is the same')
    parser.add_argument('source', help='Source device config file')
    parser.add_argument('destination', help='Destination device config file')
    parser.add_argument('--verbose', help='Print verbose output', action='store_true')
    parser.add_argument('--fwaddr', help='Compare firewall address objects', action='store_true')
    parser.add_argument('--fwaddrgrp', help='Compare firewall address groups', action='store_true')
    parser.add_argument('--fwsvc', help='Compare firewall service objects', action='store_true')
    parser.add_argument('--fwsvcgrp', help='Compare firewall service groups', action='store_true')
    parser.add_argument('--fwnat', help='Compare firewall NAT objects', action='store_true')
    parser.add_argument('--all', help='Run all comparisons', action='store_true')
    if len(sys.argv[1:]) < 3:
        parser.print_help()
        parser.exit()
    args = parser.parse_args()
    if (args.all):
        args.fwaddr = True
        args.fwaddrgrp = True
        args.fwsvc = True
        args.fwsvcgrp = True
        args.fwnat = True

    if (args.fwaddr):
        run(args, 'config firewall address', 'address')
    if (args.fwaddrgrp):
        run(args, 'config firewall addrgrp', 'address group')
    if (args.fwsvc):
        run(args, 'config firewall service custom', 'service')
    if (args.fwsvcgrp):
        run(args, 'config firewall service group', 'service group')
    if (args.fwnat):
        run(args, 'config firewall vip', 'NAT')
