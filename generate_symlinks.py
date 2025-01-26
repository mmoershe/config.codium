from sys import exit
import os
import shutil

import dotenv
dotenv.load_dotenv()


DEFAULT_CONFIG_DIRECTORY: str = "~/.config/VSCodium/User/"
CONFIG_DIRECTORY: str = os.getenv("VSCODIUM_CONFIG_DIRECTORY", default=DEFAULT_CONFIG_DIRECTORY)
CONFIG_DIRECTORY: str = DEFAULT_CONFIG_DIRECTORY if CONFIG_DIRECTORY == "" else CONFIG_DIRECTORY
CONFIG_DIRECTORY: str = os.path.expanduser(CONFIG_DIRECTORY)
if not os.path.exists(CONFIG_DIRECTORY): 
    print(f"Given VSCodium config-directory ('{CONFIG_DIRECTORY}') does not seem to exist. Either the directory is wrong, or you need to start VSCodium once for it to create the required directories.")
    exit()


files_to_link: list[str] = ["settings.json", "keybindings.json"]
directories_to_link: list[str] = ["snippets"]


print("\n---- SYMLINKS ----\n")
for file in files_to_link: 
    assert os.path.exists(file), "file doesn't exist in repository."
    source: str = os.path.abspath(file)
    target: str = os.path.join(CONFIG_DIRECTORY, file)
    os.remove(target) if os.path.exists(target) else None
    os.symlink(source, target)
    print(f'Symlink created: "{source}" -> "{target}"')

print()
for directory in directories_to_link: 
    assert os.path.exists(directory), "directory doesn't exist in repository."
    source: str = os.path.abspath(directory)
    target: str = os.path.join(CONFIG_DIRECTORY, directory)
    os.unlink(target) if os.path.islink(target) else None
    shutil.rmtree(target) if os.path.isdir(target) else None
    os.symlink(source, target, target_is_directory=True)
    print(f'Symlink created: "{source}" -> "{target}"')
print("\n---------------\n")

print("To install the extensions, run the 'install_extensions.sh' script.")
