#!bin/bash
BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo $BRANCH
if [ -n "$(git status --branch --porcelain)" ];
then
    echo "Your branch is up to date with origin/"$BRANCH
fi
# STATUSDOCKER=null
git diff --quiet HEAD $REF -- ./dataStructures/ || STATUSDOCKER='changed'
echo $STATUSDOCKER
if [[ $STATUSDOCKER == 'changed' ]]
then
    echo 'rebuilding the docker image'
else
    echo 'no changes'
fi