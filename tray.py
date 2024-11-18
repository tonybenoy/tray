import sys
import subprocess

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: tray.py [options] [package]")
        sys.exit(1)

    # Mapping of pacman commands to winget commands
    pacman_to_winget = {
        '-Syu': ['upgrade', '--all'],
        '-Syyu': ['upgrade', '--all'],
        '-Sy': ['source', 'update'],
        '-S': ['install'],
        '-Ss': ['search'],
        '-R': ['uninstall'],
        '-Rns': ['uninstall'],
        '-Q': ['list'],
        '-Qi': ['show'],
        '-Si': ['show'],
        '-Qs': ['list'],
    }

    cmd = args[0]

    if cmd in pacman_to_winget:
        winget_cmd = ['winget'] + pacman_to_winget[cmd]

        # Commands that require additional arguments
        requires_arg = ['-S', '-Ss', '-R', '-Qi', '-Si', '-Qs','-Syyu','-Rns']
        if cmd in requires_arg:
            if len(args) > 1:
                winget_cmd += args[1:]
            else:
                print(f"Error: The command '{cmd}' requires a package name or search term.")
                sys.exit(1)
        print(f"Running: {' '.join(winget_cmd)}")
        subprocess.run(winget_cmd)
    else:
        # Default to winget command
        winget_cmd = ['winget'] + args
        print(f"Running: {' '.join(winget_cmd)}")
        subprocess.run(winget_cmd)

if __name__ == '__main__':
    main()
