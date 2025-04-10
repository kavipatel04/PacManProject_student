# Part 1

Kavi - Worked on Feature/player, reviewed merges, group leader
Ben - Worked on Feature/item, reviewed merges
John - Worked on Feature/ghost, reviewed merges
Mariia - Worked on Feature/gameboard, reviewed merges
Aarav - Worked on test_player, reviewed marges


# Part 2


John - Created a new branch, set gitignore to ignore .env file, and created a pull request. Approved pull requests. Created a new branch for members to update the report file.

Aarav Naveen - completed part 1 of the project, and replaced all mentions of player with pacman. I used mv to rename the files and grep (grep -r "player" --include="*.py" .) and sed (sed -i 's/player/pacman/g' *.py). Then, I double checked for any stragglers using my IDE's find and replace function to see if I missed any other instances of player. Also created a pull request for this & approved+merged other PRs

Kavi - Created a branch to set up the CICD pipeline. The process required multiple commits, as the only way to test the program was to push and view how the action performed. The set up only includes the environment and setting up depedencies - not the actual tests themselves.