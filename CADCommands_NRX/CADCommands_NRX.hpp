#pragma once

using namespace System;
using namespace Teigha::Runtime;

namespace CADCommandsNRX {
	public ref class AuxiliaryTools : IExtensionApplication
	{
	public:
		static void CreateObject(IntPtr^ ptr) {

			AcDbEntity* nCAD_Entity = (AcDbEntity*)ptr->ToInt64();
			if (nCAD_Entity)
			{
				AcDbObjectId entId;
				pBlockTableRecord->appendNcDbEntity(entId, nCAD_Entity);
			}
		}

		static property AcDbBlockTableRecord* pBlockTableRecord {
	public: AcDbBlockTableRecord* get() {
		AcDbDatabase* pCurDb = acDocManager->curDocument()->database();
		AcDbBlockTable* pBlockTable;
		acdbHostApplicationServices()->workingDatabase()
			->getSymbolTable(pBlockTable, AcDb::kForWrite);

		AcDbBlockTableRecord* pBlockTableRecord;
		pBlockTable->getAt(ACDB_MODEL_SPACE, pBlockTableRecord,
			AcDb::kForWrite);
		pBlockTable->close();

		return pBlockTableRecord;
	}
		}

	public:
		virtual void Initialize()
		{

		}

		virtual void Terminate()
		{

		}
	};
}
