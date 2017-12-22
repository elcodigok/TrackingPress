#!/usr/bin/python3

import os
from terminaltables import AsciiTable

class OsInfo:
    def getSysname(self):
        return os.uname().sysname
    
    def getVersion(self):
        return os.uname().version
    
    def getRelease(self):
        return os.uname().release
    
    def getMachine(self):
        return os.uname().machine
    
    def getNodename(self):
        return os.uname().nodename

def main():
    system = OsInfo()
    print (system.getSysname())
    print (system.getVersion())
    print (system.getRelease())
    title = ' TrackingPress. '
    TABLE_DATA = (
        ('Sysname', 'Version', 'Release', 'Name'),
        (system.getSysname(), system.getVersion(), system.getRelease(), system.getNodename()),
    )
    # AsciiTable.
    print ()
    table_instance = AsciiTable(TABLE_DATA, title)
    print(table_instance.table)
    print ()

if __name__ == '__main__':
    main()