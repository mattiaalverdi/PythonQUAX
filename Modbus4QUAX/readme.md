# QUAX Modbus Communication

In this project, we establish communication with the QUAX's PLC in the automation rack.

The work is divided into several components:
- `main.py`
- `functions.py`
- `thresholds_class.py`
- `QUAX_thresholds.py`
- `mail_sender.py`
- `QUAX_bot.py`
- `bot.json`

---

## Components

### main.py
This file contains the main logic for various types of communication with the PLC. It imports the other components as follows:
- **Functions**: Defines the Modbus client for the PLC Modbus server and the decode functions for holding registers where data is stored by the PLC server.
- **thresholds_class**: Defines the class for alarm and warning configuration, including the comparison function.
- **QUAX_thresholds**: Contains the main configuration for the QUAX alarms and warnings.

### functions.py
Contains utility functions for the project, including Modbus client setup and register decoding.

### thresholds_class.py
Defines the `Thresholds` class for managing alarm and warning thresholds, including methods for setting and getting these thresholds.

### QUAX_thresholds.py
Includes the configuration for the QUAX alarms and warnings, setting specific thresholds for different parameters.

### mail_sender.py
Application for sending emails. This can be used to notify about alarms or other significant events.

### QUAX_bot.py
Telegram bot for interacting with the QUAX system.

### bot.json
Configuration file for the Telegram bot. It includes:
- `bot_token`: The Telegram Bot access token, generated with @BotFather on a Telegram client.
- `bot_name`: The desired bot name to be shown.
- `antibounce`: The delay in seconds before sending alarm notifications. The notification is sent only if the alarm persists for more than the specified antibounce seconds.
- `users`: A list of known Telegram user IDs who can interact with the bot. Unauthorized users will receive a message stating their ID, which they need to send to the bot admin to be included in this list. This field can also include IDs of Telegram groups.
- `subscriptions`: Specifies who will receive notifications for each group of PV alarms. For example, users `user1` and `group1` will receive notifications for alarms from PVs belonging to the `example_subsystem` group. The users and their IDs must be specified in the `users` field. Multiple groups can be specified.

---

## Installation

