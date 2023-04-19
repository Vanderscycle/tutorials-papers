# first thing with bash: change the file's permission
# chmod +x <nameOfScript>.sh
# to find which bash dialect we are using 
# which bash (in our case returned /bin/bash)

# on top of the file we use shebang(#!)and location of bash 
#!/bin/bash

# ECHO COMMAND
# echo is a command that outputs the string passed as arguments
echo hello World!

# VARIABLES
# Uppercase by convention
# Letters,numbers,underscores
NAME='Dick'
# in the video, Brad used string markers but that would output as a literal string
echo My name is ${NAME}

# USER INPUT
# -p (prompt the user)
# read -p 'Enter your name:' NAME
# echo hello $NAME, nice to meet you!

# SIMPLE IF STATEMENT
# of note you need a space before and after each brackets
if [ $NAME == 'Henri' ]
then 
    echo 'Your name is Henri (simple IF)'
#fi (end of if statment)
fi

# IF-ELSE
if [ $NAME == 'Henri' ]
then 
    echo 'Your name is Henri (simple IF-ELSE)'
else
    echo 'You name is NOT Henri'
#fi (end of if statment)
fi

# ELSE-IF (elif)
if [ $NAME == 'Henri' ]
then 
    echo 'Your name is Henri (ELIF)'
elif [ $NAME == 'Bro' ]
then
    echo 'You are my tru Bro'
else
    echo 'You name is NOT Henri and neither are you my bro'
#fi (end of if statment)
fi

# COMPARAISON
NUM1=31
NUM2=5

if [ $NUM1 -gt $NUM2 ]
then
    echo $NUM1 is greater than $NUM2
else
    echo $NUM1 is less than $NUM2
fi
########
# val1 -eq val2 Returns true if the values are equal
# val1 -ne val2 Returns true if the values are not equal
# val1 -gt val2 Returns true if val1 is greater than val2
# val1 -ge val2 Returns true if val1 is greater than or equal to val2
# val1 -lt val2 Returns true if val1 is less than val2
# val1 -le val2 Returns true if val1 is less than or equal to val2
########

# FILE CONDITIONS
FILE='test.txt'
#-f check if its a file (only check for files and not folders)
#-e check if exits (doesn't discriminate between file or folders)
# touch test.txt to create the file
if [ -f $FILE ]
then
    echo $FILE is a file
else
    echo $FILE is not a file 
fi
########
# -d file   True if the file is a directory
# -e file   True if the file exists (note that this is not particularly portable, thus -f is generally used)
# -f file   True if the provided string is a file
# -g file   True if the group id is set on a file
# -r file   True if the file is readable
# -s file   True if the file has a non-zero size
# -u    True if the user id is set on a file
# -w    True if the file is writable
# -x    True if the file is an executable
########

# CASE STATEMENT
read -p 'Are you 21 and over?Y/N': ANSWER
case $ANSWER in
    [yY] | [yY][eE][sS])
        echo 'You can have a beer :)'
        ;;
    [nN] | [nN][oO])
        echo 'No beer 4u T_T'
        ;;
    *)
        echo 'Please enter y/yes or n/no'
esac

# SIMPLE FOR LOOP
NAMES='Bro Brodette Bromeister'
for NAME in $NAMES
    do
        echo Hello $NAME
done
#touch 1.txt 2.txt 3.txt
# FOR LOOP TO RENAME FILES 
# FILES=$(ls *.txt)
# NEW='new'
# for FILE in $FILES
#     do
#         echo Renaming $FILE to new-$FILE
#         mv $FILE $NEW-$FILE
# done

# WHILE LOOP - READING file line by line
#index (iterator)
LINE=1
while read -r CURRENT_LINE 
    do
        echo  $LINE:$CURRENT_LINE
        ((LINE++))
done <'./lorem.txt'

# FUNCTION
function sayHello(){
    echo 'Hello World'
}
sayHello

# FUNCTION WITH PARAMS
function greet(){
    #positional parameters
    echo 'Hello, I am' $1 'and I am '$2
}
greet 'Henri' '31' 

# CREATE FOLDER AND WRITE TO FILE
mkdir hello
touch './hello/world.txt'
# >> output to
echo 'Hello World' >> './hello/world.txt'
echo 'Created ./hello/world.txt'