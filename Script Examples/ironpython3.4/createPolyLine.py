#Copyright(c) 2021, Hồ Văn Chương
# @chuongmep, https://chuongmep.com/
import clr
clr.AddReference('hostmgd')
clr.AddReference('hostdbmgd')

# Import references from nanoCAD
from Teigha.Runtime import *
from HostMgd.ApplicationServices import *
from HostMgd.EditorInput import *
from Teigha.DatabaseServices import *
from Teigha.Geometry import *


doc = Application.DocumentManager.MdiActiveDocument
ed = doc.Editor
db = doc.Database
# Write Code Below
with doc.LockDocument():
	with doc.Database as db:
		with db.TransactionManager.StartTransaction() as t:
			bt = t.GetObject(db.BlockTableId,OpenMode.ForRead)
			btr  = t.GetObject(bt[BlockTableRecord.ModelSpace],OpenMode.ForWrite)
			# Do action here
			pl = Polyline()
			pl.AddVertexAt(0,Point2d(0.0, 0.0), 0.0, 0.0, 0.0)
			pl.AddVertexAt(1,Point2d(100.0, 0.0), 0.0, 0.0, 0.0)
			pl.AddVertexAt(2,Point2d(100.0, 100.0), 0.0, 0.0, 0.0)
			pl.AddVertexAt(3,Point2d(0.0, 100.0), 0.0, 0.0, 0.0)
			pl_as_ent = clr.Convert(pl, Entity)
			btr.AppendEntity(pl_as_ent)
			t.AddNewlyCreatedDBObject(pl,True)
			t.Commit()