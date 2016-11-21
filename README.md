# facetools
  FaceTools have 2 function.[align and crop].  
  Before using Adjustmain.py plz change the path in it.  
  
  1.Create a list of files (manually placing standard.jpg on the first line so that it becomes the reference image when aligned.)  
  2.Use the demo.m in MTCNNv2 for face key detection (output binocular, nasal tip, mouth position). Modify its input and output file path (output to the facetools under the output file)  
  3.Use Adjustmain.py,modify its input and output file paths. (The code for the third part) 
  
  
基于 https://github.com/RiweiChen/FaceTools 的人脸切割和 https://github.com/kpzhang93/MTCNN_face_detection_alignment 的人脸关键点检测。  
1.创建文件列表（手动将standard.jpg放在第一行，目的是使其成为对齐时参考图像。）  
2.使用MTCNNv2中的demo.m进行人脸关键点检测（输出双眼、鼻尖、嘴角的位置）。修改其代码设置输入和输出文件路径（我将其输出到facetools下output文件内）  
3.使用Adjustmain.py 修改其输入和输出文件路径。  
本代码为第三部分。
