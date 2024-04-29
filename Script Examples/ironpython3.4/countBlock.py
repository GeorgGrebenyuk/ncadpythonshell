#Many thanks Cyril-Pop
import clr
clr.AddReference('hostmgd')
clr.AddReference('hostdbmgd')

#clr.AddReference('ncBIMSmgd')
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
all_blkName = []
with doc.LockDocument():
	with doc.Database as db:
		with db.TransactionManager.StartTransaction() as t:
			bt = t.GetObject(db.BlockTableId, OpenMode.ForRead)
			btr  = t.GetObject(bt[BlockTableRecord.ModelSpace], OpenMode.ForRead)
			for objectid in btr:
				blkRef = t.GetObject(objectid, OpenMode.ForRead)				
				if isinstance(blkRef, BlockReference):
					if blkRef.IsDynamicBlock:
						block = t.GetObject(blkRef.DynamicBlockTableRecord, OpenMode.ForRead)
						all_blkName.append(block.Name)
					else:
						all_blkName.append(blkRef.Name)	
			resultcount = ["{} - total:{}".format(x, all_blkName.count(x)) for x in set(all_blkName)]
			print("\n".join(resultcount))
			t.Commit()
print(all_blkName)