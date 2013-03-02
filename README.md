SkyPush - Push from Skyrim
==========================

Sends your character's current location in Skyrim to your mobile application.

This is a quick hack-day exploration of integrating movement through a video
game world with external alerts systems. I wanted to use a player attribute
other than achievements or presence at the computer. My purpose was open the
possibilities that an event messaging system could open. I would love to see the
Steam and XBox Live platforms create an api for there developers that could send
rich notification events based on the activities a user is taking within a game.

Uses [Urban Airship](http://urbanairship.com) as the push platform provider.

Setup:

You will need a mobile applicaton that embeds the Urban Airship libraries,
[Python](http://www.python.org/), and the [Skyrim Creation Kit](http://www.creationkit.com/).

Edit C:\Users\$USER\Documents\My Games\Skyrim\Skyrim.ini to have the following
settings:

    [Papyrus]
    bEnableLogging=1
    bEnableTrace=1
    bLoadDebugInformation=1

I will not get deep into how to use the Creation Kit, but you will need to
drop the two SkyrimPush papyrus scripts into the Skyrim/Data/Scripts/Source
folder and compile them. Create a new mod and attach SkyrimPushQuestScript to a
new quest set to "Always Enabled" and "Run Once". Attach the
SkyrimPushPlayerScript to the player (or if you can figure out how to use a
Player ReferenceAlias and get the events to fire, please submit a patch!)

Edit the values in the python script to be appropriate for your app setup. You
will need your Urban Airship app_key and master secret, at least. Run the python
script using simply "python skypush.py". It will monitor the SkyPush.0.log file
for new updates from a Skyrim running with your mod created above.

This implementation is pretty much a terrible hack, I take no responsibility
for its use.

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">Creative Commons Attribution 3.0 Unported License</a>.