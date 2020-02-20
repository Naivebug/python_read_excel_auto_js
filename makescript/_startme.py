# -*- coding: utf-8 -*-
'''
Created on 2013-5-2
@author: dell
'''


import init


#ReadPath = "F:/project/svnremote/svnroot/game/h5/farm/doc/程序文档/";
#PathOut = "F:/project/svnremote/svnroot/game/h5/farm/doc/程序文档/mkdata"
ReadPath = "./../";
PathOut = "./../mkdata/"
types = {"type":"js","module":False} #配置导出类型,
#init.Start(ReadPath,PathOut)
init.StartAuto(ReadPath,PathOut,types)


