###############################
# WtBal.py
# Started on May 26, 2019
# By: David R
###############################

print("importing system")
import sys
print("importing PyQt5")
from PyQt5 import QtCore, QtGui, QtWidgets
print("importing matplotlib")
from matplotlib import pyplot as plt
print("importing MultipleLocator")
from matplotlib.ticker import MultipleLocator
import warnings
warnings.simplefilter("ignore")

def is_in_151(arm, weight):
    line = (arm * 95) - 5935
    if (weight > 2325):
        return 'ro'
    elif (arm < 83 or arm > 93):
        return 'ro'
    elif (arm > 83 and arm < 87 and weight > line):
        return 'ro'
    return 'go'

def is_in_181(arm, weight):
    line = (arm * 200 / 3) - (10250 / 3)
    if (weight > 2550):
        return 'ro'
    elif (arm < 82 or arm > 93):
        return 'ro'
    elif (arm > 82 and arm < 88.5 and weight > line):
        return 'ro'
    return 'go'

def bin_151(arm, weight, arm2, weight2):
    ratio = 0.5
    d_x = arm2 - arm
    d_y = weight2 - weight
    for i in range(1, 21):
        if (is_in_151(arm + (d_x * ratio), weight + (d_y * ratio)) == 'go'):
            ratio = ratio + (ratio / 2**i)
        else:
            ratio = ratio - (ratio / 2**i)
    return arm + (d_x * ratio), weight + (d_y * ratio)

def bin_181(arm, weight, arm2, weight2):
    ratio = 0.5
    d_x = arm2 - arm
    d_y = weight2 - weight
    for i in range(1, 21):
        if (is_in_181(arm + (d_x * ratio), weight + (d_y * ratio)) == 'go'):
            ratio = ratio + (ratio / 2**i)
        else:
            ratio = ratio - (ratio / 2**i)
    return arm + (d_x * ratio), weight + (d_y * ratio)

def plot_151(arm, arm_no_fuel, weight, weight_no_fuel):
    if (is_in_151(arm, weight) != is_in_151(arm_no_fuel, weight_no_fuel)):
        x, y = bin_151(arm_no_fuel, weight_no_fuel, arm, weight)
        plt.plot([x,arm_no_fuel], [y,weight_no_fuel], color='g')
        plt.plot([arm,x], [weight,y], color='r')
    elif (is_in_151(arm, weight) == is_in_151(arm_no_fuel, weight_no_fuel) == 'go'):
        plt.plot([arm, arm_no_fuel], [weight,weight_no_fuel], color='g')
    else:
        plt.plot([arm, arm_no_fuel], [weight,weight_no_fuel], color='r')

    plt.plot([83,83], [1200,1950], color='k')
    plt.plot([93,93], [1200,2325], color='k')
    plt.plot([87,93], [2325,2325], color='k')
    plt.plot([83,87], [1950,2325], color='k')

    plt.plot([83,86.5], [1950,1950], linestyle='--', color='k')
    plt.plot([86.5,86.5], [1200,1950], linestyle='--', color='k')

    plt.text(88, 2350, "NORMAL CATEGORY", fontsize=10)
    plt.text(84, 1960, "UTILTY CATEGORY", fontsize=10)
    plt.text(82.5, 1600, "FRONT HEAVY", rotation=90, fontsize=10)

    plt.plot(arm, weight, is_in_151(arm, weight))
    plt.plot(arm_no_fuel, weight_no_fuel, is_in_151(arm_no_fuel, weight_no_fuel))

    plt.title("PA 28-151 N6919J")

def plot_181(arm, arm_no_fuel, weight, weight_no_fuel):
    if (is_in_181(arm, weight) != is_in_181(arm_no_fuel, weight_no_fuel)):
        x, y = bin_181(arm_no_fuel, weight_no_fuel, arm, weight)
        plt.plot([x,arm_no_fuel], [y,weight_no_fuel], color='g')
        plt.plot([arm,x], [weight,y], color='r')
    elif (is_in_181(arm, weight) == is_in_181(arm_no_fuel, weight_no_fuel) == 'go'):
        plt.plot([arm, arm_no_fuel], [weight,weight_no_fuel], color='g')
    else:
        plt.plot([arm, arm_no_fuel], [weight,weight_no_fuel], color='r')

    plt.plot([82,82], [1200,2050], color='k')
    plt.plot([93,93], [1200,2550], color='k')
    plt.plot([88.5,93], [2550,2550], color='k')
    plt.plot([82,88.5], [2050,2550], color='k')

    plt.plot([82,86.5], [1950,1950], linestyle='--', color='k')
    plt.plot([86.5,86.5], [1200,1950], linestyle='--', color='k')

    plt.text(89, 2560, "NORMAL CATEGORY", fontsize=10)
    plt.text(84, 1960, "UTILTY CATEGORY", fontsize=10)
    plt.text(81.5, 1600, "FRONT HEAVY", rotation=90, fontsize=10)

    plt.plot(arm, weight, is_in_181(arm, weight))
    plt.plot(arm_no_fuel, weight_no_fuel, is_in_181(arm_no_fuel, weight_no_fuel))

    plt.title("PA 28-181 N103AV")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 140, 71, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 140, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(100, 30, 131, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 60, 131, 17))
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 71, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 100, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText("48")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 71, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 180, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 71, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 220, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText("25")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 260, 111, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.PLOT)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weight and Balance"))
        self.label.setText(_translate("MainWindow", "Front (lbs)"))
        self.radioButton.setText(_translate("MainWindow", "PA 28-151 N6919J"))
        self.radioButton_2.setText(_translate("MainWindow", "PA 28-181 N103AV"))
        self.label_2.setText(_translate("MainWindow", "Fuel (G)"))
        self.label_3.setText(_translate("MainWindow", "Back (lbs)"))
        self.label_4.setText(_translate("MainWindow", "Baggage (lbs)"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))

    def PLOT(self):
        if (self.radioButton.isChecked() == True):
            type = '151'
            empty_weight = 1500 #PA 28-151 N6919J
            empty_moment = 129377.7
        else:
            type = '181'
            empty_weight = 1550 #PA 28-181 N103AV
            empty_moment = 140742.4

        if (self.lineEdit.text() == ''):
            self.lineEdit.setText('0')
        if (self.lineEdit_2.text() == ''):
            self.lineEdit_2.setText('0')
        if (self.lineEdit_3.text() == ''):
            self.lineEdit_3.setText('0')
        if (self.lineEdit_4.text() == ''):
            self.lineEdit_4.setText('0')

        fuel = float(self.lineEdit_2.text())
        front_weight = float(self.lineEdit.text())
        back_weight = float(self.lineEdit_3.text())
        baggage_weight = float(self.lineEdit_4.text())

        fuel_weight = fuel * 6.0

        fuel_moment = fuel_weight * 95.0
        front_moment = front_weight * 80.5
        back_moment = back_weight * 118.1
        baggage_moment = baggage_weight * 142.8

        weight = front_weight + back_weight + baggage_weight + fuel_weight + empty_weight
        weight_no_fuel =  front_weight + back_weight + baggage_weight + empty_weight

        moment = front_moment + back_moment + baggage_moment + fuel_moment + empty_moment
        moment_no_fuel = front_moment + back_moment + baggage_moment + empty_moment

        arm = moment / weight
        arm_no_fuel = moment_no_fuel / weight_no_fuel

        print("\nFULL: Arm " + str(round(arm,4)) + ", Weight " + str(round(weight,1)))
        print("EMPTY: Arm " + str(round(arm_no_fuel,4)) + ", Weight " + str(round(weight_no_fuel,1)))

        plt.clf()
        plt.axes().xaxis.set_minor_locator(MultipleLocator(1))
        plt.axes().yaxis.set_minor_locator(MultipleLocator(100))
        plt.grid(True, which='both')

        if type == '151':
            plot_151(arm, arm_no_fuel, weight, weight_no_fuel)
        if type == '181':
            plot_181(arm, arm_no_fuel, weight, weight_no_fuel)

        plt.text(92.5, 1600, "BACK HEAVY", rotation=90, fontsize=10)
        plt.ylabel("WEIGHT - IN LBS")
        plt.ylim(1200, 2800)
        plt.xlim(81, 97)

        plt.tight_layout()
        plt.show()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
