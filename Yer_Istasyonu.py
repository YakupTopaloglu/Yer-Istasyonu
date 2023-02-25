import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTabWidget, QPushButton,QWidget,QLabel,QFrame
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
from dronekit import connect, VehicleMode
import argparse

#html colour code:#042366

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Lagari")
        icon = QIcon('C:\Yedek\Masaüstü\Lagari\Yer istasyonu\Fotoğraf\Lagari.png')

        #tab için icon
        #icon2=QIcon('C:\Yedek\Masaüstü\Lagari\Yer istasyonu\Fotoğraf\ucaklar_tab_icon.png')

        self.setWindowIcon(icon)
        self.setToolTip("Lagari...")

        centralWidget = QTabWidget()
        self.setCentralWidget(centralWidget)

        #info sekmesinin tanımlanması

        info_tab = QWidget()
        info_layout = QVBoxLayout()
        info_tab.setLayout(info_layout)
        centralWidget.addTab(info_tab, "Bilgiler")
        info_tab.setStyleSheet("Background-color:#042366")

        # grafik sekmesini hem grafik olarak hem de sekme olarak tanımlanması

        self.hiz_tab = pg.PlotWidget()
        self.hiz_tab.setTitle("Hız", color="w", size="10pt")
        centralWidget.addTab(self.hiz_tab, "Hız-Zaman")

        self.altitude_tab = pg.PlotWidget()
        self.altitude_tab.setTitle("İrtifa", color="w", size="10pt")
        centralWidget.addTab(self.altitude_tab,"İrtifa-Zaman")

        self.batarya_tab=pg.PlotWidget()
        self.batarya_tab.setTitle("Batarya", color="w", size="10pt")
        centralWidget.addTab(self.batarya_tab,"Batarya-Zaman")

        #uçak ile ilgili bilinmek istenen bilgilerin hepsinin mesajının arayüze eklenmesi

        self.qLblAirspeed = QLabel('Hız: Veri Bekleniyor...')
        info_layout.addWidget(self.qLblAirspeed)
        self.qLblAirspeed.setStyleSheet("color:white")

        self.qLblAttitude = QLabel('Attitude: Veri Bekleniyor...')
        info_layout.addWidget(self.qLblAttitude)
        self.qLblAttitude.setStyleSheet("color:white")

        self.qLblLocation = QLabel('Konum: Veri Bekleniyor...')
        info_layout.addWidget(self.qLblLocation)
        self.qLblLocation.setStyleSheet("color:white")

        self.qLbLBatarya = QLabel("Batarya Durumu")
        info_layout.addWidget(self.qLbLBatarya)
        self.qLbLBatarya.setStyleSheet("color:white")

        #uçağı çalıştıracak butonun eklenmesi

        self.arm_button = QPushButton("Çalıştır")
        self.arm_button.clicked.connect(self.arm_vehicle)
        info_layout.addWidget(self.arm_button)

        #butona basıldıktan sonra renk değişimi

        self.arm_button.setStyleSheet("QPushButton {background-color : lightblue}"
                                      "QPushButton::pressed{background-color : red}")


        #Grafik oluşturulurken gelen bilgilerin bir parametrede tutulması lazım onun için boş küme olarak yazdık

        self.altitude = []
        self.batarya = []
        self.hiz = []
        self.time = []

        #Her yarım saniyede ekranda görülen parametre ve grafik durumları değişecek

        self.qTimer = QTimer()
        self.qTimer.setInterval(500)
        self.qTimer.timeout.connect(self.getSensorValue)
        self.qTimer.start()
        self.vehicle = self.connectMyPlane()

    #Mission planerdaki uçağın bağlanması

    def connectMyPlane(self):
        parser = argparse.ArgumentParser(description='commands')
        parser.add_argument('--connect', default='tcp:127.0.0.1:5762')
        args = parser.parse_args()

        connection_string = args.connect
        baud_rate = 57600

        vehicle = connect(connection_string, baud=baud_rate, wait_ready=True)
        vehicle.mode = VehicleMode("AUTO")

        #arayüzde buton olacağı için uçağı direk arm yapmamıza gerek yok istediğimiz zaman olacak
        #vehicle.armed = True
        return vehicle

    def getSensorValue(self):
        #uçağın erişilen değerlerine parametrelere eşitledik

        airspeed = self.vehicle.airspeed
        attitude = self.vehicle.attitude
        location = self.vehicle.location.global_relative_frame
        batarya_seviye = self.vehicle.battery.level
        altitude=self.vehicle.location.global_relative_frame.alt

        #grafiklere hangisi hangi değerin grafiğiyse ona append ile ekledik

        self.hiz.append(airspeed)
        self.altitude.append(altitude)
        self.batarya.append(batarya_seviye)

        self.time.append(self.qTimer.interval()*len(self.hiz))

        self.hiz_tab.clear()
        self.hiz_tab.plot(self.time, self.hiz)

        self.altitude_tab.clear()
        self.altitude_tab.plot(self.time, self.altitude)

        self.batarya_tab.clear()
        self.batarya_tab.plot(self.time,self.batarya)

        # uçaktan çekilen parametrenin her yarım saniyede değişmesiyle birlikte ekranda da değişimesini sağladık
        self.qLblAirspeed.setText('Hız: {:.2f} m/s'.format(airspeed))

        self.qLblAttitude.setText(
            'Attitude: pitch:{:.2f}°, roll:{:.2f}°, yaw:{:.2f}°'.format(attitude.pitch, attitude.roll, attitude.yaw))

        self.qLblLocation.setText(
            'Konum:{:.2f}°N, Lon:{:.2f}°S, Alt:{:.2f}'.format(location.lat, location.lon, location.alt))
        #latitude °N longitude °S (Enlem-Boylam)
        self.qLbLBatarya.setText("Batarya Durumu:{:.2f}".format(batarya_seviye))


    #Tuşa basıldığında uçağın çalışmasına sağlayan fonksiyon

    def arm_vehicle(self):
        self.vehicle.armed = True


qApp = QApplication(sys.argv)
qWin = MainWindow()
qWin.show()
sys.exit(qApp.exec_())
qWin.vehicle.close()
