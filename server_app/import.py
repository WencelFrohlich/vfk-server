from classes.importer import Importer
from classes.dbmanager import DbManager

files = [
    '/home/enviwork/Dokumenty/ukol_vfk/vfk_files/624217_ZPMZ_00929_vfk.vfk', 
    '/home/enviwork/Dokumenty/ukol_vfk/vfk_files/654175_ZPMZ_00131_vfk.vfk',
    '/home/enviwork/Dokumenty/ukol_vfk/vfk_files/684007_ZPMZ_00331_vfk.vfk',
    '/home/enviwork/Dokumenty/ukol_vfk/vfk_files/709433_1668EX_229716210010.VFK',
]

for file in files:
    vfk_path = file
    Importer(vfk_path)
    print( DbManager().get_unique_vb())
    print(DbManager().delete_by_id(74217535999))
    pass


