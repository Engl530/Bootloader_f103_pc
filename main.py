import wx
import noname
import functions
import settings
from threading import Thread

class Main_window(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)
        functions.FindComPorts(self)  # находит ком-порты
        self.OpenedFile = 0
        self.OpenedFileLenth = 0
        self.OpenedFileFullPages = 0
        self.StringToSend = 0
        # th1 = Thread(target=functions.auto_reset_key, args=(self,), daemon=True)
        #th1.start()


    def ConnectToComPort(self, e):  # перезаписываем функцию бинда кнопки подключения
        functions.ConnectToComPort(self)

    def FilDialogOpen(self, e):
        FD = wx.FileDialog(self, "Открыть файл: ", wildcard="hex файлы (*.hex)|*hex", style=wx.FD_OPEN)
        if FD.ShowModal() == wx.ID_CANCEL:
            return
        pathname = FD.GetPath()
        self.m_staticText1.SetLabel(pathname)
        f = open(pathname, 'r')
        self.OpenedFile = f.read()
        f.close()
        self.OpenedFileLenth = len( self.OpenedFile)
        self.strings=0
        for e in range(0, self.OpenedFileLenth):
            if self.OpenedFile[e] == ':':
                self.strings = self.strings+1

        if self.OpenedFileLenth >= settings.MAX_BIN_SYMBOLS:
            print(self.OpenedFileLenth)
            self.OpenedFileLenth = 0
            functions.AddTextLog(self, 'слишком большой файл прошивки')
            return
        self.StringToSend = 0
        for e in range(0, self.OpenedFileLenth):
            if self.OpenedFile[e] == ':':
                cmd = bytes(self.OpenedFile[e + 1:e + 3], encoding='utf-8')
                if cmd == b'10':
                    self.StringToSend = self.StringToSend+1
        print('StringsToSend = ', self.StringToSend)
        functions.AddTextLog(self, 'выбран файл: ' +pathname)
        functions.AddTextLog(self, 'символов: ' +str(self.OpenedFileLenth))
        functions.AddTextLog(self, 'строк: ' +str(self.strings))


    def FlashStart(self, e):
        functions.FlashStart(self)


app = wx.App(False)
frame = Main_window(None)
frame.Show(True)
# start the applications
app.MainLoop()