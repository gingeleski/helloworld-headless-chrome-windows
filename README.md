## Headless Chrome experiments on Windows

Powershell and Python experiments with headless Chrome.

I thought this might be enlightening for others trying to get started. :rainbow:

This was practice for refactoring [xssmap](https://github.com/gingeleski/xssmap) to leverage headless Chrome.

## Powershell smoke test

```
cd 'C:\Program Files (x86)\Google\Chrome\Application

# Dump DOM to the screen
.\chrome.exe --headless --disable-gpu --enable-logging --dump-dom https://www.google.com/

# Save the page as a PDF
.\chrome.exe --headless --disable-gpu --print-to-pdf=C:\Temp\output.pdf https://www.google.com/

# Screenshot the page
.\chrome.exe --headless --disable-gpu --screenshot=C:\Temp\screenshot.png https://www.google.com/
```

Credit to [this StackOverflow answer](https://stackoverflow.com/questions/45364102/how-do-i-use-headless-chrome-in-chrome-60-on-windows-10). :100:

## Run Python

First [download chromedriver.exe](https://sites.google.com/a/chromium.org/chromedriver/downloads) (>= v2.32) into the repo directory.

Then you can do the following from your prompt... and I recommend doing so [from a venv](https://docs.python.org/3/library/venv.html).

```
pip install -r requirements.txt
python chrome_test.py
```
