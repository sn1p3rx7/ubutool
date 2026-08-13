#!/usr/bin/env python3

import getpass
import os
import platform
import shutil
import subprocess


VERSION = "0.1.0"
USERNAME = getpass.getuser()


def info():
    print("\n=== System Information ===")
    print(f"OS:       {platform.system()}")
    print(f"Release:  {platform.release()}")
    print(f"Machine:  {platform.machine()}")
    print(f"Python:   {platform.python_version()}")
    print()


def disk():
    total, used, free = shutil.disk_usage("/")

    print("\n=== Disk Usage ===")
    print(f"Total: {total // (1024**3)} GB")
    print(f"Used:  {used // (1024**3)} GB")
    print(f"Free:  {free // (1024**3)} GB")
    print()


def ram():
    try:
        result = subprocess.run(
            ["free", "-h"],
            capture_output=True,
            text=True
        )

        print("\n=== RAM Usage ===")
        print(result.stdout)

    except FileNotFoundError:
        print("The 'free' command was not found.")


def uptime():
    try:
        with open("/proc/uptime", "r") as file:
            seconds = float(file.read().split()[0])

        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)

        print(f"\nUptime: {hours}h {minutes}m\n")

    except FileNotFoundError:
        print("Could not read system uptime.")


def update():
    print("\nChecking for available updates...\n")
    subprocess.run(["apt", "list", "--upgradable"])


def help_message():
    print("""
Ubutool v0.1.0

Available commands:

  help       Show this help message
  info       Show system information
  disk       Show disk usage
  ram        Show RAM usage
  uptime     Show system uptime
  update     Check for available updates
  clear      Clear the terminal
  version    Show Ubutool version
  exit       Exit Ubutool

You can run multiple commands using &&:

  info && disk
  ram && uptime
  info && disk && ram
""")


def execute(command):
    command = command.strip().lower()

    if command == "help":
        help_message()

    elif command == "info":
        info()

    elif command == "disk":
        disk()

    elif command == "ram":
        ram()

    elif command == "uptime":
        uptime()

    elif command == "update":
        update()

    elif command == "clear":
        os.system("clear")

    elif command == "version":
        print(f"Ubutool v{VERSION}")

    elif command in ("exit", "quit"):
        return False

    elif command == "":
        return True

    else:
        print(f"Unknown command: {command}")
        print('Type "help" to see available commands.')

    return True


def main():
    print(f"Ubutool v{VERSION}")
    print('Type "help" to see available commands.\n')

    while True:
        try:
            command_line = input(
                f"ubutool@{USERNAME}> "
            ).strip()

            if not command_line:
                continue

            commands = command_line.split("&&")

            for command in commands:
                if not execute(command):
                    print("Goodbye!")
                    return

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
