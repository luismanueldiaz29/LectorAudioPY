from PySide2.QtWidgets import QWidget, QDialog, QFileDialog, QTableWidgetItem, QMessageBox, QVBoxLayout
from views.indexView import indexView
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import scipy.io.wavfile as waves
import scipy.fftpack as fourier

class indexController(QWidget, indexView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # inicializo los componentes de el widget
        self.init(); # inicializo mis variables
    
    def init(self):
        self.pushButtonFile.clicked.connect(self.uploadFileAudio)
        self.initWidgetAudio()
        self.initWidgetAudioProcesado()
    
    def uploadFileAudio(self):
        # QMessageBox.question(self, "Mensaje de dialogo", "Clicked")
        frame = QFileDialog.getOpenFileName(self, 'Seleccionar el audio', '../',  'TXT files (*.wav)')
        self.MapearAudio(frame[0])

    def MapearAudio(self, fileName):
        muestreo, sonido = waves.read(fileName)
        procesado = fourier.fft(sonido)

        self.axisAudio.plot(sonido)
        self.canvasAudio.draw()
        self.canvasAudio.flush_events()

        self.axisAudioProcesado.plot(procesado)
        self.canvasAudioProcesado.draw()
        self.canvasAudioProcesado.flush_events()
        
        print("Muestreo -> ", muestreo)
        print("sonido -> "+str(list(sonido)))
        print("fourier -> "+str(list(sonido)))

    
    def initWidgetAudio(self):
        self.figureAudio = Figure(figsize=(20, 12), dpi=80)
        self.canvasAudio = FigureCanvasQTAgg(self.figureAudio)
        self.axisAudio = self.figureAudio.add_subplot(111)
        self.layoutverticalAudio = QVBoxLayout(self.widgetAudio)
        self.layoutverticalAudio.addWidget(self.canvasAudio)

    def initWidgetAudioProcesado(self):
        self.figureAudioProcesado = Figure(figsize=(20, 12), dpi=80)
        self.canvasAudioProcesado = FigureCanvasQTAgg(self.figureAudioProcesado)
        self.axisAudioProcesado = self.figureAudioProcesado.add_subplot(111)
        self.layoutverticalAudioProcesado = QVBoxLayout(self.widgetAudioProcesado)
        self.layoutverticalAudioProcesado.addWidget(self.canvasAudioProcesado)

