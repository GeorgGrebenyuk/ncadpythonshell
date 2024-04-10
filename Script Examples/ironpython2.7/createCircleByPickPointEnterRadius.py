#Copyright(c) 2021, Hồ Văn Chương
# @chuongmep, https://chuongmep.com/
import clr
clr.AddReference('acmgd')
clr.AddReference('acdbmgd')
clr.AddReference('accoremgd')
# Import references from AutoCAD
from Autodesk.AutoCAD.Runtime import *
from Autodesk.AutoCAD.ApplicationServices import *
from Autodesk.AutoCAD.EditorInput import *
from Autodesk.AutoCAD.DatabaseServices import *
from Autodesk.AutoCAD.Geometry import *
doc = Application.DocumentManager.MdiActiveDocument
ed = doc.Editor
db = doc.Database
#Code Here : 
result1 = ed.GetPoint("Please select a point")
if(result1.Status == PromptStatus.OK):
	centerPt = result1.Value
result2 = ed.GetInteger("Please input radius")
if(result2.Status == PromptStatus.OK):
	radius = result2.Value
with doc.LockDocument():
	with doc.Database as db:
		with db.TransactionManager.StartTransaction() as t:
			bt = t.GetObject(db.BlockTableId,OpenMode.ForRead)
			btr  = t.GetObject(bt[BlockTableRecord.ModelSpace],OpenMode.ForWrite)
			circle = Circle(centerPt, Vector3d.ZAxis, radius)
			btr.AppendEntity(circle)
			t.AddNewlyCreatedDBObject(circle,True)
			t.Commit()
			print("Circle Created")