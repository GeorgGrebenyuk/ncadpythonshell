# ncadpythonshell
Расширение к nanoCAD для поддержки скриптов на IronPython 3.4.1 (доступ к NET API)

# О надстройке. Отличия от оригинальной версии
Настоящий исходный код является переработкой известного плагина к AutoCAD `CadPythonShell` от Chuong Ho (https://github.com/chuongmep/CadPythonShell).
По сравнению с оригинальной версией:
* Удалены проекты, относящиеся к MgdDbg (обозреватель классов объектов). Эта функциональность будет распространяться в рамках иного решения от nanosoft;
* Удален проект инсталлятора (пока будет распространяться без оного);
* Все библиотеки изменены для поддержки nanoCAD 22 и старше и nanoCAD 23 и новее (2 разные конфигурации), так как до nanoCAD 23 библиотеки были на .NET Framework; позже -- на .NET6 (этим обусловлен и отказ от некоторых пакетов из оригинальной версии);
* Для возможности запуска скриптов на .NET6 (nc23+) введена дополнительная библиотека `CADCommands` (см. раздел `Проблемы работы на nanoCAD 23+ (.NET 6)`)


## Установка и использование

Из раздела Releases скачайте последнюю версию надстройки и распакуйте в любую папку. В зависимости от использования для nanoCAD 22 и старше - ваша версия будет `Nc22_22`, для 23 и новее -- `Nc_23`.
Поставьте в автозагрузку nanoCAD файл `nCADPythonShell.package`.
Из новой ленты в nanoCAD `nCAD Python Shell` запустить команду `Run NPS`

__Наиболее стабильно__ работает на 22 версии nanoCAD (до миграции на .NET6). Здесь любые ошибки будут отображаться в "верхней" форме окна и не приводить к фатальному вылету.

### Примеры кода

См. в папке `\Script Examples\ironpython3.4\`

### Начало кода

Строки ниже необходимо добавлять в шапку каждого из скриптов. Если код предполагает обращение к классам вне упомянутых пространств имен, то их также необходимо будет указать через директивы `import`.
```python
import clr
#Import nanoCAD's libraries
clr.AddReference('hostmgd')
clr.AddReference('hostdbmgd')
#Import auxiliary library (look chapter below, exception for 23+ versions)
clr.AddReference('CADCommands')
#Import namespaces for nanoCAD and CADCommands
from Teigha.Runtime import *
from HostMgd.ApplicationServices import *
from HostMgd.EditorInput import *
from Teigha.DatabaseServices import *
from Teigha.Geometry import *
from CADCommands import *
```

### Проблемы работы на nanoCAD 23+ (.NET 6)

Настоящие проблемы возможно будут решены, как автор надстройки адаптирует её для AutoCAD 2025 (где появился .NET8).
Все перечисленные далее проблемы приводят к фатальному вылету nanoCAD с `Неустранимой ошибкой` в режиме открытия скрипта (окно ниже). В верхнем окне будет просто выбрасываться исключение, поэтому для тестов __настоятельно рекомендуется__ использовать именно верхнее окно с построчным вводом скрипта.

* Неверная интерпретация enum: например, частая конструкция `OpenMode.ForRead` и т.д. Решено вводом класса AuxiliaryCommands из CADCommands.То есть вводится следующее соответствие:

```python
OpenMode.ForRead = AuxiliaryCommands.OpenModeRead
OpenMode.ForWrite = AuxiliaryCommands.OpenModeWrite
OpenMode.ForNotify = AuxiliaryCommands.OpenModeNotify
```

* Неверная интерпретация наследуемых классов: когда какой-либо метод в API ожидает "базовый" класс, а ему подается наследник. Например, популярная процедура AppendEntity (добавление созданного объекта в чертеж) ожидает тип `Entity`, а все объекты имеют свои классы: Circle, Polyline и т.д. Решение: пока отсутствует. Принудительная конфертация через библиотеку clr не работает:

```python
centerPt = Point3d(0,0,0)
circle = Circle(centerPt, Vector3d.ZAxis, 2)
circle_as_entity = clr.Convert(circle, Entity)
btr.AppendEntity(circle_as_entity)
#Error: expected Entity, got Circle
```