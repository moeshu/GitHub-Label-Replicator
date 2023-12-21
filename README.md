# GitHub Label Replicator

A simple Python script to replicate GitHub labels from one repository to another. Ideal for maintaining consistent labeling across multiple projects.

## Prerequisites

- Python 3
- A GitHub Personal Access Token with repository permissions.

## Usage

1. **Clone this repository**:
  - Use the following commands to clone the repository and navigate into the directory:

  ```bash
  git clone https://github.com/moeshu/GitHub-Label-Replicator.git
  cd GitHub-Label-Replicator
  ```

2. **Run python file**
  - Execute the script with Python. During execution, you'll be prompted to enter the source repository, target repository, and your GitHub personal access token:
  ```python label_replicator.py```

**Source Repository:** Enter the source repository in the format username/repo.
**Target Repository:** Enter the target repository in the same format.
**GitHub Token:** Enter your personal access token when prompted.

## Prerequisites for GitHub Label Replicator

- Ensure you have Python installed on your system. You can verify this by running `python3 --version` in your terminal.
- Your GitHub personal access token should have the repo scope for private repositories or `public_repo` for public repositories.
