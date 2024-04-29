#Copyright(c) 2021, Hồ Văn Chương
# @chuongmep, https://chuongmep.com/
import clr
import math
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
#Code Here : 
with doc.LockDocument():
	with doc.Database as db:
		with db.TransactionManager.StartTransaction() as t:
			bt = t.GetObject(db.BlockTableId,OpenMode.ForRead)
			btr  = t.GetObject(bt[BlockTableRecord.ModelSpace],OpenMode.ForWrite)
			centerPt = Point3d(0,0,0)
			radius = 50
			arc = Arc(centerPt,Vector3d.ZAxis,radius,0,math.pi / 2)
			btr.AppendEntity(arc)
			t.AddNewlyCreatedDBObject(arc,True)
			t.Commit()
			print("Arc Created")