import csv
import pandas as pd
import numpy as np
#1. chuyển string sang số
def strfloat(s):
  if s[0]>'9' or s[0]<'0':
    return -1
  return float(s)

#2. kiểm tra sinh viên có phải D19 và học CN
def checkclass(s): # ktra B19DCCNXXX
  if s[2]!='9' or s[5]!='C' :
    return False
  return True

#3.chuyển điểm hệ 10 sang hệ 4
def convertGPA(n):
  if n < 4 :
    ans=0
  elif n< 5 :
    ans=1
  elif n< 5.5 :
    ans=1.5
  elif n< 6.5 :
    ans =2.0
  elif n< 7 :
    ans=2.5
  elif n< 8 :
    ans=3.0
  elif n<8.5:
    ans=3.5
  elif n< 9 :
    ans=3.7
  elif n<=10 :
    ans=4.0
  return ans

#4.từ file csv chuyển thảnh mảng 2 chiều với [i][0]= msv, [i][1] điểm đã * tín chỉ 
def diem(path,tc) :
  ds=[]
  with open(path) as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
      if checkclass(row[0]) == True and convertGPA(strfloat(row[1])) > 0 :
        tmp=[]
        tmp.append(row[0])
        tmp.append(convertGPA(strfloat(row[1]))*tc)
        ds.append(tmp)
  return ds

#5.tìm kiếm msv ở vị trí nào của điểm môn nào
def vitri(msv,csv):
  for i in range (len(csv)):
    if msv==csv[i][0]:
      return i
  return -1

#6.tạo mảng 2 chiều lưu msv, điểm
mmt=diem("mmt.csv",3)
hdh=diem("hdh.csv",3)
csdl=diem("csdl.csv",3)
python=diem("python.csv",3)
oop=diem("oop.csv",3)
eng=diem("english.csv",4)
#7.
def checktontai(msv):
  if vitri(msv,mmt) == -1 or vitri(msv,hdh)==-1 or vitri(msv,csdl)==-1 or vitri(msv,python)==-1 or vitri(msv,oop)==-1 :
    return False
  return True

#8.tạo mảng GPA thôi
gpa=[]
for i in range (len(python)) :
  msv=python[i][0]
  tmp=[]
  tmp.append(msv)
  tong=0
  tc=0
  if vitri(msv,python) != -1:
    tong+=python[vitri(msv,python)][1]
    tc+=3
  if vitri(msv,mmt) != -1:
    tong+=mmt[vitri(msv,mmt)][1]
    tc+=3
  if vitri(msv,hdh) != -1:
    tong+=hdh[vitri(msv,hdh)][1]
    tc+=3
  if vitri(msv,csdl) != -1:
    tong+=csdl[vitri(msv,csdl)][1]
    tc+=3
  if vitri(msv,oop) != -1:
    tong+=oop[vitri(msv,oop)][1]
    tc+=3
  if vitri(msv,eng) != -1:
    tong+=eng[vitri(msv,eng)][1]
    tc+=4
  tmp.append(tong/tc)
  gpa.append(tmp)

#9. tạo 2 mảng lưu msv, gpa của mảng gpa
col_1=[]
col_2=[]
for i in range(len(gpa)):
  col_1.append(gpa[i][0])
  col_2.append(round(gpa[i][1],2))
#10. sort theo điểm 
for i in range (0,len(col_2)-1):
  for j in range (i+1,len(col_2)):
    if col_2[j] > col_2[i]:
      col_2[j], col_2[i] = col_2[i], col_2[j]
      col_1[j], col_1[i] = col_1[i], col_1[j]
stt=[]
stt.append(1)
tmp = 1
tg=tmp
for i in range(1,len(col_2)):
  if col_2[i]==col_2[i-1] :
    stt.append(tg)
    tmp+=1
  else :
    tmp+=1
    tg=tmp
    stt.append(tg)


#11. lưu file thôi
submission=pd.DataFrame({'STT':stt,'MSV':col_1, 'GPA':col_2})
submission.to_csv('GPA_D19.csv',index=False)