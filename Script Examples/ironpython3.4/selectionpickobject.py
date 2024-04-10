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
#Code Here : 
objects = []
with doc.LockDocument():
	with doc.Database as db:
		with db.TransactionManager.StartTransaction() as t:
			acblkbl = t.GetObject(db.BlockTableId,AuxiliaryCommands.OpenModeRead)
			print(type(acblkbl))
			acblktblrec = t.GetObject(acblkbl[BlockTableRecord.ModelSpace],AuxiliaryCommands.OpenModeWrite)
			print(type(acblktblrec))
			sel = doc.Editor.GetSelection()
			if(sel.Status== PromptStatus.OK):
				results = sel.Value
				for i in range(len(results)):
					if(results[i] != None) : objects.append(i)
			else : pass
print("Count Object Exploded:",len(objects))