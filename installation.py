# installation.py sets up the paths and enters your authorization token for uploading to dropbox.
# Run the installation from the project folder

import os
cwd = os.getcwd()  # Current Working Directory

print "Make sure your authentication token and nothing else is in the text file  authorization_token.txt. If it is not, cancel now by pressing ctrl + d."

print "Please enter the full path to the music folder, without a '/'  at the end."
music_folder = raw_input('> ')

with open("authorization_token.txt", 'r') as token_file:
    authorization_token = token_file.read()

print "Setting the music folder to", music_folder
print "Setting the authorization token to", authorization_token
print "Setting the path to the project folder as", cwd

filename = "dropboxscript"
with open(filename, 'r') as myfile:
    text = myfile.read()

new_text = text.replace("PATH_TO_REPOSITORY", cwd)
new_text = new_text.replace("MUSIC_FOLDER", music_folder)
new_text = new_text.replace("AUTHORIZATION_TOKEN", "FfH7p3Pu-IEAAAAAAABJ-V8wec9YjZO1oIWdd7M0CZWQ4hbK18ALlvGaowcZOK99")

with open(filename, 'w') as myfile:
    myfile.write(new_text)

# Use backups of song lists if they exists
for filename in ["songList_backup.txt", "songList2_backup.txt"]:
    if os.path.isfile(filename):
        new_filename = filename.replace("_backup", "")
        os.rename(filename, new_filename)
