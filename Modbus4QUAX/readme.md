QUAX MODBUS COMUNICATION

In this project we can dialog with the QUAX's PLC in the automation Rack



where:

-bot_token: is the Telegram Bot access token, to be generated with @BotFather on a Telegram client.
-bot_name: is the desired bot name to be shown on the help.
-antibounce: is the delay in seconds to wait before sending alarms notifications. The notification is sent only if the alarm persists for more than antibounce seconds.
-users: is a list of know Telegram user IDs, who can talk to this Bot. All other users will get an unathorized message, stating their ID. They should send this ID to the bot admin to be included in this list. This field can also include IDs of Telegram groups.
-subscriptions: is used to specify who will receive notifications for each group of PV alarms. Let's create a new group of PVs called example_subsystem: the users user1 and group1 will receive notification of alarms from the PVs belongin to this group. The users and their IDs must be specified in the users tag. Multiple groups can be specified.