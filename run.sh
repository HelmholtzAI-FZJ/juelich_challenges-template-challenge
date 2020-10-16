#!/bin/bash

# Please edit this script
# it should create the following archives:
# 1) evaluation_script.zip (already done, no need to modify)
# 2) challenge_config.zip (arleady done, no need to modify), this is the file you upload to the challenge frontend to create a new challenge
# 3) data_public_leaderboard_phase.zip  (archive to download for the users for the public leaderboard phase)
# 4) data_private_leaderboard_phase.zip (archive to download for the users for the private leaderboard phase)

# Remove already existing zip files
rm -f *.zip *.tar.gz

# Create new zip configuration according the updated code
zip -r -j evaluation_script.zip evaluation_script/*  -x "*.DS_Store"
zip -r challenge_config.zip *  -x "*.DS_Store" -x "evaluation_script/*" -x "*.git" -x "run.sh" -x "raw/*" -x "annotations/train/*" -x "annotations/valid/*" -x "annotations/test/*"

cd annotations
zip -r -j ../data_public_leaderboard_phase.zip train.csv train/ valid/ submission_valid.csv README.md
zip -r -j ../data_private_leaderboard_phase.zip test test.csv submission_test.csv README.md
cd ..
