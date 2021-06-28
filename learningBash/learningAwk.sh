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
# awk treats spaces as the column delimiter use -F flag 
awk -F ":" '{ print $1}' /etc/passwd
# multiple columnms (print)
awk -F ":" '{ print $1 $6 $7}' /etc/passwd
awk -F ":" '{ print $1"\t"$6"\t"$7}' /etc/passwd # a more readable output (specifying tabs between columns)

#more advanced 
awk 'BEGIN{FS=":"; OFS="-"}{print $1, $6, $7}' /etc/passwd #FS = field seperator OFS= output field seperator
# print the last column
awk -F "/" '/^\// {print $NF}' /etc/shells # before the print {} its the search pattern
awk -F "/" '/^\// {print $NF}' /etc/shells | uniq | sort # pipe the output into unique and alphabetical results
# df shows the disk space
df | awk '/\/dev\/nv/ {print $1"\t"$2"\t"$3}'
df | awk '/\/dev\/nv/ {print $1"\t"$2 + 3}' #you can also combine 

# filter the results by the length of the line (only return lines that are greater than 7 chars)
awk 'length($0) > 7' /etc/shells 
awk 'length($0) <= 8' /etc/shells # works multiple 

# ps -rf (all process running on the machine)
pf -ef | awk '{if($NF == "zsh") print $0}' #if the last filed ($NF) == "zsh" print  the entire line
awk 'BEGIN { for(i=1; i<=10; i++) print "the square root of", i, "is",i*i;}'
awk '$1 ~ /^[a,b,c]/ {print $0}' ~/.zshrc # print all lines that begins with either a,b or c

awk '{print substr($0,4)}' /etc/shells # only start printing the 4th character

awk 'match($0, /a/) {print $0 " has \"a\" character at " RSTART}'  /etc/shells

sudo df | awk 'NR==3, NR==2 {print NR, $0}' # print the line number (NR) and the line itself

awk 'END {print NR}' /etc/shells
awk 'END {print NR}' /etc/shells /etc/passwd # oyu can also do multiple files
# probably can do *.py files for example
# WARN: for hi file :hi (tells all the highlights)
