# Learning Git and GitHub - My First MLOps Tool

Welcome to my Git and GitHub learning repository! This repository is dedicated to my journey of learning **Git** and **GitHub**, which are essential tools for version control in MLOps and software development.

## Why Git and GitHub?

- **Git**: A distributed version control system that helps track changes in code and collaborate with others.
- **GitHub**: A platform for hosting Git repositories, enabling collaboration, code sharing, and project management.

This repository documents my hands-on practice with Git and GitHub as I prepare to use them in MLOps workflows.

---

## Project Structure

Here’s the structure of the repository:

`
├── data/
│   ├── raw/                   # Raw data collected from the database
│   └── cleaned/               # Cleaned and preprocessed data
├── main.py                    # Main script to run the workflow
├── data_collection.py         # Script for collecting data from the database
├── feature_engineering.py     # Script for feature engineering tasks
├── model_trainer.py           # Script for training the machine learning model
└── requirements.txt           # List of required Python libraries
`

## Key Git Commands Used

Below is a list of the key Git commands I used in this project, along with their descriptions:

| Command                     | Description                                      |
|-----------------------------|--------------------------------------------------|
| `git init`                  | Initialize a new Git repository.                 |
| `git checkout -b <branch>`  | Create and switch to a new branch.               |
| `git add <file>`            | Stage changes for commit.                        |
| `git commit -m "msg"`       | Commit changes with a message.                   |
| `git merge <branch>`        | Merge changes from one branch into another.      |
| `git log`                   | View the commit history.                         |
| `git status`                | Check the status of the working directory.       |
|--------------------------------------------------------------------------------|

## What I Did in This Repository

1. **Initialized a Git Repository**:
   - I started by creating an empty Git repository using the `git init` command.
   ```bash
   git init
  
   git add requirements.txt main.py

   git commit -m "Initialized a repo and installed all the required packages"


2. **Created a new branch and Collected data from a Database**:
   - I wrote a Python code to collect the data from database and did train test split and save the data in `data/raw` folder
   ```bash
   git checkout -b get_data_from_database

   git add main.py data_collection.py

   git commit -m "data collected from Database"

3. **Created a new branch and Label Encoded the target column**
   - I cretaed a new branch and wrote a code to Label encode the data and saved data in `data/cleaned` folder
   ```bash
   git checkout -b  "feature_engineering"

   git add main.py feature_engineering.py

   git commit -m "feature engineering code added"

4. **Created a new Branch and Trained a model**
   - I created a new ranch to write a code of model tranig
   ```bash 
   git checkout -b  model_trainer
   
   git add main.py model_trainer.py

   git commit -m "model trainer code aadded"

5. **Merged all the barnches**
    ```bash 
    git checkout master 

    git merge get_data_from_database

    git merge feature_engineering

    git merge model_trainer

    git commit -m "merged all the branches"
   
    git add . 

    git commit -m "added remaining files"

6. **Renamed branch name from master to main**
   ```bash
    git branch -m master main

7. **Pushed the code to GitHub**
   - Created a public repo on github and ran the following command on cmd on loacl repo
   ```bash
    git remote add origin https://github.com/Shreycasm/Basics-of-Git-and-GitHub.git 

    git push -u origin main


