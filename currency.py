from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.sip import transferback
from PyQt5.QtCore import QDate
import requests
from curplot import dataClass, draw
#from datetime import date


def tarama(list, str):
    a = 0
    for i in list:
        if i == str:
            return True, a
        a += 1
    return False


def exchanceInator(base: str, date: QDate):
    day = date.day()
    month = date.month()
    year = date.year()
    str_date = f"{year}-{month}-{day}"

    print(str_date)
    response = requests.get("https://freecurrencyapi.net/api/v1/rates", {
        "base_currency": base,
        "date_from": str_date,
        "date_to": str_date,
        "apikey": "Your api key"
    })

    return response
def graphInator(base: str, date_from: QDate,date_to:QDate):
    day = date_from.day()
    month = date_from.month()
    year = date_from.year() 

    day1 = date_to.day()
    month1 = date_to.month()
    year1 = date_to.year() 

    str_date_from = f"{year}-{month}-{day}"
    str_date_to = f"{year1}-{month1}-{day1}"

    response = requests.get("https://freecurrencyapi.net/api/v1/rates", {
        "base_currency": base,
        "date_from": str_date_from,
        "date_to": str_date_to,
        "apikey": "Your api key"
    })

    return response


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.SellectedStr = []
        self.responseList = []
        #today = date.today()
        self.Qtoday = QDate.currentDate()  # QDate(today.year, today.month, today.day)
        self.QminDate= QDate(2012, 1, 2)
        self.BASE = False
        self.base = "USD"
        self.baseTo = True

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 406)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.sellectedLabel = QtWidgets.QLabel(self.centralwidget)
        self.sellectedLabel.setGeometry(QtCore.QRect(200, 90, 71, 16))
        self.sellectedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sellectedLabel.setObjectName("sellectedLabel")

        self.sellectionsLabel = QtWidgets.QLabel(self.centralwidget)
        self.sellectionsLabel.setGeometry(QtCore.QRect(40, 90, 71, 16))
        self.sellectionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sellectionsLabel.setObjectName("sellectionsLabel")

        self.ExchangeLabel = QtWidgets.QLabel(self.centralwidget)
        self.ExchangeLabel.setGeometry(QtCore.QRect(422, 90, 101, 20))
        self.ExchangeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ExchangeLabel.setObjectName("ExchangeLabel")

        self.sellectionsList = QtWidgets.QListWidget(self.centralwidget)
        self.sellectionsList.setGeometry(QtCore.QRect(10, 111, 131, 221))
        self.sellectionsList.setToolTipDuration(-1)
        self.sellectionsList.setObjectName("sellectionsList")
        # currencies
        # list insert
        self.sellectionsList.insertItem(0, "USD USA Dollar")
        self.sellectionsList.insertItem(1, "JPY Japan Yen")
        self.sellectionsList.insertItem(2, "BGN bulgaria lev")
        self.sellectionsList.insertItem(3, "CZK Czech Koruna")
        self.sellectionsList.insertItem(4, "DKK Denmark Krone")
        self.sellectionsList.insertItem(5, "GBP Great Britain Pound")
        self.sellectionsList.insertItem(6, "HUF Hungary Forint")
        self.sellectionsList.insertItem(7, "PLN Poland Zloty")
        self.sellectionsList.insertItem(8, "RON Romania New Lei")
        self.sellectionsList.insertItem(9, "TRY Turkish New Lira")
        self.sellectionsList.insertItem(10, "AUD Australia Dollar")
        self.sellectionsList.insertItem(11, "BRL Brazil Real")
        self.sellectionsList.insertItem(12, "CAD Canada Dollar")
        self.sellectionsList.insertItem(13, "CNY China Yuan/Renminbi")
        self.sellectionsList.insertItem(14, "HKD Hong Kong Dollar")
        self.sellectionsList.insertItem(15, "IDR Indonesia Rupiah")
        self.sellectionsList.insertItem(16, "ILS srael New Shekel ")
        self.sellectionsList.insertItem(17, "INR India Rupee")
        self.sellectionsList.insertItem(18, "KRW South Korea Won")
        self.sellectionsList.insertItem(19, "MXN Mexico Peso")
        self.sellectionsList.insertItem(20, "MYR Malaysia Ringgit")
        self.sellectionsList.insertItem(21, "NZD New Zealand Dollar")
        self.sellectionsList.insertItem(22, "PHP Philippines Peso")
        self.sellectionsList.insertItem(23, "SGD Singapore Dollar")
        self.sellectionsList.insertItem(24, "THB Thailand Baht")
        self.sellectionsList.insertItem(25, "ZAR South Africa Rand")
        self.sellectionsList.insertItem(26, "EUR Euro")

        self.sellectedList = QtWidgets.QListWidget(self.centralwidget)
        self.sellectedList.setGeometry(QtCore.QRect(170, 110, 131, 221))
        self.sellectedList.setObjectName("sellectedList")

        self.sellectedList.clicked.connect(self.sellected)
        self.sellectionsList.clicked.connect(self.sellection)

        self.exchangelist = QtWidgets.QListWidget(self.centralwidget)
        self.exchangelist.setGeometry(QtCore.QRect(340, 110, 261, 221))
        self.exchangelist.setObjectName("exchangelist")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(140, 20, 311, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.TophorizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.TophorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.TophorizontalLayout.setObjectName("TophorizontalLayout")
        # top layout
        self.otherToButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.otherToButton.setObjectName("otherToButton")
        self.TophorizontalLayout.addWidget(self.otherToButton)
        self.BaseToButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.BaseToButton.setObjectName("BaseToButton")
        self.TophorizontalLayout.addWidget(self.BaseToButton)
        # baseto other other to base connect
        self.otherToButton.clicked.connect(self.otherTo)
        self.BaseToButton.clicked.connect(self.BaseTo)

        self.BaseCurLabel = QtWidgets.QLabel(self.centralwidget)
        self.BaseCurLabel.setGeometry(QtCore.QRect(40, 20, 61, 31))
        self.BaseCurLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.BaseCurLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BaseCurLabel.setObjectName("BaseCurLabel")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 0, 41, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.sellectButton = QtWidgets.QPushButton(self.centralwidget)
        self.sellectButton.setGeometry(QtCore.QRect(20, 60, 99, 23))
        self.sellectButton.setObjectName("sellectButton")
        self.sellectButton.clicked.connect(self.basesellect)
        # date edit
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(470, 30, 110, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(self.Qtoday)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 10, 57, 15))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(170, 340, 251, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.bottomHorizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.bottomHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomHorizontalLayout.setObjectName("bottomHorizontalLayout")
        self.showGraphButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.showGraphButton.setObjectName("showGraphButton")
        self.bottomHorizontalLayout.addWidget(self.showGraphButton)
        self.getRatesButton = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        self.getRatesButton.setObjectName("getRatesButton")
        # get rates button
        self.getRatesButton.clicked.connect(self.lister)
        self.bottomHorizontalLayout.addWidget(self.getRatesButton)
        #graph button
        self.showGraphButton.clicked.connect(self.showGraph)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 609, 20))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "currency graph"))

        self.sellectedLabel.setText(_translate("MainWindow", "sellected"))
        self.sellectionsLabel.setText(_translate("MainWindow", "Sellections"))
        self.ExchangeLabel.setText(_translate("MainWindow", "exchange rates"))

        self.sellectionsList.setToolTip(_translate(
            "MainWindow", "click on list items to sellect currencies"))
        self.sellectedList.setToolTip(_translate(
            "MainWindow", "click on sellected currencies to remove them"))
        self.exchangelist.setToolTip(_translate(
            "MainWindow", "click on exchange rates to open graphs"))

        self.otherToButton.setToolTip(_translate(
            "MainWindow", "callculate exchange rates others to base"))
        self.otherToButton.setText(_translate("MainWindow", "other to base"))

        self.BaseToButton.setToolTip(_translate(
            "MainWindow", "callculate exchange rates base to others"))
        self.BaseToButton.setText(_translate("MainWindow", "Base to other"))

        self.BaseCurLabel.setToolTip(_translate("MainWindow", "Base currency"))
        self.BaseCurLabel.setText(_translate("MainWindow", "USD"))

        self.label_4.setText(_translate("MainWindow", "BASE"))

        self.sellectButton.setToolTip(_translate(
            "MainWindow", "sellect base currency after pushing the button"))
        self.sellectButton.setText(_translate("MainWindow", "sellect base"))

        self.dateEdit.setToolTip(_translate(
            "MainWindow", "date exchange rates are based on"))
        self.label.setText(_translate("MainWindow", "Date"))

        self.showGraphButton.setToolTip(_translate(
            "MainWindow", "click on to show a graph with all chosed currencies"))
        self.showGraphButton.setText(_translate("MainWindow", "Show Graph"))

        self.getRatesButton.setToolTip(_translate(
            "MainWindow", "clickto get exchange rates based on the date"))
        self.getRatesButton.setText(_translate("MainWindow", "get rates"))

    def sellection(self):
        item = self.sellectionsList.currentItem()
        if not self.BASE and self.base != item.text()[0:3]:
            if not tarama(self.SellectedStr, item.text()):
                self.sellectedList.insertItem(0, item.text())
                self.SellectedStr.append(item.text())
                # print(self.SellectedStr)
                # print(self.sellectedList.count())
        else:
            self.BaseCurLabel.setText(item.text()[0:3])
            self.BASE = False
            self.base = item.text()[0:3]

            for i in self.SellectedStr:
                if i[0:3] == self.base:
                    for x in range(self.sellectedList.count()-1):
                        if self.sellectedList.item(x).text()[0:3] == self.base:
                            self.sellectedList.takeItem(x)
                    self.SellectedStr.remove(i)
                    # print(str(i)+" blyat")

    def sellected(self):
        item = self.sellectedList.currentItem()
        itemRow = self.sellectedList.currentRow()
        self.SellectedStr.remove(item.text())
        self.sellectedList.takeItem(itemRow)

    def basesellect(self):
        self.BASE = True

    def BaseTo(self):
        self.baseTo = True

    def otherTo(self):
        self.baseTo = False

    def clearList(self, qlist):
        count = qlist.count()
        if count == 0:  # return
            return
        for i in range(count):
            qlist.takeItem(0)
    
    def showGraph(self):
        qdate = self.dateEdit.date()
        curs=[]
        for i in self.SellectedStr:
            curs.append(i[0:3])

        if qdate.__le__(self.Qtoday) and qdate.__ge__(self.QminDate):
            response = graphInator(self.base, qdate, self.Qtoday)
            
        else:
            response = graphInator(self.base, self.Qtoday)
        data = dataClass(response)
        draw(data, curs)



    def lister(self):
        qdate = self.dateEdit.date()
        if qdate.__le__(self.Qtoday) and qdate.__ge__(self.QminDate):
            response = exchanceInator(self.base, qdate)
            
        else:
            response = exchanceInator(self.base, self.Qtoday)

        json = response.json()

        date = list(json["data"].keys())

        keys = json["data"][date[0]]
        self.clearList(self.exchangelist)
        for key in keys:
            for x in self.SellectedStr:
                if x[0:3] == key and self.baseTo:
                    self.exchangelist.insertItem(
                        0, f"{self.base} ->{key} : {keys[key]}")
                    print(f"{self.base} ->{key} : {keys[key]} skrrt")
                elif x[0:3] == key:
                    self.exchangelist.insertItem(
                        0, f"{self.base} ->{key} : {1/keys[key]}")
                    #print(f"{self.base} ->{key} : {1/keys[key]}YES")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
