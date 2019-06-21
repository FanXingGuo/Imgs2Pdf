from PIL import Image
import os
import sys


def getImgList():
    file_list=[]

    for file_name in os.listdir("."):
        if "jpg" in file_name:
            file_list.append(file_name)
    file_list.sort()
    return file_list
def threshold(num):
    table = []
    for i in range(256):
        if i < num:
            table.append(0)
        else:
            table.append(1)
    return table
def getP_ImgList(imgList,ts_List):
    new_pic=[]
    for imgName in imgList[1:]:
        p=Image.open(imgName)
        p_wb=p.convert("L")
        p1=p_wb.point(ts_List,"1")
        p1=p1.convert("RGB")
        new_pic.append(p1)

    return new_pic

if __name__ == '__main__':
    argv=sys.argv

    num=int(argv[1]) # 140
    file_name=argv[2]

    imgList=getImgList()
    table=threshold(num)
    im_list=getP_ImgList(imgList,table)

    im1=Image.open(imgList[0])
    im1=im1.convert("L")
    im1=im1.point(table,"1")
    im1=im1.convert("RGB")

    im1.save(file_name,"PDF", resolution=100.0, save_all=True, append_images=im_list)







