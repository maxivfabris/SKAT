# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 18:17:36 2021

@author: max-v
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 17:48:07 2021

@author: max-v
"""

import cv2
import numpy as np
import os

directory = r'C:\NeuralNet\datasets\huelse_dataset_64x64\images'+'/'   ### image directory
#label_path=r'C:\NeuralNet\datasets\huelse_dataset_64x64\1_keypoint'+'/'
 
# Picture path
for file in os.listdir(directory):
    #filename = os.fsdecode(file)
    if file.endswith(".jpg") or file.endswith(".png"):
        filename=directory+file

        img = cv2.imread(filename)
        (h, w, d) = img.shape
        a = []
        b = []
         
        
         
        def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                xy = "%d,%d" % (x, y)
                a.append(x)
                b.append(y)
                cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
                cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                            1.0, (0, 0, 0), thickness=1)                
                cv2.imshow(file, img)
                print(x,y)
         
        label_path=directory.replace('images', "1_keypoint")+file.replace(".jpg",".txt")
        #label_path=label_path.replace(".jpg",".txt")
        cv2.namedWindow(file)
        cv2.moveWindow(file, 900,700);
        cv2.setMouseCallback(file, on_EVENT_LBUTTONDOWN)
        # with open(label_path, "w") as file:   
                # file.write(a[0]/w, b[0]/h) 
        cv2.imshow(file, img)
        #cv2.waitKey(0)
        k = cv2.waitKey(0) & 0xFF
        # press 'q' to exit
        if k == ord('n'):
            cv2.destroyAllWindows()
        elif k == ord('q'):
            break
        else:
            cv2.destroyAllWindows()
            print("wrong key")
        # if cv2.waitKey(33) == ord('a'):
        #     print("pressed a")
        # if cv2.waitKey(0)&0xFF==2555904:
        # #cv2.imshow("image", img)
        #     print("blabla")
        #     cv2.destroyAllWindows()
        if(len(a)>0):
            with open(label_path, "w") as file:   
                    file.write("%f %f" %(a[0]/w, b[0]/h) )
            print(a[0], b[0])

        

        # if cv2.waitKey(0)&0xFF==27:
        #     break
    
        else:
            print("no keypoint")

cv2.destroyAllWindows()