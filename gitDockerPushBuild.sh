#!bin/bash
# see if there are any files in demonstrations changed?
# file that pushes add all files, asks for a commit message and then pushes yo git (may have to use the .env for passwords)
# the second goal is also to build and then push changes to docker hub
BRANCH=$(git rev-parse --abbrev-ref HEAD)
#git add * # because of the -a flag no need to use git add *
# git commit -a -m"${COMMITMESSAGE}"
read -p "Enter your commit message": COMMITMESSAGE
if [ -n '$(git status - porcelain)' ];
then
    echo "Your branch is up to date with origin/"$BRANCH
else
    git status
    echo "Pushing data to remote origin/"$BRANCH
    git push -u origin $BRANCH
fi

