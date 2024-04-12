# Kodun calismasi icin internet baglantisi gereklli
# Program pariteleri bir web sitesinden arakliyor

from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # doviz ceviricinin boyutunun kucuk kalmasi daha guzel olur diye dusundum
        # bu nedenle pencere boyutunu sabit hale getirdim. Windowsta gorece daha
        # guzel duruyor mac icin ne olur bilmiyorum
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(250, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Asagi kaydirmali iki tane liste olusturup on ikiser tane alan ayirdim
        # Bu alanlara sonradan para birimleri gelecek
        self.comboBox = QtWidgets.QComboBox(self.centralwidget) # Bu ilk liste
        self.comboBox.setGeometry(QtCore.QRect(110, 100, 101, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget) # Bu da ikinci liste
        self.comboBox_2.setGeometry(QtCore.QRect(110, 180, 101, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        # Para tutarinin yazilacagi kutuyu olusturdum
        # Maks yazilabilecek degeri 99,99 yerine asagidaki degere ayarladim
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(110, 40, 80, 22))
        self.doubleSpinBox.setMaximum(1000000000.0) # Maks deger bu
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        # Az once olusturdugum butun bilesenlerin basına etiketler ekledim
        # Ileride bu etiketlere hangi bilesenin ne ise yaradigini yazacagim
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 41, 21))
        self.label.setObjectName("label") # Bu etikette "Amount" yazacak

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 47, 21))
        self.label_2.setObjectName("label_2") # Bu etikette "From" yazacak

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 193, 47, 20))
        self.label_3.setObjectName("label_3") # Bu etikette "To" yazacak

        # Basildiginda girilen degerlere gore web sitesinden degisim oranini getirecek
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 260, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.convert)

        # Bu etiket de butona basildiginda gelen degisim oranini uygulamada gosterecek
        # Acilir pencere olarak gostermek sacma olur diye dusundum o yuzden sade etiket kullandim
        # Sonucta tek seferde on hesap yapsam dokuz kere pencere kapatmam gerekir
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 350, 151, 41))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        # Bu fonksiyon sadece bilesenlerin yazilarini ayarliyor
        # Burada cagirarak UI kurulumunu tamamliyorum
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Exchange App"))
        self.comboBox.setItemText(0, _translate("MainWindow", "USD"))
        self.comboBox.setItemText(1, _translate("MainWindow", "TRY"))
        self.comboBox.setItemText(2, _translate("MainWindow", "EUR"))
        self.comboBox.setItemText(3, _translate("MainWindow", "GBP"))
        self.comboBox.setItemText(4, _translate("MainWindow", "INR"))
        self.comboBox.setItemText(5, _translate("MainWindow", "AUD"))
        self.comboBox.setItemText(6, _translate("MainWindow", "CAD"))
        self.comboBox.setItemText(7, _translate("MainWindow", "SGD"))
        self.comboBox.setItemText(8, _translate("MainWindow", "CHF"))
        self.comboBox.setItemText(9, _translate("MainWindow", "JPY"))
        self.comboBox.setItemText(10, _translate("MainWindow", "CNY"))
        self.comboBox.setItemText(11, _translate("MainWindow", "MYR"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "USD"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "TRY"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "EUR"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "GBP"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "INR"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "AUD"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "CAD"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "SGD"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "CHF"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "JPY"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "CNY"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "MYR"))
        self.label.setText(_translate("MainWindow", "Amount"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))


    # Bu da web ayrıklama fonksiyonum
    def convert(self):
        # Asagi cekmeli listelerden secilen para birimlerini
        # Sayi kutusundan da miktari alip degiskenlere atadım
        currencyFrom = self.comboBox.currentText()
        currencyTo = self.comboBox_2.currentText()
        amount = int(self.doubleSpinBox.value())

        # Site bu degiskenleri arama parametresi olarak url'de bu sekilde kullandigi icin formatlamayi boyle yaptim
        url = f"https://www.x-rates.com/calculator/?from={currencyFrom}&to={currencyTo}&amount={amount}"

        # Sayfada icin GET sorgusu olusturup butun icerigi BeautifulSoup kullanarak html belgesine donusturdum
        page = requests.get(url).text
        htmlDocument = BeautifulSoup(page, "html.parser")

        # Sonucu gosteren HTML siniflarinin icerisindeki yazilari bir degiskene atadım
        price = htmlDocument.find(class_="ccOutputTxt").text + " " + htmlDocument.find(class_="ccOutputRslt").text

        # En alttaki etiketin yazisini price degiskeni olarak etiketin boyutunu guncelledim
        self.label_4.setText(price)
        self.label_4.adjustSize()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
