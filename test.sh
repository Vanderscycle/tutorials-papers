#!bin/bash
BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo $BRANCH
# STATUSDOCKER=null
git diff --quiet HEAD $REF -- ./dataStructures/ || STATUSDOCKER='changed'
echo $STATUSDOCKER
if [[ $STATUSDOCKER == 'changed' ]]
then
    echo 'rebuilding the docker image'
else
    echo 'no changes'
fi