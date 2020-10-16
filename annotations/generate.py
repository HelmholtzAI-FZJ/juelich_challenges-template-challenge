import uuid
import random
import pandas as pd
# Please modify this script
# This script should take raw data you have
# and generate the data splits in a CSV file:
# train.csv, valid.csv, test.csv
# - train.csv would be given to the participants
# - valid.csv is the public leaderboard data with the **labels**, so it will not be given to the participants.
# - submission_valid.csv is the same as valid.csv but the labels column contains some dummy values,
#   this will be given to the participants as a dummy submission for the public leaderboard phase
# - test.csv is the private leaderboard data with the **labels"", so it will not be given to the participants.
# - submission_test.csv is the same as test.csv, the difference is that the labels column contains dummy values,
#    this will be given to the participants as a dummy subbmission for the private leaderboard phase

# WARNING: in the following script we just generate the CSVs randomly, please edit this script

def generate_dummy(nb):
    names = [uuid.uuid4() for _ in range(nb)]
    labels = [random.choice(("label1", "label2", "label3")) for _ in range(nb)]
    df = pd.DataFrame({"name": names, "label": labels})
    return df


nb_train = 10000
nb_valid = 1000
nb_test = 1000


train = generate_dummy(nb_train)
valid = generate_dummy(nb_valid)
test = generate_dummy(nb_test)

train.to_csv("train.csv", index=False)
valid.to_csv("valid.csv", index=False)
test.to_csv("test.csv", index=False)

valid["label"] = ""
valid.to_csv("submission_valid.csv", index=False)

test["label"] = ""
test.to_csv("submission_test.csv", index=False)
