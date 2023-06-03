import re
import sys
import os

def getlink(s):
    pattern = r"^(https?://)?(www\.)?[a-zA-Z0-9]{1,256}\.[a-zA-Z0-9]{1,256}/?"
    m = re.match(pattern, s)
    return m.group(0) if m != None else None


def transform_link(og, id):
    base = getlink(og)

    if not base: return "Link format not recognized"
    if base == og:
        return f"{'https://www.' if not 'http' in base else ''}{base}/view/{id}"
    if base[-1] == "/": base = base[:-1]
    PATTERN_ITEM = r",.*\.htm"
    PATTERN_PROMO = r"/kategorie/promocja-.+"
    PATTERN_CATEGORY = r"/kategorie/.+"
    m = re.search(PATTERN_ITEM, og)
    if m:
        return f"{'https://www.' if not 'http' in base else ''}{base}/view/{id}/{m.group(0)[1:-4]}"
    m = m = re.search(PATTERN_PROMO, og)
    if m:
        return f"{'https://www.' if not 'http' in base else ''}{base}/page/{id}/{m.group(0)[1:]}"
    m = m = re.search(PATTERN_CATEGORY, og)
    if m:
        return f"{'https://www.' if not 'http' in base else ''}{base}/page/{id}/{m.group(0)[1:]}"

    return f"{'https://www.' if not 'http' in base else ''}{base}/view/{id}"


id = input("id: ")

if len(sys.argv) == 2:
    try:
        inpt = open(sys.argv[1], "r")
        with open(f"{os.getcwd()}/{sys.argv[1][:-4]}modified.txt", "w+") as output:

            for line in inpt.readlines():
                output.write(transform_link(line.strip(), id))
                output.write("\n")
        inpt.close()
        exit(0)
    except FileNotFoundError:
        print("wrong file")

links = []
while True:
    try:
        link = input("link: ")
        lt = transform_link(link, id)
        print(lt)
        links.append(lt)
    except KeyboardInterrupt:
        if input("\nsave to file? [y/n]: ").lower() == "y":
            with open("books.txt", "w+") as f:
                for l in links:
                    f.write(l)
                    f.write("\n")
                f.close()
        exit(0)