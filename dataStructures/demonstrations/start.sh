#!bin/bash

#conda init
# source ~/miniconda2/etc/profile.d/conda.sh
# DESIRED_ENV=NNScraper
# conda activate $DESIRED_ENV 
echo 'Welcome to the Data Structures (DS) Python App'
ORDER=null
while [ $ORDER != 'exit' ]
    do
        read -p 'Type help for a list of available DS to try and exit to leave': ORDER
        if [ -z "$ORDER"  ]
        then
            echo 'please do not enter an empty string'
            ORDER='empty'

        else
            case $ORDER in
                [hH][eE][lL][pP])
                    echo 'Here is the list of available DS'
                    python dataStrutureApp.py
                    ;;
                'empty')
                    ;;
                *)
                    python dataStrutureApp.py --dataStructure $ORDER

            esac
        fi
done
# inside docker 
# docker run -it data_structure_app:beta-pre-prod /bin/bash