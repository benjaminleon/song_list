## song_list

Have you ever had a song locally on your computer and wanted to recommend it, but couldn't produce its name?

This bash script lists all your songs in a specified folder and uploads that list to a dropbox account. To reduce unneccesary data traffic the script only uploads if there has been a change in the music folder since the last upload. Changes in the folder inlcudes renaming, adding or deleting a song or multiple songs.

An interesting find was that even though my dropbox is full (I'm using >30 Gb out of 5 Gb), I was able to upload through their CURL api. However, that seems to be "fixed" by now. It is possible that they have a bug which allows users to upload once via the CURL api even though their storage exceeds the maximum limit.


## Setting things up

To set up the script for your own computer, head over to https://www.dropbox.com/developers/apps to create your own app. Just make a minimal entry to be able to create a key to authorize uploading via their CURL api.

Go to https://dropbox.github.io/dropbox-api-v2-explorer/#files_upload and press "Get Token". Copy that Access Token and put it in the text file "authorization_token.txt".

Type `python installation.py` from the project folder, to let a python script set up the paths and enter your token at the right place in the bash script for you.

## Scheduling a cronjob
A cronjob can execute scripts at regular intervals and is perfect for a script like this which produces backups.

To schedule a cronjob, type `crontab -e` in the terminal. Be careful not to type `crontab -r`, which will remove all crontab settings.

When adding the cronjob, go to the bottom and add `0 20 * * * /path_to_repository/dropboxscript` to run the script every day at 8pm. Press ctrl + o to save, accept with enter and ctrl + x to exit. The terminal should output "crontab: installing new crontab" if everything went OK.

Type in the terminal `chmod +x dropboxscript` to give the shell permission to run the script. This is neccesary for the cronjob to work.

For the cronjob to execute, the computer has to be turned on and the user needs to be logged in. If you want to find out the most likely hour for your user to be logged in to the computer, have a look at my other github repository at http://github.com/benjiyo/computer_usage_statistics.

A good guide to cronjobs is found at http://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/






