# Hydrator

## Purpose

This tool written in Python 3 transforms HAR (HTTP Archive) content from modern browsers and transforms it into custom, ready to use **http(s)-form-post** THC-Hydra commands.

## Requirements

Windows - So far my program's clipboard interface only with the Windows operating system. UNIX support will soon be integrated.

Python 3?+ - May work with Python 2+ (haven't tested with anything less than Python 3.6)

Google Chrome / Firefox / Internet Explorer 9 - These are the only mainstream browsers that support network request exports as HAR content.

## Procedure

To utilize this tool, first clone this repository to your machine (or download as .zip and extract):

`git clone https://github.com/tjgerot/hydrator`

Navigate your browser to the HTTP/HTTPS form you want to brute force. Open the debugger console and switch to the **network** tab (it should be recording). Login with the credentials `ABC` for the username and `XYZ` for the password; submit the form. Once you see a message indicating an invalid authentication, stop the recording and right click on a request (I only tested this in Google Chrome). Select the option that lets you copy your network interactions in the HAR content.

Navigate into the project's directory in your terminal (with Python installed and on %PATH%) and run `python hydrator.py`

Answer the following prompts given by the program:
  `Invalid Flag` - If Hydra see's this string, it knows the combination was wrong (otherwise they were right)
  `Username` - The username to guess passwords for
  `Wordlist` - The path to the wordlist (Kali Linux - `/usr/share/wordlists/rockyou.txt`)
  `Timeout` - The time (s) Hydra should wait on a slow thread before giving it up
  `Threads` - Number of separate processes (threads) to assign to the attack

## Limitations

These items are current limitations of this tool, but should be fixed in the future:

  1. Windows only support
  2. Python clipboard dependencies
  3. Form only brute forces
  4. No success flags
  5. No option for username lists
  6. Only 1 password configuration
  7. Python 3 only support (maybe?)
  8. Includes all headers + parameters when many are often worthless
