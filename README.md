# TWBoxPy
Simple box art downloader from GameTDB deisgned for TwilightMenu++

## Features
* Cross-platform (Windows, Mac and Linux)
* Multi-language
* Ready to use for TwilightMenu++

## Requirements
* Python3
* python-requests

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
# In this example, the program will scan nds files from IN_DIR,
# try to download covers in english, spanish and then japanese
# and save all covers in ./out
python3 twbox.py IN_DIR --languages EN ES JA --output ./out
```

You can get more info about how to use the CLI tool with:
```bash
python3 twbox.py -h
```

The output argument should be the `boxart` folder inside your `_nds` folder, more info [here](https://wiki.ds-homebrew.com/twilightmenu/how-to-get-box-art)

## Credits
NDS Header info taken from: https://problemkaputt.de/gbatek-ds-cartridge-header.htm
