QUAX MODBUS COMUNICATION

In this project we can dialog with the QUAX's PLC in the automation Rack 

We can divide the work in more than one function, in particular we have:
- main
- Functions
- thresholds_class
- QUAX_thresholds
- mailSender
- QUAX_bot
- bot.json

---------------------------------------------------------------------------------------------------
main
in this file we can find the main logic behind the various type of comunication with the PLC
Here we import all the other files as:
- Functions: where we define the modbus client of the PLC modbus server and the decode functions of a holding register where datas are stored by PLC server
- Thresholdd_class: where we define the class for alarm and warning configuration, also we define the comparison function
- QUAX_thresholds: in this file there is the main configuration for the QUAX alarms and warnings


---------------------------------------------------------------------------------------------------
- mailSender: application that send an email

---------------------------------------------------------------------------------------------------
BOT TELEGRAM
- QUAX_bot


- bot.json
where:

-bot_token: is the Telegram Bot access token, to be generated with @BotFather on a Telegram client.
-bot_name: is the desired bot name to be shown on the help.
-antibounce: is the delay in seconds to wait before sending alarms notifications. The notification is sent only if the alarm persists for more than antibounce seconds.
-users: is a list of know Telegram user IDs, who can talk to this Bot. All other users will get an unathorized message, stating their ID. They should send this ID to the bot admin to be included in this list. This field can also include IDs of Telegram groups.
-subscriptions: is used to specify who will receive notifications for each group of PV alarms. Let's create a new group of PVs called example_subsystem: the users user1 and group1 will receive notification of alarms from the PVs belongin to this group. The users and their IDs must be specified in the users tag. Multiple groups can be specified.