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

## Get Color
import Teigha.Colors.EntityColor as cl
rgbcad = cl.LookUpRgb(111)
print(rgbcad)
blue = rgbcad & 255
green = (rgbcad >> 8) & 255
red = (rgbcad >> 16) & 255
print("Color RGB is", (red,green,blue))

## see more at : https://forum.dynamobim.com/t/aci-color-to-rgb/59856/6