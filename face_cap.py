# -*- coding: utf-8 -*-

import dlib  # 人脸识别的库dlib
import numpy as np  # 数据处理的库numpy
import cv2  # 图像处理的库OpenCv
from time import localtime,strftime
from skimage import io as iio
import os
import db
import _thread
import threading




PATH_FACE = "data/face_img_database/"
# face recognition model, the object maps human faces into 128D vectors
facerec = dlib.face_recognition_model_v1("model/dlib_face_recognition_resnet_model_v1.dat")
# Dlib 预测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('model/shape_predictor_68_face_landmarks.dat')
# 打卡时间
puncard_time = "00:00:00"

def return_euclidean_distance(feature_1, feature_2):
    feature_1 = np.array(feature_1)
    feature_2 = np.array(feature_2)
    dist = np.sqrt(np.sum(np.square(feature_1 - feature_2)))
    print("欧式距离: ", dist)
    if dist > 0.4:
        return 'diff'
    else:
        return 'same'


class Face:
    def __init__(self):
        self.initData()

    def initData(self):
        '''初始化变量'''

        # self.name = '周梦泽'
        # self.id = 9527

        self.name = ''
        self.id = None

        self.face_feature = ''
        self.pic_num = 0
        self.flag_registed = False
        self.puncard_time = '21:00:00'
        # self.db.loadDataBase(1)
        
    def getDateAndTime(self):
        '''获取当下时间'''

        dateandtime = strftime("%Y-%m-%d %H:%M:%S",localtime())
        return "["+dateandtime+"]"

    def OnFinishRegister(self, id, name):
        self.id = id
        self.name = name

        # self.new_register.Enable(True)
        # self.finish_register.Enable(False)
        # self.cap.release()

        # self.bmp.SetBitmap(wx.Bitmap(self.pic_index))
        if self.flag_registed == True:
            # dir = PATH_FACE + self.name
            # for file in os.listdir(dir):
            #     os.remove(dir+"/"+file)
            #     print("已删除已录入人脸的图片", dir+"/"+file)
            # os.rmdir(PATH_FACE + self.name)
            # print("已删除已录入人脸的姓名文件夹", dir)
            self.initData()
            # return
        if self.pic_num>0:
            pics = os.listdir(PATH_FACE + str(self.id) + '/' + self.name)
            feature_list = []
            feature_average = []
            for i in range(len(pics)):
                pic_path = PATH_FACE + str(self.id) + '/' + self.name + "/" + pics[i]
                print("正在读的人脸图像：", pic_path)
                img = iio.imread(pic_path)
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                dets = detector(img_gray, 1)
                if len(dets) != 0:
                    shape = predictor(img_gray, dets[0])
                    face_descriptor = facerec.compute_face_descriptor(img_gray, shape)
                    feature_list.append(face_descriptor)
                else:
                    face_descriptor = 0
                    print("未在照片中识别到人脸")
            if len(feature_list) > 0:
                for j in range(128):
                    #防止越界
                    feature_average.append(0)
                    for i in range(len(feature_list)):
                        feature_average[j] += feature_list[i][j]
                    feature_average[j] = (feature_average[j]) / len(feature_list)
                db.insertARow([self.id,self.name,feature_average],1)
                print(self.getDateAndTime()+"工号:"+str(self.id)
                                     +" 姓名:"+self.name+" 的人脸数据已成功存入\r\n")
            # pass
        # else:
            # os.rmdir(PATH_FACE + self.name)
            # print("已删除空文件夹",PATH_FACE + self.name)
        self.initData()

    def face_Operation(self):
        '''摄像头人脸处理'''

        self.cap = cv2.VideoCapture(0)
        while self.cap.isOpened():
            im_rd = cv2.flip(self.cap.read()[1], 1)
            cv2.waitKey(1)

            self.dets = detector(im_rd, 1)
            if len(self.dets) != 0:
                self.biggest_face = self.dets[0]
                maxArea = 0
                for det in self.dets:
                    w = det.right() - det.left()
                    h = det.top()-det.bottom()
                    if w*h > maxArea:
                        self.biggest_face = det
                        maxArea = w*h
                cv2.rectangle(im_rd, tuple([self.biggest_face.left(), self.biggest_face.top()]),
                                      tuple([self.biggest_face.right(), self.biggest_face.bottom()]),
                                      (255, 0, 0), 2)
                # img_height, img_width = im_rd.shape[:2]

                # image_rgb = cv2.cvtColor(im_rd, cv2.COLOR_BGR2RGB)
                # image_flip = cv2.flip(image_rgb, 1)
                # cv2.imshow("capture", image_flip)


                shape = predictor(im_rd, self.biggest_face)
                features_cap = facerec.compute_face_descriptor(im_rd, shape)

                # i = None; knew_face_feature=None
                # 有3种情况 1.不相同返回diff 2.相同返回same 3.数据库为空不执行for循环以下代码 
                for i,knew_face_feature in enumerate(db.loadDataBase(1)[2]):

                    compare = return_euclidean_distance(features_cap, knew_face_feature)
                    print(compare)
                    yield i,compare, im_rd

                if not db.loadDataBase(1)[2]:
                    yield None, None, im_rd
            else:
                # 这两个None并无实际意义，只作占位使得与上一句  yield i,compare, im_rd  调用相同
                yield None, None, im_rd
            # cv2.imshow('A Moron', im_rd)
    def register(self, id, name):
        '''注册人脸'''

        self.id = id; self.name = name
        dir = PATH_FACE + str(self.id) + '/' + self.name
        if not os.path.exists(dir):
            os.makedirs(dir)
        print(self.name, self.id)
        perform = 'nothing'
        for i,compare, im_rd in self.face_Operation():
            # print(compare)

            if len(self.dets) != 0:
                if compare == 'same':  # 找到了相似脸
                    print('你的人脸数据已存在')
                    perform = 'existed'
                    # self.cap.release()
                    # self.flag_registed = True
                    # self.OnFinishRegister()
                
                elif compare =='diff' or compare ==None:
                    
                    perform = 'loading'

                    face_height = self.biggest_face.bottom() - self.biggest_face.top()
                    face_width = self.biggest_face.right() - self.biggest_face.left()
                    im_blank = np.zeros((face_height, face_width, 3), np.uint8)

                    try:

                        for ii in range(face_height):
                            for jj in range(face_width):
                                im_blank[ii][jj] = im_rd[self.biggest_face.top() + ii][self.biggest_face.left() + jj]

                        if len(self.name)>0:
                            print('pic_num=', self.pic_num)
                            cv2.imencode('.jpg', im_blank)[1].tofile(
                            PATH_FACE + str(self.id) + '/' + self.name + "/img_face_" + str(self.pic_num) + ".jpg")  # 正确方法
                            self.pic_num += 1

                            print("写入本地：", str(PATH_FACE + self.name) + "/img_face_" + str(self.pic_num) + ".jpg")
                            print("保存成功")

                    except:
                        perform = 'abnormal'
                        print("照片保存异常,请对准摄像头")
                    # else:
                    #     print('找不到相似')
                    if self.pic_num == 10:
                        self.OnFinishRegister(id, name)
                        perform = 'res_succ'
                        # exit(0)
            
            yield im_rd, perform
                
    def punchcard_cap(self):
        '''打卡'''
        
        for i, compare, im_rd in self.face_Operation():
            if compare == 'same':  # 找到了相似脸
                # print("same")
                flag = 0
                nowdt = self.getDateAndTime()

                # 数据库可能为空,for循环就会不执行
                for j,logcat_name in enumerate(db.loadDataBase(2)[1]):
                    if logcat_name == db.loadDataBase(1)[1][i]  and  nowdt[0:nowdt.index(" ")] == db.loadDataBase(2)[2][j][0:db.loadDataBase(2)[2][j].index(" ")]:
                        print(nowdt+"工号:"+ str(db.loadDataBase(1)[0][i])
                                         + " 姓名:" + db.loadDataBase(1)[1][i] + " 签到失败,重复签到\r\n")
                        flag = 1; perform = 'repeat'
                    #     break
                    # if flag == 1:
                    #     break
                if flag == 0:
                    if nowdt[nowdt.index(" ")+1:-1] <= puncard_time:
                        print(nowdt + "工号:" + str(db.loadDataBase(1)[0][i])
                                             + " 姓名:" + db.loadDataBase(1)[1][i] + " 成功签到,且未迟到\r\n")
                        db.insertARow([db.loadDataBase(1)[0][i],db.loadDataBase(1)[1][i],nowdt,"否"],2)
                        perform = 'success'

                    else:
                        print(nowdt + "工号:" + str(db.loadDataBase(1)[0][i])
                                                 + " 姓名:" + db.loadDataBase(1)[1][i] + " 成功签到,但迟到了\r\n")
                        db.insertARow([db.loadDataBase(1)[0][i], db.loadDataBase(1)[1][i], nowdt, "是"], 2)
                        perform = 'late'
                    # db.loadDataBase(2)
            
            elif compare == 'diff':
                print('识别失败')
                perform = 'fail'
            else:
                perform = 'nothing'
            yield im_rd, perform

    def finish(self):
        '''退出所有任务'''
        try:
            self.cap.release()
            exit(0)
        except:
            # exit(0)
            pass

face = Face()
# face.register()

if __name__ == '__main__':

# 注册
    face.register()
# 打卡
# face.punchcard_cap()



