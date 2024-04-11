#Copyright(c) 2021  Hồ Văn Chương
# @chuongmep  https://chuongmep.com/
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
			btr = t.GetObject(bt[BlockTableRecord.ModelSpace], AuxiliaryCommands.OpenModeWrite)
			# Do action here
			box = Solid3d()
			box.CreateBox(1000,2000,3000)
			matrix = ed.CurrentUserCoordinateSystem
			matrix = matrix * Matrix3d.Displacement(Vector3d(111, 222, 333))
			box.TransformBy(matrix)
			btr.AppendEntity(box)
			t.AddNewlyCreatedDBObject(box, True)
			t.Commit()
			print("Created Box")