

import csv
import sys
import os
import difflib
import shlex
import re


def main():
    try:


        master = []
        newUsers = []
        with open('master.txt', 'r') as masterFile:
            # print('-----')
            cnt = 0
            for line in masterFile:
                name = format_names(line)
               # print('line {}: content: {}'.format(cnt, name))


                fullname = getFirstLastName(name)
                master.append(fullname)

                cnt += 1
            # print('-----')
        with open('remove.txt', 'r') as inputFile:
            cnt = 0
            for line2 in inputFile:
                name2 = format_names(line2)
                # print('line {}: content: {}'.format(cnt, name2))

                fullname = getFirstLastName(name2)
                newUsers.append(fullname)

                cnt += 1

        print()
        print('----List of names on INPUTLIST and not in MASTERLIST----')

        # create new file containing only the unique names in list 2
        with open("usersToAdd.txt", 'w') as myFile:
            for element in newUsers:
                if element not in master:
                    myFile.write(element + "\n")
                    print(element)

        print()
        print('----List of names on Both Lists----')
         # create new file containing only the unique names in list 2
        with open("usersToRemove.txt", 'w') as myFile:
            for element in newUsers:
                if element in master:
                    myFile.write(element + "\n")
                    print(element)

    except Exception as e:
        print('Error opening input file {}'.format(e))
        exit(1)


def record_name_cnt(name, masterNames):
    # for name in names:
    if name != '' or name != ' ':
        if name.lower() in masterNames:
            masterNames[name.lower()] += 1
        else:
            masterNames[name.lower()] = 0


def format_names(name):
    newName = re.sub(r'^[ \t]*|[\t)+|[\n]', ' ', name)
    newName = newName.replace(',', '')
    newName = newName.strip()
    return newName.lower()


def getFirstLastName(name):
    splitName = re.split("\s+", name, 0)
    last = splitName[-1]
    first = splitName[0]

    return first + ' ' + last

if __name__ == '__main__':
    main()
    input('Done')
