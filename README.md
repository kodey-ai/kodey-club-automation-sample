
# kodey-club-automation-sample

This repository is an example Kodey.ai Coding Agent Workflow

## Objectives

In this sample, we will explore how Kodey.ai can read external api documentation related to club automation and create python apps for them.

## Project Setup & Steps 

1. Signup for a new Kodey.ai account or login to your existing Kodey.ai environmenty (link-here)
2. Configure your Kodey.ai integrations to the desired issue tracker and cloud git provider.
3. Fork this repository, and clone it to the cloud git provider of your choosing (Github, Azure DevOps, Bitbucket)
4. Make sure you have dev branch. If not create one, kodey will be creating all the new branches against dev.
5. Create the sample issue / work item in your issue tracker. Copy and Paste the issue description from below.
6. Execute the below prompt in the Kodey.ai chat UI
7. Validate the commits and pull requests in your cloud git provider

### SAMPLE PROMPT - EPIC FHIR AllergyIntolerance.Search(R4) API Sample
```
    platform: github | bitbucket | azure | gitlab (choose one of yours)

    repository to work on: kodey-clubautomation-sample

    branch name to create: feature/kodey-clubautomation-sample-v3

    programming language to use: python

    Information to agent: Do as the steps below are defined one by one. You are working in <platform> repo so make sure to use tools related to <platform> repo.
    NOTE: You should write the actual implementation of code not just comments.  If you need to use credentials , read the credentials from env variables.

    Steps:

    step 1: Create a new branch with name <branch name to create> and then do the steps below.

    step 2: Using webcrawler tool, understand how to make an authentication to Daxko Api https://docs.partners.daxko.com/tutorials/authentication

    step 3: Create a new file utils.py where the authentication for oauth of Daxko api from step 2 should be implemented.

    step 4: Using webcrawler tool, understand how to make request to an endpoint which gives member packages from url https://docs.partners.daxko.com/openapi/ClubAutomation/v1/#tag/Members/operation/get-user-packages and create a new file to implement that request in python. FYI: Remember to use the authentication token retrieved from step 3. 

    step 4: Using webcrawler tool, understand how to make request to an endpoint which gives member profile from url https://docs.partners.daxko.com/openapi/ClubAutomation/v1/#tag/Members/operation/get-user-profile and create a new file to implement that request in python. FYI: Remember to use the authentication token retrieved from step 3.

    step 5: Create a new main.py file which will allow us to call the methods and functions created above. FYI: Read the credentials from env variables.

    step 7: Also create .gitignore file which will include the env files and others.

    step 7: Update the readme file to include the detail about the app and also instruction on how to run the app.

    step 8: Create a new pull request from the above created branch with title "KODEY CLUB AUTOMATION SAMPLE V3" and body "club automation documentation reading and scripting".

    step 9: Update this issue to closed/done status
```

## Once you have set the description of the issue in your relavant system. You need to use kodey UI Chat and execute below statement to get the work done. 

### Github Issue and Github Repo
```
   Get the issue with id <issue_id> from github repo and do as the description of the issue says step by step.
```

### Azure Repo Issue and Azure Repo
```
   Get the issue with id <issue_id> from azure repo and do as the description of the issue says step by step.
```

### Jira Issue and Bitbucket Repo
```
   Get the issue with id <issue_id> from jira and do as the description of the issue says step by step.
```

## Confirming Successful Sample Outputs

1. Confirm that the branch was created on the issue / work item
2. Confirm that the code created in the associated pull request contains the following
3. Confirm that the work item/issue/ticket in your relevant issue tracking platform is updated.
