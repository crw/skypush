ScriptName SkyPushQuestScript extends Quest
{Script to capture and log significant events, to be pushed
by our external push service.}
 
Event OnInit()
    Maintenance() ; OnPlayerLoadGame will not fire the first time
EndEvent
 
Function Maintenance()
    Debug.Notification("[SkyPush] Welcome to Skyrim Push, logging enabled.")
    Debug.OpenUserLog("PushLog")
EndFunction
