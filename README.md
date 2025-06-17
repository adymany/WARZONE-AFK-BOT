# Warzone AFK Bot

A Python-based controller simulator designed to keep you AFK (Away From Keyboard) in Call of Duty: Warzone by simulating controller inputs using the `vgamepad` library.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Features
- Simulates controller inputs to prevent being kicked for inactivity in Warzone.
- Easy to set up with minimal dependencies.
- Lightweight and customizable for different AFK scenarios.

## Prerequisites
- Python 3.8 or higher
- `vgamepad` library
- Windows operating system (required for `vgamepad`)

## Installation
1. **Install Python**:  
   Download and install Python 3.8+ from [python.org](https://www.python.org/downloads/). Ensure you add Python to your system PATH during installation.

2. **Install vgamepad**:  
   Open a terminal or command prompt and run:
   ```
   pip install vgamepad
   ```

3. **Clone the Repository**:  
   Clone this project to your local machine:
   ```
   git clone https://github.com/your-username/warzone-afk-bot.git
   cd warzone-afk-bot
   ```

## Usage
1. Ensure Warzone is running and your controller is recognized by the game.
2. Run the AFK bot script:
   ```
   python warzone_afk_bot.py
   ```
3. The script will simulate periodic controller inputs to keep you active in the game.
4. To stop the bot, press `Ctrl+C` in the terminal.

**Note**: Customize the script (e.g., input frequency or type) by editing `warzone_afk_bot.py` to suit your needs.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows the project's coding standards and includes relevant documentation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer
This tool is for educational purposes only. Use it responsibly and in compliance with Call of Duty: Warzone's terms of service. The developer is not responsible for any account bans or issues arising from the use of this tool.
