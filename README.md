**GOAL**:

We will make an end-to-end project where we learn the following :
- github deployement
- dvc
- uni testing 

**STEPS**:

create env
```bash
conda create -n wineq python=3.7 -y
```
activate env
```bash
conda activate wineq
```

Create a req.txt file. In windows, create this file manually
```bash
touch reqirements.txt
```
install the req
```bash
pip install -r requirements.txt
```
Then create a "template.py" file that makes all the root directories and files You can later add more files using touch command. Make sure to add a .gitkeep file in each directory and also create a file .gitignore for future purposes.

download the data from
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

Initialize a repository in simple_app (main working folder). This will be our repository when we git push
```bash
git init
```

Connect dvc to this repository and add the data to it
``` bash
dvc init #initialize dvc inside the folder
dvc add data_given/winequality.csv #dvc will start tracking this input file from here onwards
```

Add the current directory contents to staging area ( This is a middle-ground between the github repository and your working copy. A staged file is not yet committed to the repository, but is independent of any further changes to your working copy.): (Use same command to save/update any changes to the repo). This step is important. Without this git push won't update all changes made to the github repo.
```bash
git add .
```
Commit any message/s about your recent work. Here message is "first commit"
```bash
git commit -m "first commit"
```
In case you want to write both commands in one line :
```bash
git add . && git commit -m "update README.md"
```
Now , the data_given folder has a .gitignore that tells git not to upload the winequality.csv file. The dvc file version is created and uploaded to show that the input data file is added to dvc. 


 Next step is to create a new repo in your github that will mimic this project. To add/update all the local changes made to the repo to your github, do this:
 ```bash
 git remote add origin https://github.com/Jayashree-Behera/simple-dvc-demo.git  #this step is done only once to link the repo to your project
 git branch -M main   #renames the master branch as the main branch. 
 git push -u origin main   #push all the codes/local changes into this github repo to the main branch
 ```

 A cheat sheet for other git commands can be found here:
 https://gist.github.com/cblunt/860360

**tox commands**:

A package that runs the codes in all environments, has the req.txt file and also does the pytest check. Properties and command lines:
```bash
tox # runs the tox.ini file.It runs req.txt file only first time. Use below command to run it again
tox -r # runs req.txt file again
pytest -v # command line in tox.ini that runs the files in the "tests" folder 
test_config.py # runs the tests
```

**setup commands**:
```bash
pip install -e. # run setup.py that makes/installs package/s
python setup.py sdist bdist_wheel # creates a tar file that can be shared to download the libraries involved.
```

**dvc commands**:
```bash
dvc repro # tracks and runs the stages if not run before.
dvc metrics show # tracks and shows a specific part (here, metrics) of a stage
dvc metrics diff # shows the differences of all results of all metrics used in past and present
```
**SUMMARY** :
