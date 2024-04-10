#Copyright(c) 2021, Hồ Văn Chương
# @chuongmep, https://chuongmep.com/
import clr
clr.AddReference('hostmgd')
clr.AddReference('hostdbmgd')
clr.AddReference('CADCommands')
#clr.AddReference('ncBIMSmgd')
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
with doc.LockDocument():
	with doc.Database as db:
		with db.TransactionManager.StartTransaction() as t:
			bt = t.GetObject(db.BlockTableId,AuxiliaryCommands.OpenModeRead)
			btr  = t.GetObject(bt[BlockTableRecord.ModelSpace],AuxiliaryCommands.OpenModeWrite)
			centerPt = Point3d(0,0,0)
			radius = 50
			circle = Circle(centerPt, Vector3d.ZAxis, radius)		
			btr.AppendEntity(circle)
			t.AddNewlyCreatedDBObject(circle,True)
			t.Commit()
			print("Circle Created")