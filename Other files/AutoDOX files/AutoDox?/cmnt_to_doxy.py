import sys
import os

#Pre-defined variables
lineBrk = "!!<!---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->"

#Input filename that needs conversion, seperate extension from name
inName = sys.argv[1]
fileName, file_exten = os.path.splitext(inName)

#Output file result
outName = fileName + "_result.txt"

#Open a file to edit
with open(inName, 'r') as inFile, open(outName, 'w') as outFile:
    outFile.write("!! Changes made before git 2018 and git version control can be found \\ref " + fileName + "_change_log \"here\" while changes after\n")
    outFile.write("!! this time can be found in git (logs and histories)\n!!\n!> \\file \n!> \page change_logs_pre_git Changelogs before 2018 (pre-git version control)\n")
    outFile.write("!! \n!!<table> \n!!<caption id=\"" + fileName + "_change_log\">Changelog for " + fileName + "</caption>\n")
    outFile.write(lineBrk + "\n!!<tr><th>Date</th>                   <th>User</th>                      	       <th><b>Comments</b></th>		 					   	</tr>\n" + lineBrk)

    counter = 0
    #If a '|' is encountered
    #If a '/' is encountered
    #If a '-' is encountered
    for line in inFile:
        pipe_line = line.replace('|', "<td>")
        slash_line = line.replace('/', "<br>")
        dash_line = line.replace('-', "<li>")
        
        
    outFile.write(lineBrk + "\n!!</table>")
    
    inFile.close()
    outFile.close()
