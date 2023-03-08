
# import face_cap
from PySide2.QtGui import QPixmap
from PySide2 import QtGui
from PySide2.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox, QAbstractItemView, QHeaderView
from PySide2 import QtCore
from PySide2 import QtWidgets
# from PySide2.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
# from PySide2.QtCore import QThread, Qt
from Ui_index import Ui_Form
from face_cap import face
import db
import cv2
import sys
import os


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.initData()
        
        # 绑定按钮
        self.ui.pushButton_3.clicked.connect(self.register_button)
        self.ui.pushButton.clicked.connect(self.punchcard_button)
        self.ui.pushButton_2.clicked.connect(self.show_data)
        self.ui.pushButton_4.clicked.connect(self.initData)

        self.perform = 'nothing'
        self.timer.timeout.connect(self.status_text)
        self.timer.start(1000) # 启动计时器 1秒刷新1次

    def initData(self):
        '''默认数据/初始化'''

        face.finish()
        self.timer.timeout.connect(self.showtime)
        self.timer.start(1000) # 启动计时器 1秒刷新1次
        self.setWindowTitle('主页')
        pixmap = QPixmap('img/bg_picture.jpg')
        self.ui.label_2.setPixmap(pixmap)
        self.ui.stackedWidget.setCurrentIndex(0)
        
    
    def closeEvent(self, event):
        '''重写closeEvent函数, 当点击右上角关闭按钮时关闭后台'''

        face.finish()
        self.ui.stackedWidget.setCurrentIndex(0)
        event.accept()


    def showtime(self):
        '''显示时间'''

        datetime = QtCore.QDateTime.currentDateTime()       # 获取当前日期时间
        date_text = datetime.toString("yyyy-MM-dd")     # 对日期时间进行格式化
        time_text = datetime.toString("HH:mm:ss")   # 对日期时间进行格式化
        week_text = datetime.toString("dddd")   #对星期几进行格式化

        self.ui.label_3.setText(time_text)
        self.ui.label_4.setText(date_text)
        self.ui.label_5.setText(week_text)



    def display(self, im_rd):
        '''接收图片, 将每张图片处理并显示出来'''

        # 背景图
        pixmap = QPixmap('img/bg_picture.jpg')
        self.ui.label_7.setPixmap(pixmap)

        image_rgb = cv2.cvtColor(im_rd, cv2.COLOR_BGR2RGB)
        # width = image_rgb.shape[1]
        # height = image_rgb.shape[0]
        height, width = image_rgb.shape[:2]
        
        # 640 x 480
        image = QtGui.QImage(bytes(image_rgb), width, height, 3*width, QtGui.QImage.Format_RGB888)
        # cv2.imshow('cap',image)
        pixmap = QPixmap(image)
        self.ui.label.setPixmap(pixmap)
        # self.ui.label.setScaledContents(True)


    def input_id(self):
        '''工号输入框'''

        self.id_num, self.okPressed = QInputDialog.getInt(
			self,
			'Tips',
			'请输入工号(0-99999)',
            value=0,
            minValue=0,
            maxValue=99999
        )
        print(self.okPressed)


    def register_button(self):
        '''点击人脸录入按钮'''

        self.initData()
        # face.finish()

        self.input_id()
        self.setWindowTitle('人脸录入')


        if self.okPressed:
            '''按下OK后判断工号是否已存在'''
            
            for knew_id in db.loadDataBase(1)[0]:
                print(knew_id)
                if knew_id == self.id_num:
                    QMessageBox.critical( self, '错误', '工号已存在！')
                    self.input_id()

            self.name, okPressed2 = QInputDialog.getText(
                self,
                'Tips',
                '请输入姓名'
            )
            if okPressed2:
                '''按下OK后判断名字是否为空'''
                
                if not self.name:
                    QMessageBox.critical( self, '错误', '姓名为空！')
                else:
                    # print('self.id_num', type(self.id_num))
                    # print('self.name', type(self.name))
                    # height = 680; width = 790
                    self.ui.stackedWidget.setCurrentIndex(1)
                    for im_rd, self.perform in face.register(self.id_num, self.name):

                        # image_rgb = cv2.cvtColor(im_rd, cv2.COLOR_BGR2RGB)
                        # width = image_rgb.shape[1]
                        # height = image_rgb.shape[0]
                        # image = QtGui.QImage(bytes(image_rgb), width, height, 3*width, QtGui.QImage.Format_RGB888)
                        # # cv2.imshow('cap',image)
                        # pixmap = QPixmap(image)
                        # self.ui.label.setPixmap(pixmap)
                        # self.status_text()
                        # 将每张图处理显示
                        self.display(im_rd)
        # self.initData()
    

    def punchcard_button(self):
        '''当点击人脸打卡按钮时触发'''

        # self.initData()\
        face.finish()
        self.ui.stackedWidget.setCurrentIndex(1)
        self.setWindowTitle('人脸打卡')


        for im_rd, self.perform in face.punchcard_cap():

            # self.status_text(self.perform)
            self.display(im_rd)
        # self.initData()



    def show_data(self):
        '''将打卡表显示/加载数据库表格'''

        # self.ui.stackedWidget.setCurrentIndex(2)
        # self.initData()
        face.finish()
        self.setWindowTitle('考勤信息')

        
        data = db.loadDataBase(2)[4]
        # print(data)
        row = len(data)
        # 根据数据量而设置行数
        self.ui.tableWidget.setRowCount(row)

        # 设置表格头的伸缩模式，也就是让表格铺满整个QTableWidget控件
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 将表格变为禁止编辑。默认情况下表格中的字符串是可以更改的
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格整行选中。表格默认选中的是单个单元格
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 设置表格标题字体加粗
        font = self.ui.tableWidget.horizontalHeader().font()
        font.setBold(True)
        self.ui.tableWidget.horizontalHeader().setFont(font)

        # 指定列宽度
        # self.ui.tableWidget.horizontalHeader().resizeSection(2,150)
        x = 0
        for i in data:
            y = 0
            for j in i:
                self.ui.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))
                y = y + 1
            x = x + 1
        # self.initData()
        self.ui.stackedWidget.setCurrentIndex(2)

    def status_text(self):
        # 成功签到 重复签到 迟到 识别失败/未注册  请对准摄像头 加载中... 人脸数据已存在
        if self.perform == 'repeat' or self.perform == 'success':
        # if self.perform == 'success':
            self.ui.label_6.setText('您已成功打卡')
            # self.timer.timeout.connect(self.ui.label_6.setText('您已成功打卡'))
        elif self.perform == 'late':
            self.ui.label_6.setText('您已迟到')
            # self.timer.timeout.connect(self.ui.label_6.setText('您已迟到'))
        elif self.perform == 'fail':
            self.ui.label_6.setText('识别失败/未注册')
            # self.timer.timeout.connect(self.ui.label_6.setText('识别失败/未注册'))
        elif self.perform == 'existed':   #这里
            self.ui.label_6.setText('人脸数据已存在')
            # self.timer.timeout.connect(self.ui.label_6.setText('人脸数据已存在'))
        elif self.perform == 'abnormal':
            self.ui.label_6.setText('人脸加载异常')
            # self.timer.timeout.connect(self.ui.label_6.setText('人脸加载异常'))
        elif self.perform == 'loading':
            self.ui.label_6.setText('人脸数据加载中')
            # self.timer.timeout.connect(self.ui.label_6.setText('人脸数据加载中'))
        elif self.perform == 'res_succ':
            self.ui.label_6.setText('注册成功')
            # self.timer.timeout.connect(self.ui.label_6.setText('注册成功'))
        elif self.perform == 'nothing':
            self.ui.label_6.setText('请对准摄像头')
            # self.timer.timeout.connect(self.ui.label_6.setText('请对准摄像头'))
        # elif self.perform == 'repeat':
        #     self.ui.label_6.setText('您已成功打卡')
            # self.timer.timeout.connect(self.ui.label_6.setText('您已重复签到'))
        # self.timer.timeout.connect(self.showtime)
        self.timer.start(1000) # 启动计时器 1秒刷新1次




        # x = 0
        # for i in data:
        #     print(i)
        #     y = 0
        #     for j in i:
        #         print(j)
        #         self.ui.tableWidget.setItem(i, y, QtWidgets.QTableWidgetItem(str(data[x][y])))
        #         y += 1
        #     x += 1
    # def home_page(self):
    #     self.initData()
    #     self.ui.stackedWidget.setCurrentIndex(0)



if __name__ == '__main__':
    


    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('icon/win_icon.gif'))
    mainw = MainWindow()
    mainw.setWindowTitle('每日打卡')
    # 禁止最大化按钮（只显示最小化按钮和关闭按钮）
    mainw.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    # 禁止拉伸窗口大小
    mainw.setFixedSize(mainw.width(), mainw.height())
    # mainw.ui.mainmenuButton.clicked.connect(exit(0))
    # styles.light(app)
    mainw.show()
    app.exec_()
    # sys.exit(app.exec_())



        # app = QApplication(sys.argv)
        # m_login = Ui_Form()
        # login_window = QWidget()
        # m_login.setupUi(login_window)
        # login_window.show()
        # sys.exit(app.exec_())