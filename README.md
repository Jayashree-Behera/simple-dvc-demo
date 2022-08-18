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
dvc add data_given/winequality.csv
```

Add the current directory contents to staging area: (Use same command to save/update any changes to the repo)
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

 Part 2:

 Create a new repo in your github. To add/update all the local/remote changes made to the repo to your github, do this:
 ```bash
 git remote add origin https://github.com/Jayashree-Behera/simple-dvc-demo.git
 git branch -M main   #renames the master branch as the main branch
 git push -u origin main   #push all the codes/local changes into this github repo to the main branch
 ```