#!/bin/bash
exe="weekplan"
pth="dist/weekplan"
[[ -f "$exe" ]] && rm -- "$exe"
pyinstaller --onefile weekplan.py
[[ -f "$pth" ]] && cp -- "$pth" "$PWD/"
