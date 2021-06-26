# alternatives to awk
# https://www.gnu.org/software/gawk/manual/gawk.html

#cat (or bat) although bat is vim like
cat ~/.zshrc
grep '#' ~/.zshrc # prints every line that has a '#'
#bad don't do
cat ~/.zshrc | grep '#'
# all that grep does is searches for text but doesn't replaces it

# awk is a programming language
awk '{print $0}' ~/.zlogin # replaces cat ($0 means the entire line)
awk '/#/' ~/.zlogin # prints all the commented lines
awk '/gpg/' ~/.zlogin #pirnts all lines that contains gpg

#fine tuned control searches
awk '$1 == "#" { print $2 }' ~/.zlogin # if the first field contains a hastag (the line is a comment) print the second columne
awk '$2 ~ "test" { print $4 }' ~/.zlogin# prints the 4th column (index 3) of the second column item matching (not exactly) test
# fuzzier 
awk '$2 !~ "http" { print $4 }' ~/.zlogin # outputs the 4th column of every line not containing http.
awk '{print $1, $4}' ~/.zlogin

# replace head
awk '(NR>=0 && NR<=11){print} (NR==11){exit}' ~/.zlogin #NR number of records

grep -1 'dir' ~/.zlogin #case insensitive in grep
sed '/[Dd]ir/!d' ~/.zlogin
# can be done the same in awk
awk 'tolower($0) ~ /dir/' ~/.zlogin

#IMPORTANT 
# AWK shines for piped commands (e.g)
ps | awk '(NR>=2){print$1}'   #get the pid of the running process and removes the PID column name
# very roundabout way of doing things but... we can use xargs to pipe and execute commands on each numbers
ps | awk '(NR>=2){print$1}' | xargs -t -n 2 ps -p





#WARN: for hi file :hi (tells all the highlights)
