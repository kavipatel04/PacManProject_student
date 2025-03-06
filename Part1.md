# Pac-Man Project - Part 1: Collaborative Development

## **Overview**
In this project, you and your team will collaboratively build a Pac-Man game in Python. The focus is on implementing key game features, using version control with Git, and writing tests to ensure the functionality of your code. Part 1 covers feature development, collaboration via Git, and creating tests.

## **Objectives**
1. **Implement key Pac-Man game features**:
   - Game board
   - Player (Pac-Man)
   - Ghosts
   - Items (e.g., dots, power pellets)
2. **Use Git for collaborative development**:
   - Work in separate branches for each feature.
   - Submit pull requests (PRs) for code review.
3. **Write tests**:
   - Ensure that all features are properly tested.
   - Identify and fix bugs through testing.



## **Tasks and Workflow**

### **1. Fork the Repository (10 points)**
- **Group leader**: Fork the upstream Pac-Man repository to create the group's own repository on GitHub.
- **Group leader**: Add team members (including KaranJain22 and mdurrani808) as collaborators to the repository.
- **All group members**: Clone the group's repository to your local machine, ensuring your remote origin points to the group's repository.

**Note**: After cloning, you should also configure your Git to track the upstream repository (original repository) to stay updated with any changes made to it.

### **2. Branch Workflow (10 points)**
Each team member will work on a specific feature. Create separate branches for each feature. The branch names should match the feature assigned:
- `feature/player`
- `feature/ghost`
- `feature/game_board`
- `feature/item`

Steps for branching:
- Create a new branch based on the main branch.
- Work only on the feature assigned to you within that branch.
- Commit and push your changes to the remote repository.

### **3. Implement Features (10 points)**
You will find corresponding files for each component in the repository:
- **game_board.py**: Manages the game grid.
- **player.py**: Implements Pac-Man's movement and interactions.
- **ghost.py**: Handles ghost behavior and movement.
- **item.py**: Manages items such as dots and power pellets.

Instructions:
- Implement the feature in the corresponding file, ensuring that each feature is developed within its respective branch. To "implement" the feature, uncomment the code in the file.
- If you mistakenly commit code to the wrong branch, fix the Git history by moving your changes to the correct branch and then push it.

### **4. Write Tests (25 points)**
Fill in tests for your code in the corresponding test file (e.g., test_player.py for player.py). Follow the example tests to model your tests.
- Use the **pytest** framework for filling in tests.
- If you find an error, make sure to create an issue on GitHub about it in the base repository

You can also check the [PyTest documentation](https://docs.pytest.org/en/stable/) for more details if you are interested.

### **5. Collaborate Using Pull Requests (20 points)**
- Each team member must submit a pull request (PR) to merge their feature branch into the main branch.
- All push requests to the main branch must be reviewed by **at least one team member** before merging.
- Each team member is responsible for making and/or reviewing at least one other member’s PR. This ensures that everyone is actively involved in the code review process.
- Once the PR is reviewed and approved, it can be merged into the main branch.

### **6. Report (10 points)**
Write a markdown report (2-3 sentences) in the main branch outlining each team member’s contributions to the project. Be honest about the work completed and the role each person played in implementing features, filling in tests, and contributing to the collaboration process.

**Note**: If you feel that a team member misrepresented their contributions, make a private Piazza post to address the issue. We will verify reports to ensure fairness. Regardless, we will be checking to see if what the report says aligns with what each person did.


## **Grading Criteria**
Groups will receive the same grade unless a team member did not contribute meaningfully. In such cases, grading will be adjusted accordingly.


## **Additional Notes**
- **Git Workflow**: In real-world development, you would typically test your code locally first, ensuring that everything works as expected. Once the code is tested and ready, you would then push your changes to the feature branch on the remote repository. This allows your teammates to review the code and run additional tests before merging it into the main branch.
However, for this project, testing will only be done on the main branch after all the features have been implemented.
