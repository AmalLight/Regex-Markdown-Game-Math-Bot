
import re

# ------------------------------------------------------------------------

print ( 'FIRST step' )

regex = re.compile ( r'ab+' )

test_str = "ababb"

match = regex.match ( test_str )

for groupNum in range (0, len(match.groups())):

    groupNum = groupNum + 1
    
    print ( "Group {groupNum} found at {start}-{end}: {group}".format (
    
            groupNum = groupNum,
            start = match.start(groupNum),
            end = match.end(groupNum),
            group = match.group(groupNum)
        )
    )
