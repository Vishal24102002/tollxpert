import cv2import easyocrdef retry(gfg,text_sc,tex):    reader2 = easyocr.Reader(['en'],verbose=False)    img2=cv2.imread(gfg)    cv2.imshow("real",img2)    img_gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)    cv2.imshow("gray",img_gray2)    _,img_thresh2=cv2.threshold(img_gray2,130,255,cv2.THRESH_TOZERO)    cv2.imshow("thresh",img_thresh2)    result1=reader2.readtext(img_thresh2)    text2=result1[0][1]    text_score2=result1[0][2]    if len(text2)==0:        print("can't detect")    else:        if text_score2>=0.8 and text_score2<0.9:            text_sc=text_sc+0.1            print("plate :",text2)            print("accuracy:",text_sc*100)        elif text_score2<1 and text_score2>0.9:            print("plate",tex)            print("accuracy:",text_sc*100)        elif text_score2<0.5 and text_score2>0.4:            text_sc=text_sc+0.45            print("plate",tex)            print("accuracy:",text_sc*100)        elif text_score2<=0.79 and text_score2>0.65 :            text_sc=text_sc+0.20            print("plate",tex)            print("accuracy:", text_sc * 100)        elif text_score2<=0.65 and text_score2>=0.5:            text_sc = text_sc + 0.20            print("plate", tex)            print("accuracy:", text_sc * 100)        elif text_score2<0.4 and text_score2>0.3:            text_sc = text_sc + 0.50            print("plate", tex)            print("accuracy:", text_sc * 100)        else:            text_sc = text_sc + 0.60            print("plate", tex)            print("accuracy:", text_sc * 100)    cv2.waitKey(0)pos=input("enter the path")reader = easyocr.Reader(['en'],verbose=False)img=cv2.imread(pos)cv2.imshow("real",img)img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)cv2.imshow("gray",img_gray)_,img_thresh=cv2.threshold(img_gray,30,255,cv2.THRESH_TOZERO)cv2.imshow("thresh",img_thresh)result=reader.readtext(img_gray)text=result[0][1]text_score=result[0][2]if len(text)==0:    retry(pos,text_score)elif len(text)!=0:    if text_score>0.90 and len(text)>=6:        print("most accurate result")        retry(pos,text_score,text)    elif text_score<0.8 and len(text)>=6:        print("result")        retry(pos,text_score,text)else:    print("can't detect try with more clear image")cv2.waitKey(0)