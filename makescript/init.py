# coding:utf-8
'''
Created on 2013-3-23
@author: dell
'''

import makescript
def StartAuto(ReadPath,PathOut,types):
    print "int:",ReadPath,PathOut
    makescript.SetPath(ReadPath,PathOut)
    makescript.SetTypes( types)
    ##---
    import makescript_auto
    makescript_auto.Auto();
    
def Start(ReadPath,PathOut):
    print "int:",ReadPath,PathOut
    
    makescript.SetPath(ReadPath,PathOut)
    FileList = [
            "",
            "1:商店",
            ]
    for temstr in FileList:
        makescript.TestPrint(temstr)  
    content = "";
    while 1:
        makescript.TestPrint("不输入就编译所有,输入编号就仅编译指定文件(客户端):") 
        content = raw_input("Input:")
        try:
            content = int(content)
        except:
            content = ""
        break
        print "输入错误,文件不存在,你输入的是:", content
    if content in ["", 1, "商店"]:
        import make_shop
        make_shop.DaoBiao();
    
        


