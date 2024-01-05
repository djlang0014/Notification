# Notification
Repository for Notification, a python script that sends Windows notifications and plays an alert.

# How-To

1. It is assumed you have already cloned the Clue-Less GitHub repo and have a terminal open in the top folder of the repo folder structure.  It is also highly recommended to run `git pull` before editing the project.
  
2. It is recommended to set up a virtual enviornment. This can be done by running:
```
python -m venv ./<venv name>
```
where <venv name> should be replaced by the name of your virtual environment.  I recommend naming it either `env` or `venv`.  If you name it anything else, please add the name to the end of the `.gitignore` file.
After your virtual environment has been created, you can activate it by running
```
. <venv name>/Scripts/activate
```

3. Ensure you have the required dependencies. In order to install the required dependencies, run
```
pip install -r requirements.txt
```
If it is necessary to download new dependencies during development, you can update the dependencies file by running
```
pip freeze > requirements.txt
```
Please only run the above command if you are in a virtual environment created exclusively for this project.  Otherwise, add the dependency manually to the `requirements.txt` file.

4. The notifications that are sent are listed in MyNotifications.txt. These can be freely changed as desired. It will take each line of text as a separate notification message.

6. This script is ran through the terminal with command line arguments. Specifically, it takes an input file path, period (amount of time between each notification), a file path for the alert sound (this needs to be a .wav file), and repeat argument where 1 will repeat the notifications after each one is used. For example:
   ```
    python notification.py ./MyNotifications.txt 1 ./alert.wav 0
   ```
   This command will run the script with MyNotifications as the input file, a 1 minute period between each notification, alert.wav as the alert sound, and it will not repeat.
   
