import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()

WAIT_TIME = 12

START_PAGE_LINK = "https://github.com"
LOGIN_PAGE_LINK = "https://github.com/login"

USERNAME = os.getenv("USERNAME_GITHUB")  # "VladislavTest"
PASSWORD = os.getenv("PASSWORD_GITHUB")  # "SecondTestAcc123"

NAME_NEW_REPOSITORY = "test_rep"
NEW_REPO_NAME = "new_rep"

README_TITLE = "README.md"
TEXT_TO_README = \
    """<h1>hello Readme</h1>
I created you with a few problems, but...
if you here, i have a success!!!! 
Cheers !!!"""

