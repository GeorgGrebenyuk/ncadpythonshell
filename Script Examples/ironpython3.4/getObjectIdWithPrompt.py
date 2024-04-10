#Copyright(c) 2021, Hồ Văn Chương
# @chuongmep, https://chuongmep.com/
import clr
clr.AddReference('hostmgd')
clr.AddReference('hostdbmgd')
clr.AddReference('CADCommands')
# Import references from nanoCAD
from Teigha.Runtime import *
from HostMgd.ApplicationServices import *
from HostMgd.EditorInput import *
from Teigha.DatabaseServices import *
from Teigha.Geometry import *
from CADCommands import *

doc = Application.DocumentManager.MdiActiveDocument
ed = doc.Editor
db = doc.Database
# Write Code Below
def GetObjectIdWithPrompt(editor):
	result = editor.GetEntity("Please Select an Entity")
	if(result.Status!= PromptStatus.OK) : return
	editor.WriteMessage(result.ObjectId.ObjectClass.Name)
	print("Object Class Name:",result.ObjectId.ObjectClass.Name)
GetObjectIdWithPrompt(ed)