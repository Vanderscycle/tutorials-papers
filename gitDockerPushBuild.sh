#!bin/bash
# script that add all files, asks for a commit message and then push to git (may have to use the .env for passwords)
# also pushes to docker hub if changes are detected in the ./datastructure folder
BRANCH=$(git rev-parse --abbrev-ref HEAD)
git add * 
read -p "Enter your commit message": COMMITMESSAGE  
git commit -m"${COMMITMESSAGE}"
if [[ -n '$(git status - porcelain)' ]]
then
    git status
    echo "Pushing data to remote origin/"$BRANCH
    git push -u origin/$BRANCH

else
    echo "Your branch is up to date with origin/"$BRANCH
    echo 'resetting the commit'
    git reset --soft HEAD~1
fi
# This is the part where we want to see if there are any changes to the docker container
# STATUSDOCKER=null
git diff --quiet HEAD $REF -- ./dataStructures/ || STATUSDOCKER='changed'
if [[ $STATUSDOCKER == 'changed' ]]
then
    echo 'rebuilding the docker image'
    docker build -t data_structure_app:beta-pre-prod ./dataStructures/
    docker tag data_structure_app:beta-pre-prod  vandercycle/datastructures-python:beta-pre-prod
    echo 'pushing the image to docker hub'
    docker push vandercycle/datastructures-python:beta-pre-prod
    #cleaning up the none docker images
    docker rmi -f  $(docker images -f "dangling=true" -q)
else
    echo 'no change to the container local files'
fi

# if the branch is ahead by {x} commits it will display them
# git log origin/master..HEAD
# when there's too many commits
#git reset --soft HEAD~3
# super usefull explanation of checkout
# https://stackoverflow.com/questions/20101994/git-pull-from-master-into-the-development-branch