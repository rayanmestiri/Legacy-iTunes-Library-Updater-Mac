iTunes-Library-Updater-Mac
==========================

Choose a folder and iTunes will automatically watch it and all its subfolders. 
<br/>You don't have to drag n drop files into iTunes anymore.

<h2>Instructions</h2>
- Launch the app
- Click on "Choose Folder"
- The folder you choose will be the one iTunes will watch to update automatically
- Wait for the process to complete (I didn't yet add a loading animation or something). <br/>It can be long if you have a lot of sub-folders.
- Once the process is completed, you're good to go.
- If you want to change the folder or remove the auto updating, launch the app again.

<h2>How it works</h2>
An AppleScript adds <a href="https://developer.apple.com/library/mac/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_folder_actions.html">folder actions</a> recursively.
<br/>When files are added, the folder action tells iTunes to add the list of files to its library.
<br/>When files are removed or moved, unfortunately, we can't get the list of files. It must be a bug because apple doc says it can but it didn't work for me (i'm using OSX 10.10.1).
<br/>So the workaround is to call a python script that parses the iTunes library XML and checks if the paths matches to an existing file on the system.
<br/>It creates an array of missing music names and passes it to an AppleScript as an argument.
<br/>The AppleScript tells iTunes to remove each of these files from its library.

<h2>Known issue</h2>
The script doesn't update folder actions. So when you copy a folder into your music folder, it won't be watched.
<br/>It should be fixed soon
