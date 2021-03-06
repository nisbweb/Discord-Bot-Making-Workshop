# Discord Bots making Event

### Needed:
- [Python 3.x](https://www.python.org/downloads/)
- [A verified discord account](https://discord.com/register)

### How to run :
- Clone the repository
  ```
	$ git clone https://github.com/nisbweb/Discord-Bot-Making-Workshop.git
  ```
- Install [Discord.py](https://pypi.org/project/discord.py/) python module for discord bots.
  ```bash
	$ pip install discord.py
  ```
  or for Linux 
  ```
	$ pip3 install discord.py
  ```
  Mac
  ```
	$ python3 -m pip install discord.py
  ```
- Get your bots token from [ the discord developers page](https://discord.com/developers/applications), By selecting your application , going into the bots navigation menu and copying the secret token generated.
- Add the token in the files at the places mentioned.
- Add the bot to the server, by generating a link in the OAuth tab of the bot page.
- Run the python file
  ```
	$ python <file name>.py
  ```

### Further additions:
- Host the bot so that it will constantly run, Heroku, Okteto, Civo , AWS etc are all viable options
- Make multipurpose bots with a varied range of commands.
- Add logging and error handling in the bot.

### NOTE:
- If you get a invalid certificate issue, 
  - open Internte explorer in administrator mode
  - go to www.discord.com
  - click on the padlock next to the url
  - View certificate and install certificate
