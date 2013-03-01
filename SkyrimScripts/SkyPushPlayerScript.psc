ScriptName SkyPushPlayerScript extends Actor
 
SkyPushQuestScript Property QuestScript Auto
  
Event OnPlayerLoadGame()
	QuestScript.Maintenance()
EndEvent

Event OnLocationChange(Location akOldLoc, Location akNewLoc)
    Debug.TraceUser("PushLog", "[SkyPush][Location] " + akNewLoc.GetName())
    Debug.Notification("[SkyPush][Location] " + akNewLoc.GetName())
endEvent

