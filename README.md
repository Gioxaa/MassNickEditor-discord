# MassNickEditor-discord

MassNickEditor is a Discord bot script that allows server administrators to modify the nicknames of all members in a server simultaneously. It supports two primary features:
- **Change Nicknames**: Change all member nicknames in the server to a specified name.
- **Restore Original Nicknames**: Restore all members’ original nicknames to their default.

## Features
- Quickly change all member nicknames to a specified name using the `.call` command.
- Revert all members' nicknames to their original state using the `.backnick` command.
- Efficiently handles permissions and skips the server owner and bots.

## Commands
- `.call <nickname>`: Changes all members' nicknames in the server to the specified `<nickname>`.
- `.backnick`: Restores all members' original nicknames.

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd MassNickEditor
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Replace the placeholder token in the script with your Discord bot token.

5. Run the bot:
    ```bash
    python bot.py
    ```

## Usage

- **Change Nicknames**: Use the `.call <nickname>` command to set a new nickname for all members.
  - Example: `.call EventName`
  
- **Restore Original Nicknames**: Use the `.backnick` command to restore all members' original nicknames.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions and suggestions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For any questions or support, please reach out to the repository owner or open an issue on GitHub.

Happy coding!
