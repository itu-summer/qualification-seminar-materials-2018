# Installing Visual Studio Code

  * Navigate to https://code.visualstudio.com
  * Hit the download button

  * Install the program accordingly.
    - On MacOS: drag the downloaded file to your `Application` folder
    - On Windows:

Run Visual Studio Code by double clicking it's icon


https://code.visualstudio.com/docs/setup/mac


Make it executable from the command-line by following:
  * MacOS Xhttps://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line
  * Under Windows it is added to the PATH by default during installation but it requires a restart

Install the Python tools https://marketplace.visualstudio.com/items?itemName=ms-python.python



For enabling the debugger, this has to be done only once and the first time the tool is installed:

  * From the command-line execute `code debug_me.py`
  * Hit the debug icon (left side 4th from the top)
  * Hit the green play button next to `Debug` on the top left
  * Create a new configuration as suggested


**TODO**: Figure out how to pass CLI arguments to the debugger. When I do as under https://i.stack.imgur.com/Hx5tf.png and https://stackoverflow.com/a/49480670 I get an error. But it starts working when I remove the leading comments, which do not seem to be correct JSON  

