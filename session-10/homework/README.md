# Assignment for Session 10

## A bit of software integration

Programming today often means to integrate programs or systems with each other.

The purpose of this assignment is to get a feeling for that.


Inspect the code in the directory `eliza_server`. You can run the webserver with 

```bash
$ python server.py
```

You can stop the running webserver by pressing `CTRL+C`.

After running the webserver and playing a bit with it in your browser (navigate to `http://127.0.0.1:5000`) inspect the Python program in `server.py`. In particular try to understand where the messages are created that are displayed in the browser and where answers from the user are handled.

Now, take the complete Eliza program from session one (both modules `eliza.py` and `eliza_language.py`) and modify it so that you can talk to Eliza via your browser. That is, integrate `eliza.py` and `server.py`. Consequently, you do not want to have any calls to the `input` function in your code and you want to start your web-based Eliza by starting the `server.py`.

