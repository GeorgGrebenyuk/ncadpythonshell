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
#Code Here : 
objects = []
p1 = Point3d(0,0,0)
p2 = Point3d(100,100,0)
line1 = Line(p1,p2)
with doc.LockDocument():
	with doc.Database as db:
		with db.TransactionManager.StartTransaction() as t:
			bt = t.GetObject(db.BlockTableId,OpenMode.ForRead)
			btr  = t.GetObject(bt[BlockTableRecord.ModelSpace],OpenMode.ForWrite)
			btr.AppendEntity(line1)
			t.AddNewlyCreatedDBObject(line1,True)
			t.Commit()
			print("Line Created")