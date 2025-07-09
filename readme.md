# AutoSpotDL
*Note: i don't want to promote music piracy, this is for educational purposes only*

This is a small python script to automate the use of SpotDL, a tool to download spotify albums and playlist

## **SETUP**
**PACKAGES**:
create a python venv with `python -m venv venv`, activate it, and use 

    pip install -r requirements.txt
to install the required packages.


**KEYS**: If you are planning on downloading a lot of music, its highly possible that you get an api key bottleneck, because is limited to 600 calls/hour. To avoid this, you can get your own api keys from spotify dev page, and put them in 

    keys.txt

## **ADDING LISTS**

You need to modify `lists.txt` to add the music you want to download. For each album/playlist, you have to add a line to the file, with the link, and the name you want the folder to have. Use this format:

    <link> - <name>
leaving a " - " between the two. for example:

    https://open.spotify.com/intl-es/album/6eUW0wxWtzkFdaEFsTJto6?si=5thLDEzmTT2xhLFaSS9eCg - RickAstley

## **YOU'RE DONE!**

Now you can use `donwloader.py` to download all the playlists, and `folder-sync.py` to copy the music to flashdrives, sd cards, and even to a phone using developer tools for android.

This has been written with help of chatgpt and my knowledge. This isn't meant for people who don't know some computer and python basics, and isn't a final product. Use it if you know how to. Thanks!