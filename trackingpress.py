#!/usr/bin/python3

import os

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

print ("Hello TrackingPress")
system = OsInfo()
print (system.getSysname())
print (system.getVersion())
print (system.getRelease())
