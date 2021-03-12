# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 23:01:45 2021

@author:Deepak
"""

import sys

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QIntValidator, QFont, QPixmap, QPalette, QLinearGradient, QColor, QBrush, QMovie, QPainter
from PyQt5.QtCore import Qt, QLine

import model
my_dic={}
output = 10

def output_reverse(output):
    if output == 0:
        return(4)
    elif output == 1:
        return(12)
    else:
        return(19)

class Performance(QWidget):

    def __init__(self) -> None :
        super(Performance, self).__init__()
        
        self.title = "Student Performance Prediction"
        self.sub_head = QLabel("Student's Detail")
        self.sub_head.setFont(QFont("Times",24, weight=QFont.Bold))
        self.label = QLabel(self)
        """"pixmap = QPixmap('std.jpg')
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(),pixmap.height())
        self.label.setGeometry(700,50,1600,1066)"""
        
        
        self.movie = QMovie("wow.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.setGeometry(700,500,255,276)
        self.movie.start()
                
        self.l1 = QLineEdit()
        self.l2 = QLineEdit()
        self.l3 = QLineEdit()
        self.l4 = QLineEdit()
        self.l5 = QLineEdit()
        self.l6 = QLineEdit()
        self.l7 = QLineEdit()
        self.l8 = QLineEdit()
        self.l9 = QLineEdit()
        self.l10 = QLineEdit()
        self.l11 = QLineEdit()
        self.l12 = QLineEdit()
        self.l13 = QLineEdit()
        self.l14 = QLineEdit()
        self.l15 = QLineEdit()
        self.l16 = QLineEdit()
        self.l17 = QLineEdit()
        self.l18 = QLineEdit()
        
        self.t1 = QLabel("Enter Student Age:                     ")
        self.t2 = QLabel("Enter Mother's Education:              ")
        self.t3 = QLabel("Enter Father's Education:              ")
        self.t4 = QLabel("Enter Travel Time:                     ")
        self.t5 = QLabel("Enter Student no. of Failure:          ")
        self.t6 = QLabel("Enter School Support:                  ")
        self.t7 = QLabel("Enter Family Support:                  ")
        self.t8 = QLabel("Enter Paid:                            ")
        self.t9 = QLabel("Enter Activity Enrollment:             ")
        self.t10 = QLabel("Enter Internet Access:                ")
        self.t11 = QLabel("Enter Free Time:                      ")
        self.t12 = QLabel("Enter level of going out:             ")
        self.t13 = QLabel("Consumption of daily alcohol?:        ")
        self.t14 = QLabel("Consumption of weekly alcohol?:       ")
        self.t15 = QLabel("Current health status?:               ")
        self.t16 = QLabel("Absent level?:                        ")
        self.t17 = QLabel("Enter First Assesment Grade:          ")
        self.t18 = QLabel("Enter Second Assesment Grade:         ")
       
        
        self.r1 = QLabel("(15-25)")
        self.r2 = QLabel("(0-4)")
        self.r3 = QLabel("(0-4)")
        self.r4 = QLabel("(1-4)")
        self.r5 = QLabel("(1-4)")
        self.r6 = QLabel("(0[NO] or 1[YES])")
        self.r7 = QLabel("(0[NO] or 1[YES])")
        self.r8 = QLabel("(0[NO] or 1[YES])")
        self.r9 = QLabel("(0[NO] or 1[YES])")
        self.r10 = QLabel("(0[NO] or 1[YES])")
        self.r11 = QLabel("(0-5)")
        self.r12 = QLabel("(0-5)")
        self.r13= QLabel("(0-5)")
        self.r14 = QLabel("(0-5)")
        self.r15 = QLabel("(0-5)")
        self.r16 = QLabel("(0-93)")
        self.r17 = QLabel("(0-20)")
        self.r18 = QLabel("(0-20)")
        
        self.h1 = QHBoxLayout()
        self.h0 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.h3 = QHBoxLayout()
        self.h4 = QHBoxLayout()
        self.h5 = QHBoxLayout()
        self.h6 = QHBoxLayout()
        self.h7 = QHBoxLayout()
        self.h8 = QHBoxLayout()
        self.h9 = QHBoxLayout()
        self.h10 = QHBoxLayout()
        self.h11 = QHBoxLayout()
        self.h12 = QHBoxLayout()
        self.h13 = QHBoxLayout()
        self.h14 = QHBoxLayout()
        self.h15 = QHBoxLayout()
        self.h16 = QHBoxLayout()
        self.h17 = QHBoxLayout()
        self.h18 = QHBoxLayout()
        
        self.clbtn = QPushButton("CLEAR")
        self.clbtn.setFixedWidth(100)
        self.submit = QPushButton("SUBMIT")
        self.submit.setFixedWidth(100)
        self.graph = QPushButton("SHOW GRAPH")
        self.graph.setFixedWidth(100)
        self.v1_box = QVBoxLayout()
        self.v2_box = QVBoxLayout()
        self.v3_box = QVBoxLayout()
        self.final_hbox = QHBoxLayout()
        self.initui()

        
        
    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)
            
            
    def initui(self) -> None:
        """ The gui is created and widgets elements are set here """
        
        rangeVal = QIntValidator(self)
        rangeVal.setRange(0,1)
        rangeVal1 = QIntValidator(self)
        rangeVal1.setRange(15,25)
        rangeVal2 = QIntValidator(self)
        rangeVal2.setRange(1,5)
        rangeVal3 = QIntValidator(self)
        rangeVal3.setRange(0,4)
        rangeVal4 = QIntValidator(self)
        rangeVal4.setRange(1,4)
        rangeVal5 = QIntValidator(self)
        rangeVal5.setRange(0,93)
        rangeVal6 = QIntValidator(self)
        rangeVal6.setRange(1,20)
        
               
        
        
        self.v1_box.addWidget(self.sub_head)
        self.v1_box.addSpacing(10)
        self.v1_box.setSpacing(5)
        self.l1.setValidator(rangeVal1)
        self.l2.setValidator(rangeVal3)
        self.l3.setValidator(rangeVal3)
        self.l4.setValidator(rangeVal4)
        self.l5.setValidator(rangeVal4)
        self.l6.setValidator(rangeVal)
        self.l7.setValidator(rangeVal)
        self.l8.setValidator(rangeVal)
        self.l9.setValidator(rangeVal)
        self.l10.setValidator(rangeVal)
        self.l11.setValidator(rangeVal2)
        self.l12.setValidator(rangeVal2)
        self.l13.setValidator(rangeVal2)
        self.l14.setValidator(rangeVal2)
        self.l15.setValidator(rangeVal2)
        self.l16.setValidator(rangeVal5)
        self.l17.setValidator(rangeVal6)
        self.l18.setValidator(rangeVal6)
        
        
        
        
        self.l1.setFixedSize(40,30)
        self.l2.setFixedSize(40,30)
        self.l3.setFixedSize(40,30)
        self.l4.setFixedSize(40,30)
        self.l5.setFixedSize(40,30)
        self.l6.setFixedSize(40,30)
        self.l7.setFixedSize(40,30)
        self.l8.setFixedSize(40,30)
        self.l9.setFixedSize(40,30)
        self.l10.setFixedSize(40,30)
        self.l11.setFixedSize(40,30)
        self.l12.setFixedSize(40,30)
        self.l13.setFixedSize(40,30)
        self.l14.setFixedSize(40,30)
        self.l15.setFixedSize(40,30)
        self.l16.setFixedSize(40,30)
        self.l17.setFixedSize(40,30)
        self.l18.setFixedSize(40,30)
        
        
        
        self.h1.addWidget(self.t1)
        self.h1.addWidget(self.l1)
        self.h1.addWidget(self.r1)        
        self.v1_box.addLayout(self.h1)
        
        self.h2.addWidget(self.t2)
        self.h2.addWidget(self.l2)
        self.h2.addWidget(self.r2)       
        self.v1_box.addLayout(self.h2)
        
        self.h3.addWidget(self.t3)
        self.h3.addWidget(self.l3)
        self.h3.addWidget(self.r3)       
        self.v1_box.addLayout(self.h3)
        
        self.h4.addWidget(self.t4)
        self.h4.addWidget(self.l4)
        self.h4.addWidget(self.r4)      
        self.v1_box.addLayout(self.h4)
        
        self.h5.addWidget(self.t5)
        self.h5.addWidget(self.l5)
        self.h5.addWidget(self.r5)      
        self.v1_box.addLayout(self.h5)
        
        self.h6.addWidget(self.t6)
        self.h6.addWidget(self.l6)
        self.h6.addWidget(self.r6)      
        self.v1_box.addLayout(self.h6)
        
        self.h7.addWidget(self.t7)
        self.h7.addWidget(self.l7)
        self.h7.addWidget(self.r7)      
        self.v1_box.addLayout(self.h7)
        
        self.h8.addWidget(self.t8)
        self.h8.addWidget(self.l8)
        self.h8.addWidget(self.r8)      
        self.v1_box.addLayout(self.h8)
        
        self.h9.addWidget(self.t9)
        self.h9.addWidget(self.l9)
        self.h9.addWidget(self.r9)      
        self.v1_box.addLayout(self.h9)
        
        self.h10.addWidget(self.t10)
        self.h10.addWidget(self.l10)
        self.h10.addWidget(self.r10)      
        self.v1_box.addLayout(self.h10)
        
        self.h11.addWidget(self.t11)
        self.h11.addWidget(self.l11)
        self.h11.addWidget(self.r11)      
        self.v1_box.addLayout(self.h11)
        
        self.h12.addWidget(self.t12)
        self.h12.addWidget(self.l12)
        self.h12.addWidget(self.r12)      
        self.v1_box.addLayout(self.h12)
        
        self.h13.addWidget(self.t13)
        self.h13.addWidget(self.l13)
        self.h13.addWidget(self.r13)      
        self.v1_box.addLayout(self.h13)
        
        self.h14.addWidget(self.t14)
        self.h14.addWidget(self.l14)
        self.h14.addWidget(self.r14)      
        self.v1_box.addLayout(self.h14)
        
        self.h15.addWidget(self.t15)
        self.h15.addWidget(self.l15)
        self.h15.addWidget(self.r15)      
        self.v1_box.addLayout(self.h15)
        
        self.h16.addWidget(self.t16)
        self.h16.addWidget(self.l16)
        self.h16.addWidget(self.r16)      
        self.v1_box.addLayout(self.h16)
        
        self.h17.addWidget(self.t17)
        self.h17.addWidget(self.l17)
        self.h17.addWidget(self.r17)      
        self.v1_box.addLayout(self.h17)
        
        self.h18.addWidget(self.t18)
        self.h18.addWidget(self.l18)
        self.h18.addWidget(self.r18)      
        self.v1_box.addLayout(self.h18)
        
    
        self.h6 = QHBoxLayout()
        self.submit.clicked.connect(lambda: self.test_input())
        self.submit.setToolTip("Click to check the performance of Student")
        self.clbtn.clicked.connect(lambda: self.clfn())
        self.graph.clicked.connect(lambda: self.getgraph())
        self.h6.addWidget(self.submit)
        self.h6.addWidget(self.clbtn)
        self.h6.addWidget(self.graph)
        self.v1_box.addLayout(self.h6)
        self.report_ui()
        self.final_hbox.addLayout(self.v1_box)
        self.final_hbox.addSpacing(70)
        self.final_hbox.addLayout(self.v2_box)
        self.final_hbox.addSpacing(70)
        self.final_hbox.addLayout(self.v3_box)
        self.setLayout(self.final_hbox)

    def report_ui(self):
        self.v2_box.setSpacing(6)
        self.report_subhead = QLabel("About")
        self.report_subhead.setAlignment(Qt.AlignCenter)
        self.report_subhead.setFont(QFont("Times",24, weight=QFont.Bold))
        self.v2_box.addWidget(self.report_subhead)
        self.details = QLabel("This model uses Naive Bayes classifier.\nWe have used student dataset from UCI archive.")
        self.details.setFont(QFont("Arial",14, weight=QFont.Bold))
        self.details.setAlignment(Qt.AlignLeft)
        self.details.setWordWrap(True)
        self.model_details = QLabel("Fill details and press submit to see details. \n\n\n0 being the lowest and increasing")
        self.model_details.setWordWrap(True)
        self.v2_box.addWidget(self.details)
        self.results = QLabel(" ")
        self.results.setWordWrap(True)
        self.v2_box.addWidget(self.results)
        self.v2_box.addWidget(self.model_details)
        
        

    def clfn(self):
        """ clear all the text fields via clear button"""
        self.l1.clear()
        self.l2.clear()
        self.l3.clear()
        self.l3.clear()
        self.l4.clear()
        self.l5.clear()
        self.l6.clear()
        self.l7.clear()
        self.l8.clear()
        self.l9.clear()
        self.l10.clear()
        self.l11.clear()
        self.l12.clear()
        self.l13.clear()
        self.l14.clear()
        self.l15.clear()
        self.l16.clear()
        self.l17.clear()
        self.l18.clear()
        
        self.report_subhead.setText("About")
        self.model_details.setText("Fill details and press submit to see details.\n\n\n0 being the lowest and increasing")
        self.results.setText(" ")
        self.details.setText("This model uses Naive Bayes Algorithm.\nWe have used student dataset from UCI archive.")
    
    
    
    def test_input(self) -> None:
        global my_dic, output
        my_dic = {"age":int(self.l1.text()), "Medu":int(self.l2.text()),"Fedu":int(self.l3.text()), "traveltime":int(self.l4.text()), "failures": int(self.l5.text()),
                  "schoolsup": int(self.l6.text()),"famsup": int(self.l7.text()),"paid": int(self.l8.text()),"activities": int(self.l9.text()),"internet": int(self.l10.text()),
                  "freetime": int(self.l11.text()),"goout": int(self.l12.text()),"Dalc": int(self.l13.text()),"Walc": int(self.l14.text()),"health": int(self.l15.text()),"absences": int(self.l5.text()),
                  "G1": int(self.l17.text()),"G2": int(self.l18.text())}
        
        output = model.get_input(my_dic)
        self.report_subhead.setText("About")
        self.model_details.setText("This model uses Naive Bayes Algorithm. We have used student dataset from UCI archive.")
        if output == 0:
            self.results.setText("The model predicts that the academic performance based on the given data attributes will be POOR")
        elif output == 1:
            self.results.setText("The model predicts that the academic performance based on the given data attributes will be FAIR")
        else:
            self.results.setText("The model predicts that the academic performance based on the given data attributes will be GOOD")
        self.results.setFont(QFont("Arial",14, weight=QFont.Bold))        
  
    def getgraph(self) -> None:
        global my_dic, output
        import matplotlib.pyplot as plt
        %matplotlib qt
        print(output)
        output=output_reverse(output)
        langs = ['g1', 'g2', 'final']
        students = [my_dic['G1'],my_dic['G2'],output]
        fig = plt.figure()
        
        plt.bar(langs,students)
        plt.show()
        print(output,my_dic['G1'],my_dic['G2'])
    
    def mwindow(self) -> None:
        """ window features are set here and application is loaded into display"""
        self.setFixedSize(1200, 900)
        self.setWindowTitle("Student Performance Prediction")
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor(130, 160, 230))
        gradient.setColorAt(1.0, QColor(160, 220, 180))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        self.show()       

if __name__=="__main__":
    app = QApplication(sys.argv)
    a_window = Performance()
    a_window.mwindow()
    sys.exit(app.exec_())
    