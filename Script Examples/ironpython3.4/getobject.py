import clr
clr.AddReference('hostmgd')
clr.AddReference('hostdbmgd')

# Import references from nanoCAD
from Teigha.Runtime import *
from HostMgd.ApplicationServices import *
from HostMgd.EditorInput import *
from Teigha.DatabaseServices import *
from Teigha.Geometry import *


adoc = Application.DocumentManager.MdiActiveDocument
ed = adoc.Editor
output =[]
with adoc.LockDocument():
    with adoc.Database as db:
        with db.TransactionManager.StartTransaction() as t:
            bt = t.GetObject(db.BlockTableId, OpenMode.ForWrite)
            btr = t.GetObject(bt[BlockTableRecord.ModelSpace], OpenMode.ForWrite)
            for objectid in btr:
                obj1 = t.GetObject(objectid, OpenMode.ForRead)
                output.append(obj1)
                print(obj1)
ed.WriteMessage("Done")