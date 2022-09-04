# Simple Encrypt

## Description
This is a tool for encrypting text, especially used for sending sensitive information on the Internet.

## Build Instructions
To build Simple Encrypt, the latest version of Python 3 and cryptocode, pyperclip module are required.

```
$ sudo apt install python3 python3-pip
$ python3 -m pip install --upgrade pip
$ pip3 install cryptocode pyperclip
```

After ensuring the requirements are met, simply build from "simple_encrypt.py" file using pyinstaller.

```
$ pyinstaller -F simple_encrypt.py
```

## Licensing Information
Copyright (C) 2022  Carter Zhang

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
