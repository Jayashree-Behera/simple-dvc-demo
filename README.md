create env
```bash
conda create -n wineq pthon=3.7 -y
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

download the data from
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

Initialize a repository in simple_app (main working folder). This will be our repository when we git push
```bash
git init
```

Connect dvc to this repository and add the data to it
``` bash
dvc init
dvc add data_given/winequality.csv #dvc will start tracking this file from here onwards
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

