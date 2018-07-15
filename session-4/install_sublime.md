# Installing a Text Editor for Programming


In this guide, we describe how to install a quite popular text editor for programming called _Sublime Text 3_.

Interestingly, _Sublime Text 3_ is written in Python itself.


  * Navigate in your browser to https://www.sublimetext.com/3
  * Download the file corresponding to your operating system to your computer
    - For Windows (64bit) https://download.sublimetext.com/Sublime%20Text%20Build%203176%20x64%20Setup.exe
    - For Mac OS X https://download.sublimetext.com/Sublime%20Text%20Build%203176.dmg
    - For Linux follow the instructions on https://www.sublimetext.com/docs/3/linux_repositories.html
  * For Windows and Mac OS X, double click the downloaded program/archive and install it by following the on-screen instructions.


## Making Sublime Text Callable from the Command-line


### Windows


### Mac OS X

Create a link to the `subl` program as in the following:

  * Open the terminal, for example by pressing `cmd+space` and type `terminal` followed by a `Return`
  * In the terminal enter the following:
    ```bash
    sudo ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
    ```



### Linux




  https://scotch.io/tutorials/open-sublime-text-from-the-command-line-using-subl-exe-windows