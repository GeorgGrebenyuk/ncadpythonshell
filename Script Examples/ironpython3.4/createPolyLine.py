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
with doc.LockDocument():
	with doc.Database as db:
		with db.TransactionManager.StartTransaction() as t:
			bt = t.GetObject(db.BlockTableId,AuxiliaryCommands.OpenModeRead)
			btr  = t.GetObject(bt[BlockTableRecord.ModelSpace],AuxiliaryCommands.OpenModeWrite)
			# Do action here
			pl = Polyline()
			pl.AddVertexAt(0,Point2d(0.0, 0.0), 0.0, 0.0, 0.0)
			pl.AddVertexAt(1,Point2d(100.0, 0.0), 0.0, 0.0, 0.0)
			pl.AddVertexAt(2,Point2d(100.0, 100.0), 0.0, 0.0, 0.0)
			pl.AddVertexAt(3,Point2d(0.0, 100.0), 0.0, 0.0, 0.0)
			btr.AppendEntity(pl)
			t.AddNewlyCreatedDBObject(pl,True)
			t.Commit()