# Naver Price Tracker

## Structure

```
 ┣ logs
 ┃ ┣ ERROR.log
 ┃ ┣ keywords.txt
 ┃ ┣ result.txt
 ┃ ┗ targets.txt
 ┣ ui
 ┃ ┣ myDialog.ui
 ┃ ┗ ui_mainWindow.ui
 ┣ logger.py
 ┣ main.py
 ┣ middleware.py
 ┣ myDialog.py
 ┣ scraper.py
 ┣ ui_mainwindow.py
 ┣ userAgents.py
 ┗ worker.py
```

## Workflow

1. Overall
   input : targets, keywords, pages, interval
   output : links

```sequence
user->main: inputs
main -> worker: run
worker -> scraper: inputs
worker -> main: rest
main -> user: rest for interval
worker -> main: finished
main -> user: exit
```

## Dependencies

bs4==0.0.1
PySide2==5.15.2
requests==2.25.1
