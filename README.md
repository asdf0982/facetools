# facetools
FaceTools have 2 function.[align and crop]. 
Before using Adjustmain.py plz change the path in it .
if you have any questions ,plz reply as soon as possible.
基于 https://github.com/RiweiChen/FaceTools 的人脸切割和 https://github.com/kpzhang93/MTCNN_face_detection_alignment 的人脸关键点检测。


1.使用createimglist.py创建文件列表（手动将standard.jpg放在第一行，目的是使其成为对齐时参考图像。）
2.使用MTCNNv2中的demo.m进行人脸关键点检测（输出双眼、鼻尖、嘴角的位置）。修改其输入和输出文件路径（输出到facetool下output文件内）
3.使用Adjustmain.py 修改其输入和输出文件路径。
本代码为第三部分。
