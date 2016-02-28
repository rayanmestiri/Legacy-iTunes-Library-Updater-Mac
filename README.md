Legacy-iTunes-Library-Updater-Mac
==========================
<h2>DISCLAIMER</h2>
<h2>This app doesn't work for iTunes 12.2 and later.<br/>
iTunes dropped the support of the XML file for its library in favor of a binary ITL file.<br/>
</h2>

https://support.apple.com/en-us/HT201610

<strong>I would not need the XML file to make this app work if the Apple Script code responsible for watching removed items in watched folders wasn't broken. It works just fine with pure Apple Script when watching for added items in a watched folder but when watching for removed/moved items, it doesn't:<br/><br/></strong>
`on removing folder items from alias after losing listOfAliasOrText`<br/><br/>
<strong>The variable </strong>`listOfAliasOrText`<strong> is always empty. If this worked, I wouldn't need a Python script to read the library and I could update the library with Apple Script native iTunes linking.<br/><br/>
If you know how to make it work or have a workaround, don't hesitate to contact me or send a pull request.</strong> 

<p align="center"><img src="http://4.ii.gl/j1EKzqEho.png"/><p>

Choose a folder and iTunes will automatically watch it and all its subfolders. 
<br/>You don't have to drag n drop files into iTunes anymore.

<h2>Instructions</h2>
- Launch the app
- Click on "Choose Folder"
- The folder you choose will be the one iTunes will watch to update automatically
- Wait for the process to complete (I didn't add a loading animation or something). <br/>It can be long if you have a lot of sub-folders.
- Once the process is completed, you're good to go.
- If you want to change the folder or remove the auto updating, launch the app again.

<h2>How it works</h2>
An AppleScript adds <a href="https://developer.apple.com/library/mac/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_folder_actions.html">folder actions</a> recursively.
<br/>When files are added, the folder action tells iTunes to add the list of files to its library.
<br/>When files are removed or moved, unfortunately, we can't get the list of files, see disclaimer above.
<br/>So the workaround is to call a python script that parses the iTunes library XML and checks if the paths matches to an existing file on the system.
<br/>It creates an array of missing music names and passes it to an AppleScript as an argument.
<br/>The AppleScript tells iTunes to remove each of these files from its library.

<h2>Known issue</h2>
The script doesn't remove Folder Actions from the folders you remove from your main iTunes directory.
The issue is related to the fact that I cannot retrieve the list of folders/files removed with folder actions. I don't have a solution yet.
