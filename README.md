### Fetch Git Hub user activity through command line

## How to run the script
- Generate GitHub token for interacting with GitHub API's
- Goto `Github settings> Developer settings > Personal Tokens`
- Generate personal token here and copy it
- Clone this repository using `git clone https://github.com/srisaipasupuleti/gh-user-activity-cli.git`
- Create virtual env using `python venv -m venv` and activate it using `venv\Scripts\activate`(in windows)
- Install all the requirements `pip install -r requirements.txt`
- Assign the generated token value to ghToken variable in .env file
- Run following command along with Github username for which you want to fetch the event activity
```ps
python ./gh-user-activity.py <github-username> 
```