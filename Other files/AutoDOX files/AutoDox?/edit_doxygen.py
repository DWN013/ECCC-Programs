import re
import csv
import numpy as np
import sys
# Read in the name of the file that should be checked
infile=sys.argv[1]
#print(infile)
# Read from CSV file the patterns to check and the replacement/additions to make
with open('doxygen_scalar_info.csv', newline='') as csvfile:
    patterns = list(csv.reader(csvfile))

#print(np.shape(patterns))
#print(patterns[0])
npatterns,tmp = np.shape(patterns)

# Open the file to edit
fin = open(infile,"rt")

# Loop through each line in the file
# Check each line for a potential variable that should be documented.
# If line contains declaration for variable that should be replaced, generate
# new line with correct information and change in the file.
for line in fin:
    # Loop over the patterns that might be replaced
    pattern_found=False
    for ipattern in np.arange(npatterns):
        var_replace= ":: %s" % (patterns[ipattern][0].lower())
        pattern = [ 'intent', var_replace ]
        doxygen_replacement = "  !< %s \\f$[%s]\\f$" % (patterns[ipattern][1],patterns[ipattern][2])

        if all(i in line for i in pattern):
            pattern_found=True
            x = line.find("!<")
            if (x == -1):
                #No Doxygen, add information end of line
                newline=line.strip('\n')  + doxygen_replacement
            else:
                # Doxygen template found, replace
                #print(line[46::])
                newline=line[0:x] + doxygen_replacement
        elif (pattern_found == False):
            newline=line.strip('\n')
    # Print out the line that is either not changed or has had Doxygen information added
    print(newline)

