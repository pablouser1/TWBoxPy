# TWBoxPy
Simple box art downloader from GameTDB deisgned for TwilightMenu++

## Features
* Cross-platform (Windows, Mac and Linux)
* Multi-region
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
# try to download covers for the United Kingdom, then Spain and then Japan
# and save all covers in ./out
python3 twbox.py IN_DIR --regions EN ES JA --output ./out
```

### Regions
| Name | Code |
| :--: | :--: |
| United States | US |
| Japan | JA |
| United Kingdom | EN |
| France | FR |
| Germany | DE |
| Spain | ES |
| Italy | IT |
| Netherlands | NL |
| Portugal | PT |
| Australia | AU |
| Sweden | SE |
| Denmark | DK |
| Norway | NO |
| Finland | FI |
| Korea | KO |
| Russia | RU |

You can get more info about how to use the CLI tool with:
```bash
python3 twbox.py -h
```

The output argument should be the `boxart` folder inside your `_nds` folder, more info [here](https://wiki.ds-homebrew.com/twilightmenu/how-to-get-box-art)

## Credits
NDS Header info taken from: https://problemkaputt.de/gbatek-ds-cartridge-header.htm
