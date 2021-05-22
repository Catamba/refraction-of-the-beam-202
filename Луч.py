import sys


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
import math


SCREEN_SIZE = [1200, 530]
SCREEN_SIZE2 = [500, 500]



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 120, *SCREEN_SIZE)
        self.setWindowTitle('Преломление луча')
        # # рисование 1000, 600
        # fon1_color = 'green'
        # width = 500
        # height = 500
        # draw = ImageDraw.Draw(im)
        # draw.polygon(((0, 0), (500, 0), (500, 250), (0, 250),), fon1_color)
        #
        # draw.line((0, 250, 500, 250), fill=('white'), width=3)
        # draw.line((250, 0, 250, 500), fill=('white'), width=3)
        ###################################################################################
        new_image = Image.new("RGB", (500, 500), ('green'))  # размер холста
        self.orig_image = new_image
        self.curr_image = new_image
        self.degree = 0

        draw = ImageDraw.Draw(self.curr_image)

        self.dd = 0
        if self.dd:
            draw.line((0, 0, 250, 250), fill=('red'), width=3)



        draw.line((0, 250, 500, 250), fill=('white'), width=3)
        draw.line((250, 0, 250, 500), fill=('white'), width=3)


        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)

        self.image = QLabel(self)
        self.image.move(15, 15)
        self.image.resize(500, 500)   # ограничение отображаемого размера
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)


        ###################################################################################

        # текс кнопки начать
        self.label_vivod = QLabel(self)
        self.label_vivod.setText("Нажмите кнопку (                            ) что бы программа отрисовала отражение луча")
        self.label_vivod.move(520, 180)

        self.label_a = QLabel(self)
        self.label_a.setText("a")
        self.label_a.move(45, 250)
        self.label_a1 = QLabel(self)
        self.label_a1.setText("a1")
        self.label_a1.move(250, 45)

        self.label_b = QLabel(self)
        self.label_b.setText("b")
        self.label_b.move(465, 270)
        self.label_b1 = QLabel(self)
        self.label_b1.setText("b1")
        self.label_b1.move(275, 460)

        # sreda
        self.label_sreda0 = QLabel(self)
        self.label_sreda0.setText("Задайте оптические плотности сред (p > 1)")
        self.label_sreda0.move(520, 20)

        # sreda1
        self.label_sreda1 = QLabel(self)
        self.label_sreda1.setText("Оптическая плотность первой среды (p1) ->")
        self.label_sreda1.move(520, 50)
        self.name_input_sreda1 = QLineEdit(self)
        self.name_input_sreda1.move(750, 50)

        #sreda2
        self.label_sreda2 = QLabel(self)
        self.label_sreda2.setText("Оптическая плотность второй среды (p2) ->")
        self.label_sreda2.move(520, 90)
        self.name_input_sreda2 = QLineEdit(self)
        self.name_input_sreda2.move(750, 90)

        # угол(angle)
        self.label_angle = QLabel(self)
        self.label_angle.setText("Задайте угол (X) падения луча в градусах [0;90] ->")
        self.label_angle.move(520, 130)
        self.name_input_angle = QLineEdit(self)
        self.name_input_angle.move(790, 130)

        # надписи
        self.label_angle0 = QLabel(self)
        self.label_angle0.setText("0")
        self.label_angle0.move(5, 260)
        self.label_angle45 = QLabel(self)
        self.label_angle45.setText("45")
        self.label_angle45.move(3, 5)
        self.label_angle90 = QLabel(self)
        self.label_angle90.setText("90")
        self.label_angle90.move(260, 3)


        self.label_a = QLabel(self)
        self.label_a.setText('                                                                                      ')
        self.label_a.move(520, 260)
        self.label_a1 = QLabel(self)
        self.label_a1.setText("                                                                                     ")
        self.label_a1.move(520, 290)
        self.label_b = QLabel(self)
        self.label_b.setText("                                                                                      ")
        self.label_b.move(520, 320)
        self.label_b1 = QLabel(self)
        self.label_b1.setText("                                                                                     ")
        self.label_b1.move(520, 350)

        self.label_aa = QLabel(self)
        self.label_aa.setText('                                                                                ')
        self.label_aa.move(790, 265)
        self.label_aa1 = QLabel(self)
        self.label_aa1.setText("                                                                                ")
        self.label_aa1.move(790, 295)
        self.label_bb = QLabel(self)
        self.label_bb.setText("                                                                                ")
        self.label_bb.move(790, 325)
        self.label_bb1 = QLabel(self)
        self.label_bb1.setText("                                                                                ")
        self.label_bb1.move(790, 355)

        self.lcd_a = QLCDNumber(self)
        self.lcd_a.move(720, 260)
        self.lcd_a1 = QLCDNumber(self)
        self.lcd_a1.move(720, 290)
        self.lcd_b = QLCDNumber(self)
        self.lcd_b.move(720, 320)
        self.lcd_b1 = QLCDNumber(self)
        self.lcd_b1.move(720, 350)



        self.label_Error = QLabel(self)
        self.label_Error.setText("                                                                                ")
        self.label_Error.move(910, 90)
        self.label_Error2 = QLabel(self)
        self.label_Error2.setText("                                                                                ")
        self.label_Error2.move(1035, 90)


        # начать
        self.btn_go = QPushButton('Начать', self)
        self.btn_go.resize(self.btn_go.sizeHint())
        self.btn_go.move(615, 175)
        self.btn_go.clicked.connect(self.Start)



    def test(self):
        a = 45
        a_prel = 90 - a
        sr1 = 1.0003
        sr2 = 6.0003
        a_rad = a_prel*math.pi/180

        cos = str(math.cos(a_rad))[0:3]
        sin = str(math.sin(a_rad))[0:3]

        cos_x1 = float(cos) * 250
        sin_y1 = float(sin) * 250

        sin11 = float(math.sin(a_rad))
        sin22 = (float(sr1) * float(sin11)) / float(sr2)
        arcsin22 = math.asin(sin22) # в радианах
        cos22 = float(math.cos(arcsin22))

        cos_y2 = float(str(math.cos(arcsin22))[0:3]) * 250
        sin_x2 = float(str(math.sin(arcsin22))[0:3]) * 250




        self.curr_image = self.orig_image.copy()
        draw = ImageDraw.Draw(self.orig_image)
        draw.line((int(cos_x1), int(sin_y1), 250, 250), fill=('red'), width=3)
        draw.line((250, 250, 250 + int(sin_x2), 250 + int(cos_y2)), fill=('red'), width=3)




        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)




    def Start(self):
        sreda1_text = self.name_input_sreda1.text()  # Получим текст из поля ввода
        sreda2_text = self.name_input_sreda2.text()  # Получим текст из поля ввода
        angle_text = self.name_input_angle.text()

        def is_number(str):
            try:
                float(str)
                return True
            except ValueError:
                return False

        if is_number(sreda1_text) and is_number(sreda2_text) and is_number(angle_text):
            sr1 = float(self.name_input_sreda1.text())
            sr2 = float(self.name_input_sreda2.text())
            a = int(self.name_input_angle.text())
            bigi = 1.0000000000000000000000000000000000000000000000000000000000000000000000000001
            if (sr1 > bigi and sr2 > bigi) and (a > 0 and a < 90):
                self.label_Error.setText(' ')
                self.label_Error2.setText(' ')
                a_prel = 90 - a

                a_rad = a_prel * math.pi / 180

                cos = str(math.cos(a_rad))[0:3]
                sin = str(math.sin(a_rad))[0:3]

                cos_x1 = float(cos) * 250
                sin_y1 = float(sin) * 250

                sin11 = float(math.sin(a_rad))
                sin22 = (float(sr1) * float(sin11)) / float(sr2)
                arcsin22 = math.asin(sin22)  # в радианах
                cos22 = float(math.cos(arcsin22))
                b1 = cos22 * 180 / math.pi

                cos_y2 = float(str(math.cos(arcsin22))[0:3]) * 250
                sin_x2 = float(str(math.sin(arcsin22))[0:3]) * 250

                self.curr_image = self.orig_image.copy()
                draw = ImageDraw.Draw(self.curr_image)
                draw.line((int(cos_x1), int(sin_y1), 250, 250), fill=('red'), width=3)
                draw.line((250, 250, 250 + int(sin_x2), 250 + int(cos_y2)), fill=('red'), width=3)
                self.label_a.setText('Угол падения в первой среде =')
                self.label_a1.setText('Угол преломления в первой среде =')
                self.label_b.setText('Угол падения в первой среде =')
                self.label_b1.setText('Угол преломления во второй среде =')
                if sr1 == sr2:
                    self.lcd_a.display(a)
                    self.lcd_a1.display(a_prel)
                    self.lcd_b.display(a)
                    self.lcd_b1.display(a_prel)
                else:
                    self.lcd_a.display(a)
                    self.lcd_a1.display(a_prel)
                    self.lcd_b.display(b1)
                    self.lcd_b1.display(90 - b1)

                self.label_aa.setText('градусов')
                self.label_aa1.setText('градусов')
                self.label_bb.setText('градусов')
                self.label_bb1.setText('градусов')

                self.curr_image = self.curr_image.rotate(self.degree, expand=True)
                # python 3.8 garbage collection issue
                self.a = ImageQt(self.curr_image)
                self.pixmap = QPixmap.fromImage(self.a)
                self.image.setPixmap(self.pixmap)

            else:
                self.label_Error.setText('Вы ввели недопустимое')
                self.label_Error2.setText('значение!!!!!!')
        else:
            self.label_Error.setText('Вы ввели недопустимое')
            self.label_Error2.setText('значение!!!!!!')














if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())