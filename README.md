# Todoist-Script

---

## Description

This script aims to connect [Todoist](https://todoist.com/) to a local database of SCRUM files written in Markdown.
The idea is simple: 
  1. Write out your personal todo for the day or week, or start an empty Markdown file with the Sprint title.
  2. The script takes care of synchronizing the work that is in Todoist, and the SCRUM paper, by exchanging tasks with the markdown file. (Markdown Sync)

However the project has expanded beyond that initial idea.

## Current Capabilities

- Shifting the due time for the task of the day by however among you want +/-00:00
  - Example: ```shift +02:00``` will move all the task for the day by two hours in case you slept in.
    
# Future Features

- Generating time-block task for the current sprint so that I can not spent the extra amount of time setting up my Sprint work due. (automating SCRUM workload)