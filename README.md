# tray
Pacman life in windows

## Description
`tray` is a Python script that maps common `pacman` commands to their equivalent `winget` commands, allowing you to use familiar `pacman` syntax to manage packages on Windows.

## Usage
To use the script, run it with the desired `pacman` command and options. 

### Example Commands
- Update all packages: `python tray.py -Syu`
- Update package sources: `python tray.py -Sy`
- Install a package: `python tray.py -S <package_name>`
- Search for a package: `python tray.py -Ss <search_term>`
- Uninstall a package: `python tray.py -R <package_name>`
- List installed packages: `python tray.py -Q`
- Show package information: `python tray.py -Qi <package_name>`

### Command Mapping
The following `pacman` commands are mapped to `winget` commands:
- `-Syu` -> `winget upgrade --all`
- `-Syyu` -> `winget upgrade --all`
- `-Sy` -> `winget source update`
- `-S` -> `winget install`
- `-Ss` -> `winget search`
- `-R` -> `winget uninstall`
- `-Rns` -> `winget uninstall`
- `-Q` -> `winget list`
- `-Qi` -> `winget show`
- `-Si` -> `winget show`
- `-Qs` -> `winget list`

## Subcommands
The script supports the following subcommands:

1. `-Syu` or `-Syyu`: Upgrade all packages
    ```bash
    python tray.py -Syu
    python tray.py -Syyu
    ```

2. `-Sy`: Update package sources
    ```bash
    python tray.py -Sy
    ```

3. `-S <package_name>`: Install a package
    ```bash
    python tray.py -S <package_name>
    ```

4. `-Ss <search_term>`: Search for a package
    ```bash
    python tray.py -Ss <search_term>
    ```

5. `-R <package_name>`: Uninstall a package
    ```bash
    python tray.py -R <package_name>
    ```

6. `-Q`: List installed packages
    ```bash
    python tray.py -Q
    ```

7. `-Qi <package_name>`: Show package information
    ```bash
    python tray.py -Qi <package_name>
    ```

## Installation
To install the script, clone the repository and ensure you have Python and `winget` installed on your system.

```bash
git clone https://github.com/tonybenoy/tray.git
cd tray
```

## Running the Script
Run the script using Python and pass the desired `pacman` command as an argument.

```bash
python tray.py [options] [package]
```

## License
This project is licensed under the MIT License.
```

You can edit the [README.md](https://github.com/tonybenoy/tray/edit/main/README.md) file to include this content.
