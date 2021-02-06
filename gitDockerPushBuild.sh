#!bin/bash
# script that add all files, asks for a commit message and then push to git (may have to use the .env for passwords)
# also pushes to docker hub if changes are detected in the ./datastructure folder

# This is the part where we want to see if there are any changes to the docker container
# https://carlosbecker.com/posts/git-changed/
git diff --quiet HEAD $REF -- ./dataStructures/ || STATUSDOCKER='changed' #! have another look it is possible that this isn't rebuilding when there are changes to ./dataStructures
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

# we did docker first as otherwise it will not detect the changes and rebuild the container

BRANCH=$(git rev-parse --abbrev-ref HEAD)
git add * 
read -p "Enter your commit message": COMMITMESSAGE  
git commit -m"${COMMITMESSAGE}"
if [[ -n '$(git status - porcelain)' ]]
then
    echo "Pushing data to remote origin/"$BRANCH
    git push #-u #origin/$BRANCH
    echo 'git status:'
    git status

else
    echo "Your branch is up to date with origin/"$BRANCH
    echo 'resetting the commit'
    git reset --soft HEAD~1
fi


# if the branch is ahead by {x} commits it will display them
# git log origin/master..HEAD
# when there's too many commits
#git reset --soft HEAD~3
# super usefull explanation of checkout
# https://stackoverflow.com/questions/20101994/git-pull-from-master-into-the-development-branch