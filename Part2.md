# Pac-Man Project - Part 2: Updates, Git Workflow, and Securing Sensitive Information

## **Overview**
In Part 2 of the Pac-Man Project, you will collaborate with your team to implement updates and enhancements to the Pac-Man game. This phase focuses on:
1. Renaming components and updating game assets.
2. Securing sensitive information by removing it from Git history and preventing future exposure.
3. Implementing a CI/CD pipeline to automate testing using GitHub Actions.
4. Conducting pull requests and performing code reviews.

---

## **Objectives**
1. **Rename components and implement updates**
2. **Secure sensitive information**
3. **Implement a CI/CD pipeline for automated testing**
4. **Conduct pull requests and perform code reviews**

---

## **Steps for Part 2**

### **1. Rename Components and Implement Updates - 20 points**
Uh oh, we forgot that player should actually be named Pacman. Rename all appropriate files, branches, code, and dependencies to reflect this name change. Ensure you maintain a clean Git history in this process.

*Hint: Using `grep` and `sed` can help streamline this process.*

In your report, describe the method you used for renaming, and if you employed a command-based approach, include the commands you used

---

### **2. Secure Sensitive Information - 40 points**
A `.env` file containing sensitive information was mistakenly committed to the repository. To ensure security:
- Stop tracking the `.env` file in Git.
- Remove any sensitive data from the Git history to prevent access via past commits.

*Hint: Use `.gitignore` to exclude `.env` from future commits and `git filter-branch` or `git rebase` to clean up the repository history.*

---

### **3. Implement a GitHub Actions CI/CD Pipeline - 25 points**
Create a CI workflow in `.github/workflows/ci.yml` that performs the following actions:

#### **Triggering Events**
- Run the workflow on:
  - **Pushes** to the `main` branch.
  - **Pull requests** targeting the `main` branch.

#### **Job Setup**
- Use `ubuntu-latest` as the runner.
- Configure the job for Python 3.10.

#### **Steps**
1. **Checkout the Code**
   - Use `actions/checkout` to retrieve the repository’s contents.

2. **Setup Python Environment**
   - Use `actions/setup-python` to install Python 3.10.

3. **Install System Dependencies**
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3-pygame xvfb
   ```

4. **Install Python Dependencies**
   ```bash
   python -m pip install --upgrade pip
   pip install pytest pytest-cov flake8 black pygame
   ```

5. **Check Code Formatting with Black**
   ```bash
   black --check --diff .
   ```

6. **Lint Code with Flake8**
   ```bash
   flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
   flake8 . --count --exit-zero --max-complexity=30 --max-line-length=100 --statistics
   ```

7. **Run Tests with Pytest**
   ```bash
   xvfb-run -a pytest --cov=./ --cov-report=xml
   ```

*Note: Ensure the pipeline executes in the correct order and follows best CI/CD practices.*

---

### **4. Conduct Pull Requests and Perform Code Reviews - 10 points**
Ensure proper collaboration by:
- Submitting pull requests for changes if needed.
- Reviewing and approving team members' code updates before merging if needed.
- Providing constructive feedback on improvements and code quality if needed.

---

### **5. Report - 10 points**
Write a markdown report (2-3 sentences) in the main branch outlining each team member’s contributions to the project. Be honest about the work completed and the role each person played.

**Note**: If you feel that a team member misrepresented their contributions, make a private Piazza post to address the issue. We will verify reports to ensure fairness. Regardless, we will be checking to see if what the report says aligns with what each person did

---
