# Todoist-Script

---

## Description

This script aims to automate task creation and scheduling for the [Todoist](https://todoist.com/) app. 

## Building

Just make sure you have the libraries listed in the modules. These are:
- request
- json
- todoist-python (although I never used it, You can still acquire it)

## Running

You can run the program from your anywhere in your terminal by adding the following alias to your bash/zsh profile

```alias ptodoist='~/<<<path-to-your-code-repo>>>/.bin.sh'```

The program takes certain arguments to run so in case you are not sure you can run ```ptodoist -h``` to bring up a list of all available commands.

## Current Capabilities

- Shifting the due time for the task of the day by however among you want +/-00:00
  - Example: ```shift +02:00``` will move all the task for the day by two hours in case you slept in.
    
## Future Features

- Generating time-block task for the current sprint so that I can not spend the extra amount of time setting up my Sprint work due. (automating SCRUM workload)
- Generate SCRUM documents written in Markdown to be able to: 
  - Write out your personal todo for the day or week and load these tasks on the current Sprint project.
  - Import tasks, sections, and projects from Todoist into the Current Scrum document.
  - Synchronize the work that is in Todoist, and the SCRUM paper. (Markdown Sync)
