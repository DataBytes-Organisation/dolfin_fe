# How to get setup
1. Download a good IDE: https://code.visualstudio.com/download
2. Install python, this code base is tested on Python 3.10: https://www.python.org/downloads/
3. clone the repo down: git clone <repo-name>
4. Change directory to the <repo-name>/frontend directory
5. Create a python virtual env:
    Windows: python -m venv venv
    Linux: python3 -m venv venv or python -m venv venv
6. Activate the Virtal environment:
    Windows: venv/Scripts/Activate
    Linux: source venv/bin/activate
7. Install the project requirements:
    pip install -r requirements.txt or pip3 install -r requirements.txt


# How to contribute
1. do the setup steps
2. Get assigned a task from the project board: <insert link to trello or whatever here>
3. create a branch and check out that branch:
    command line: git checkout -b <your-branch-name>
4. Start writing your code
5. When you wish to push the changes you have made to your branch
    add the changes: git add .
    commit the changes: git commit -m "some-message"
    push the changes: git push


# Tests: how and why
1. WHY: 
The tests serve as live documentation, they are a true representation of the current state of the code base

2. HOW:
The tests can be run using pytest or using coverage (which uses pytest and provides handy tools to figure out how much of the codebase is covered by the tests)
command to run from the /frontend directory:
coverage run -m pytest

# Run the application locally:
1. Make sure you are inside the frontend directory
2. Make sure the virtual environment is active
3. run the application:
    Windows: python application.py
    Linux: python3 application.py

# Things to keep in mind

The Zen of Python: https://peps.python.org/pep-0020/


