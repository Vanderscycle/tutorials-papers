#!/bin/bash

#sed: stream editor (super usefull with cat or echo anything streams)
# sed uses regex to find the stream pattern and you can expand using -E flag

#substitution
# sed search for the word "find" and when found replace it with the word "replace" (first instance only)
#sed 's/find/replace/'
#example 2 (< readfrom > writetofile)
sed 's/o/O/' < sedRandom.txt > sed-test
# global substitution g is the global flag
sed 's/o/O/g' < sedRandom.txt > sed-test
# often we want to pipe terminal commands into sed
echo "henri" | sed 's/henri/DT/'
echo "the emacs file manager is dires" | sed 's/red/green/' # in this example it is looking for a specific string
# take from a file and write to that file
sed -i 's/find/replace/g' sed-test # filename
# find the line that matches a pattern and then enact a pattern on that line
tldr sed | sed '/Replace/s/the/THE/' # add g if you want all instances in the line

#deletion
tldr sed | sed '/line_pattern/d' #d being the deletion flag
cat /etc/shells | sed 's/usr/u/g'
# multiple commands (requires -3 flag)
cat /etc/shells | sed -e 's/usr/u/g' -e 's/bin/b/g'
# if the pattern yo are looking for contains "/" you can use "|" as te separator
cat /etc/shells | sed -e 's|/usr|u|g' -e 's/bin/b/g'

#filter (print specific lines)
cat /etc/shells | sed -n '/usr/p' #p for printing

# remove all white spaces at the end of each lines
sed -i 's/ *$//' sed-test 
sed -i 's/[[:space:]]*$//' sed-test
# delete empty lines
cat sed-test | sed '/^$/d'
# replace all lowercases with uppercases
sed 's/[a-z]/\U&/g'
sed 's/[a-z]/\L&/g' # lowercase (L)

# replacement to head/tail
sed 11q ~/.zshrc # first 11 lines
awk 'NR < 13' ~/.zshrc # better
