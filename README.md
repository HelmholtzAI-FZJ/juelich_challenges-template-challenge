# Template Challenge

This is a template challenge. If you would like to create a new challenge
at Jülich Callenges, please follow the steps. All the steps are necessary.

## 1) Clone the repository

- `git clone https://gitlab.version.fz-juelich.de/MLDL_FZJ/juhaicu/jsc_internal/superhaicu/vouchers/j-lich-challenges/challenges/template_challenge my_challenge`
- `cd my_challenge`

## 2) Download Raw data

You first need to download the raw data if needed, it does not matter where you put as long as it is acccessible, for instance
yon can put it in the folder `raw/` in `my_challenge`.

## 3) Build annotation files

You need to create annotation splits.
Please check `annotations/generate.py` for more details.
Basically, the script `annotations/generate.py` should be edited
so that it creates annotation files (train.csv, valid.csv, test.csv, submission_valid.csv, submission_test.csv)
based on raw data. The splits can be generated randomly or follow the splits you already
have in your raw data. 

Note that The CSVs should not be heavy, it should not contain images themselves
if your challenge have some. If your challenge have images, you can have a column 
pointing to filenames of the images.

Once you finish editing `annotations/generate.py`, please run it:

`cd annotations;python generate.py`

you will have now the following files in the folder `annotations/`:

- `annotations/train.csv`
- `annotations/valid.csv`
- `annotations/test.csv`
- `annotations/submission_valid.csv`
- `annotations/submission_test.csv`

## 4) Edit the evaluation script

This is one of the most important steps because in this step
you define the metrics that will be used to rank the participants
in the leaderboard.

Please edit `evaluation_script/main.py` for your challenge.
It comes with an example where the accuracy metric is used
for a classification problem. But you can use any set of metrics.
It is a regular python file, so any metric which can be written
in Python could be used. You can use `Scikit-Learn` which already
offers most of the usual metrics.
Basically, the script `evaluation_script/main.py` returns a Python dictionary
containing the metric names as keys and the metric values as values.
You can use as many metrics as you want, the metric that will be used
to rank the participants in the leaderboard will be chosen later in `challenge_config.yaml`.

Here is just one note about how `evaluation_script/main.py` works.
In order to compute the metrics, the participant submission and the annotation files that you generated
previously are opened (e.g., valid.csv or test.csv depending on the challenge phase)
in `evaluation_script/main.py`. The two (participant submission and annotation file) are then compared using the column
that corresponds to the label (e.g., the column `label` in this template challenge).

## 5) Edit challenge_config.yaml

Please dit `challenge_config.yaml` and change everything which is specific to your challenge.
More documentation about the fields is given at <https://evalai.readthedocs.io/en/latest/configuration.html>

The most important parts to modify are the fields in the top of the file, they contain basic information about the challenge.
Plase also change the leaderboard section. In the leaderboard section, please put all the metric names you want to display in the leaderboard.
The metric names correspond to the metric names you defined in `evaluation_script/main.py`.
`default_order_by` defines the metric you use to rank the participants.

Please check carefully all the fields so that it correspond to your needs for the challenge,
such as the starting date and ending date of the different phases and the number of submissions.

## 6) Edit the template files and the logo

Please edit the HTML files in the folder `templates/`. These HTML files
are displayed in the frontend in your challenge page.
Please also modify the logo file `logo.jpg` to have a custom logo for your challenge,
this will displayed in the frontend as well.

## 7) Edit notebook.ipynb

Please edit `notebook.ipynb`. This part is important for the participants. This is given to the participants so that they can
have the challlenge introduced to them and be able to easily understand the problem and start to submit easily. 
Steps such as downloading the data, explanation of the problem, exploratory data analysis, baseline solutions, and example submissions 
should be included.

Here is an example of what it could look like: https://gitlab.version.fz-juelich.de/MLDL_FZJ/juhaicu/jsc_internal/superhaicu/vouchers/j-lich-challenges/challenges/covidx_challenge/-/blob/master/notebook.ipynb
## 8) Edit run.sh

Please edit `run.sh` if needed. This script will make all the archives needed for the challenge. More details are given in `run.sh`.
Here is a short description of the files that `run.sh` need to create:

- `challenge_config.zip`. This archive contains the challenge configuration, this file will be uploaded at the frontend by yourself
to create the challenge
- `data_public_leaderboard_phase.zip`. This archive is given to the users for the public leaderboard phase, so you need to upload
it somehwere in a public link.
- `data_private_leaderboard_phase.zip`. This archive is given to the users for the private leaderboard phase, so you need to upload
it somehwere in a public link.

`run.sh` should work as is, but if you have any a additional files to included in the data archives (such as images), you need to change it.
When `run.sh` is ready, please run it:

`./run.sh`

After running the script, you should have these files:

- `challenge_config.zip`
- `data_public_leaderboard_phase.zip`
- `data_private_leaderboard_phase.zip`

Please then upload the data archives in a public link, and reference the links
in the HTML files in `templates/` as well as in the `notebook.ipynb`

## 9) Upload `challenge_config.zip` to the frontend

- Go to the frontend
- Create a new challenge, then upload `challenge_config.zip`.

This is the last step. One of the administrators should then accept your challenge so that
it becomes public.

Thanks for following this guide, your challenge should be ready now!
