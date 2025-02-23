---
marp: true
theme: gaia
#size: 4:3
#_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

# Git and Github Configuration

---

## Github
- create [github](https://github.com) account
- create a test repository
- find repository url for use in git (green clone/code button)
- find email address for use in pushing to remote repo (user settings -> email)

---
## Git
- Install: \
[github guide](https://github.com/git-guides/install-git) or \
[git-scm guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Explore: \
[Git cheatsheet](https://www.git-tower.com/blog/git-cheat-sheet/) \
[Git guide @ github.com](https://github.com/git-guides) \
[Simple guide](https://rogerdudler.github.io/git-guide/) 

---
## OPTIONAL: Powershell Integration for windows

  **POSH-GIT**: PowerShell module that integrates Git and PowerShell by providing Git status summary information that can be displayed in the PowerShell prompt
  - check that powershell version is 5.0+: `$PSVersionTable.PSVersion`
  - check script execution policy: `Get-ExecutionPolicy`
  - if not Unrestricted or RemoteSigned, set to RemoteSigned: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Confirm`

  ---
  ### POSH-GIT cont'd
  - Install: `PowerShellGet\Install-Module posh-git -Scope CurrentUser`
  - Import: `Import-Module posh-git`
  - Add to all hosts (to avoid having to import module each time):`Add-PoshGitToProfile -AllHosts`
  - [Read more here](https://papercutsoftware.github.io/git-from-powershell/#:~:text=Installing%20and%20configuring%20Git%20on%20Windows,-Personally%20I%20prefer&text=Can%20also%20use%20PowerShell%20Module,present%20the%20standard%20CLI%20experience)


---
## Test out your Git install in the Terminal:
  ```
  git --version
  mkdir test_dir
  cd test_dir
  git init
  git status
  ```

---
## Additional Git Configuration (Terminal)
- User name and email (to appear on commits)
- credential manager (for authentication with Github)
- default branch name

---
### User name and email
Each commit includes code changes and information about who made the commit. 
The name and email you set will be used when your local machine makes changes (this is unrelated to your github username and email). 

Can be set:
 - _globally_, for all commits from your computer, or 
 - _locally_ for just a single project. To set globally, use the `--global` option.

---
**user name** (single repo, no `--global` option):
```
git config user.name "Leonardo"
```
**email address** (global example): 
```
git config --global user.email "myemail@hotmail.com"
```

---
Verify your configured user name and email:
```
git config user.name
git config user.email
```

_Note that you can use the noreply github email address structured as:_ 

  **githubUserName**@users.noreply.github.com

---
### Credential Manager
Used to authenticate communication between your local repository and remote repository (log in to Github from Git).
- Check if installed (can choose to install when you install Git): \
`git credential-manager --version`
- If not installed, can download (any OS) installers [here](https://github.com/git-ecosystem/git-credential-manager/releases/tag/v2.4.1)

---
### Set your default branch name (Git)
Github now uses the name "Main" for the initial branch name (used to be "Master").

It is cognitively a little easier if you set your local default branch name to "Main". 

Can set this using:
`git config --global init.defaultBranch main`

---
## [Git test drive](week02_04_slide_firstCommit)

![power drift](https://forgifs.com/gallery/d/186158-5/Kid-power-wheels-drifting.gif)
