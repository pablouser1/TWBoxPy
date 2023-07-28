import os
import argparse
from glob import glob
import requests

BASE_URL = "https://art.gametdb.com/ds/coverS/{language}/{ndsId}.png"

def printVerbose(msg: str, enabled: bool):
    if enabled:
        print("[VERBOSE] {0}".format(msg))

def getFiles(inPath: str)-> list:
    path = os.path.join(inPath, "*.nds")
    return glob(path)

def getRomInfo(path: str)-> tuple:
    # https://problemkaputt.de/gbatek-ds-cartridge-header.htm
    with open(path, "rb") as f:
        ndsTitle = f.read(12)
        ndsIdCode = f.read(4)
    return ndsTitle.decode("utf8"), ndsIdCode.decode("utf8")

def downloadArt(ndsId: str, langs: list, output: str, verbose: bool)-> tuple:
    success = False
    code = -1

    i = 0
    while i < len(langs) and not success:
        lang = langs[i]
        printVerbose("Trying to download {0}, {1}".format(ndsId, lang), verbose)
        url = BASE_URL.format(language=lang, ndsId=ndsId)
        filename = os.path.basename(url)
        r = requests.get(url, stream=True)
        if r.ok:
            with open(os.path.join(output, filename), 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        success = r.ok
        code = r.status_code
        i += 1
    
    return success, code

def main():
    parser = argparse.ArgumentParser(
        prog='TwBox',
        description='Download art boxes from GameTDB')
    
    parser.add_argument('input')
    parser.add_argument('-o', '--output', default="./out", help="Output folder where the images will be downloaded, defaults to ./out")
    parser.add_argument('-l', '--languages', nargs="+", default=['EN'], help="Languages to download the covers from top to bottom priority. Defaults to EN. Available: EN, ES, FR, IT...")
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help="Make program verbose")

    args = parser.parse_args()

    # Get all nds files available
    files = getFiles(args.input)

    if len(files) == 0:
        print("No NDS files detected!")
        return

    # Creating output folder first
    os.makedirs(args.output, exist_ok=True)

    for f in files:
        ndsName, ndsId = getRomInfo(f)
        if not os.path.exists(os.path.join(args.output, "{0}.png".format(ndsId))):
            print("Getting {0}: {1}".format(ndsName, ndsId))
            success, code = downloadArt(ndsId, args.languages, args.output, args.verbose)

            if not success:
                print("Could not download cover art for {0}! HTTP Code {1}".format(ndsName, code))
        else:
            print("{0} already exists! Skip".format(ndsId))

if __name__ == '__main__':
    main()
