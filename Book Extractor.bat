@echo off
REM to start the terminal maximized uncomment next line
REM if not "%1" == "max" start /MAX cmd /c %0 max & exit/b
Title Extractor
color 0c

start  /MIN cmd.exe  /c  "emulator @kindle_API_28"

echo loading ... .
timeout 5 >null

python main.py

echo Extraction Complete !
timeout 2 >null

START https://drive.google.com/drive/folders/1CXZOVDYMaNVNnNeJDxAL7SZ9H2tz8auY
explorer  .\books
