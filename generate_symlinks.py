import os
import dotenv


dotenv.load_dotenv()

DEFAULT_CONFIG_DIRECTORY: str = "~/.config/VSCodium/User/"
CONFIG_DIRECTORY: str = os.getenv("VSCODIUM_CONFIG_DIRECTORY", default=DEFAULT_CONFIG_DIRECTORY)
CONFIG_DIRECTORY: str = DEFAULT_CONFIG_DIRECTORY if CONFIG_DIRECTORY == "" else CONFIG_DIRECTORY
CONFIG_DIRECTORY: str = os.path.expanduser(CONFIG_DIRECTORY)


files_to_link: list[str] = ["settings.json", "keybindings.json"]
directories_to_link: list[str] = ["snippets"]

for file in files_to_link: 
    assert os.path.exists(file), "file doesn't exist in repository."
    source: str = os.path.abspath(file)
    target: str = os.path.join(CONFIG_DIRECTORY, file)
    print(f'ln -sf "{source}" "{target}"')
