<h1 style="text-align: center;">Git and Github Exercise</h1>

<p style="text-align: center;">Last Revised January 13, 2025</p>

Due: PDF \
Assignment type: Individual

#### INSTRUCTIONS
Perform the following steps in order, and answer the associated questions as you go along. To submit, upload a pdf with responses to the items marked as questions.

Before beginning the steps below, select one member of your team to create a repository in their Github account named `ist-303-team-X`, where X is your assigned team number. This person should complete the steps below first so that the other members will see the initial files.


1) Clone the github repository created above to a local repository with the same name
- >**Question G-1**: provide the github repository link.
2) Make `ist-303-team-X` the working directory (local repo)
3) If the repo is empty (you are the first member in your team to complete these steps), create three new text files in the current directory named _file1.txt_, _file2.txt_, and _file3.txt_. If you see files in the repo, create a new text file in the current directory with a similar naming structure but increment the number to the next highest number (for example if the repo has a _file4.txt_, then you create _file5.txt_)
4) Run the command `git status`
- >**Question G-2**: Describe the results of step 4.
5) Stage the text file(s) created previously, preparing to commit the changes

6) Commit the changes and include a brief message describing the changes
7) Modify the contents of _file2.txt_ by adding a line that contains two words: your favorite color and your favorite fruit, e.g. "blue persimmon"
8) Rename _file1.txt_ by appending an underscore along with your initials. If the file is _file1.txt_, you would rename to _file1_GH.txt_. Each group member will add their initials so that by the 4th group member it will look like _file1_GH_DF_JS_MV.txt_. 
- >**Question G-3**: Name the command you used to change the file name.
9) Run the command `git status`
- >**Question G-4**: Describe the results of step 9.
10) Commit your changes with a brief message detailing the changes.
11) Run the command `git log` (exit git log with `q`)
- >**Question G-5**: Attach a screenshot of the results of step 11.
12) Push your changes to the github.com repository.
13) Create a virtual environment named `venv` in the current directory
14) Run the `git status` command. Note the results of the above step.
15) Open the .git/info/exclude file in a text editor, add the text `venv` on a new line and save the file.
16) Run the `git status` command.
- >**Question G-6**: Compare the above output with the output prior to editing the .git/info/exclude file. What does this tell you about how git works?

- >**Bonus Question**: Explain the difference between the `git fetch` and `git pull` commands.

---
#### RESOURCES: 
Read about git fetch [here](https://www.atlassian.com/git/tutorials/syncing/git-fetch)