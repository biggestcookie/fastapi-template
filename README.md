# FastAPI-Template

[GitHub repository](https://github.com/biggestcookie/fastapi-template)

[Glitch live demo](https://glitch.com/~fastapi-template)

## Setup

1. [Install Python 3.6 or higher.](https://www.python.org/downloads/)
2. Install pip dependencies with `pip install -r requirements.txt`
   or `pip3 install -r requirements` for Mac/Linux users.
3. Copy or rename `.env_example` to `.env` in the root of the project folder.
4. Optionally [create a GitHub personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) and store it under `github_token` in your `.env` file to run the GitHub example routes.
5. Run the application with `uvicorn main:app --reload`

In addition, for VSCode Users:

1. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   and [Pylance extension](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance).
2. Recommended: Install the [VS Intellicode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) extension for better code suggestions/completion.
3. VSCode tasks are included in this repo as well: press 'F1' or 'Ctrl + Shift + P' and select 'Run Tasks' to access them.
4. You may also run or debug the application using the included debug profile.

## Developing with FastAPI

- [FastAPI Docs](https://fastapi.tiangolo.com/)

- [Python Types for FastAPI](https://fastapi.tiangolo.com/python-types/)
