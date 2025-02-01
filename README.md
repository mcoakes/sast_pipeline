# SAST Pipeline for Python with Bandit

# Description

A simple pipeline implementation for vulnerability testing python code


# Insallation and Setup


Repo Settings > Actions > General
Scroll down to Workflow permissions.
Choose “Read and write permissions” for the GITHUB_TOKEN.

Go to your repository on GitHub.
Navigate to Settings > Branches > Add Rule.
Create a branch protection rule for the main branch:
Enable "Require a pull request before merging."
Enable "Require status checks to pass before merging."
Select the Bandit workflow under "Status checks that are required."
Optionally, enable "Require approvals" if you want review enforcement.


Testing PR recognition

