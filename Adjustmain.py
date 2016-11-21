# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:47:23 2016

@author: ghat
"""

#import makeimagelist
import os
import aligment
import facecrop
import textutil

def test(ImagePath,savePathAligned,savePathCroped,fileformat=['png','jpg'],tag_recover=False,savesize=[64,64]):
    '''
    必须提供的参数：
	1，@ImagePath：待检测和对齐的图像路径
	2，@savePathAligned：保存对齐后的人脸文件夹路径
     3，@savePathCroped：保存对齐后专注五官的人脸文件夹路径
	可选的参数（有默认值）：
	4，@fileformat：图像的格式列表，默认为png和jpg格式
	5，@tag_recover: 是否先裁剪处人脸图像之后再做归一化，默认为False
	6, @savesize: 检测后保留的人脸图像的大小，当tag_recover=True 的时候，才会生效，默认大小为64*64
	
    '''
    
    if not os.path.exists(savePathAligned):
	os.makedirs(savePathAligned)
    if not os.path.exists(savePathCroped):
	os.makedirs(savePathCroped)
     
    AB5plist='./Output/CASIA_imglist_5p.txt'
    RE5plist='./Output/CASIA_imglist_5p_Relative.txt'
    textutil.replace_file(AB5plist,RE5plist,ImagePath)
    #five point file's absolute path and relative path 
    
    count=textutil.count_text_line(AB5plist)
    print 'There are '+str(count)+' pictures.'
          
    print 'Begin Alignment Face.'
    aligment.align_all(RE5plist,ImagePath,savePathAligned)
    print 'Done Alignment Face.'
    
    print 'Begin Face croped in.'
    facecrop.face_crop_in(savePathAligned,savePathCroped,RE5plist,savesize[0],savesize[1])
    print 'Done Face croped in.'
    print 'All work is done!'

if __name__ == "__main__" :
    '''
    @param: 提供的参数：1，图像的文件名位置，2，需要保留的文件位置，3，图像的格式列表
    '''
    ImagePath=r'/home/ghat/deepface/CASIA_WebFace'
    savePathAligned=r'/media/ghat/新加卷1/CASIA64/aligned'
    savePathCroped=r'/media/ghat/新加卷1/CASIA224/croped'
    test(ImagePath,savePathAligned,savePathCroped,tag_recover=True,savesize=[224,224])#[height,wide]
