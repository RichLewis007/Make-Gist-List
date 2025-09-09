#!/usr/bin/env bash

# Example script for MacOS to manually run the gist list updater from the terminal command line.

# CONFIGURE: Edit this file on your local computer and fill in your own values.
# Make sure to replace the "your-username-here" and "your-gist-id-here" and "your-github-token-here" values.

# REQUIREMENTS: You'll need to have the latest version of Python installed on your local computer.
# You can check the version of Python you have installed by typing: "python --version" in the terminal.
# If you need to install Python on MacOS with brew, you can use the following command: "brew install python" in the terminal.
# If you need to install Python on Windows, you can use the following command: "winget install python" in the terminal.
# If you need to install Python on Linux, you can use the following command: "sudo apt-get install python3" in the terminal.

# (Yikes, the instructions for running this script are now much longer than the lines of code themselves!)

# TO RUN: On MacOS, you can run this script by first making it  executable by typing: "chmod +x update-my-gist-list.sh" in the terminal.
# Then you can run the script by typing: "./update-my-gist-list.sh" in the terminal.

# IMPORTANT:This 'bash'script may work on macOS, but it may not work on your Linux distro, Windows, or other operating systems.
# If you need to run this script on a different operating system, you will need to use a different scripting language.
# For example, if you need to run a similar script on Windows, you will need to use PowerShell.

export GITHUB_USERNAME="your-username-here"  # Required for local runs
export LIST_GIST_ID="your-gist-id-here"      # Optional - for updating a gist
export GIST_TOKEN="your-github-token-here"   # Optional - for updating a gist

# Run the script
python make-gist-list.py
