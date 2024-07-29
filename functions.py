import serial
from serial import tools
from serial.tools import list_ports

from time import sleep
import settings


CurrentConnectionState = 'Disconnected'
ser = serial.Serial()
ser.timeout = 0.2
def AddTextLog(self, massage):
    self.m_textCtrl1.AppendText(massage+ '\n')
    self.m_textCtrl1.Refresh()



def EnableComParts(self):
    self.m_comboBox1.Enabled = True

def DisableComParts(self):
    self.m_comboBox1.Enabled = False

def SendCommand(command):
    if ser.is_open == False:
        return
    ser.write(command)

def FindComPorts(self):
    u = tools.list_ports.comports()
    ports = []
    self.m_comboBox1.Clear()
    for element in u:
        ports.append(element.device)
        self.m_comboBox1.Append(element.device)
        num = self.m_comboBox1.GetCount()
        self.m_comboBox1.SetSelection((num - 1))

def ConnectToComPort(self):
    global CurrentConnectionState
    if self.m_comboBox1.GetStringSelection() == '':
        AddTextLog(self, 'Нет com портов')
        return
    if CurrentConnectionState == 'Disconnected':
        ser.port = self.m_comboBox1.GetStringSelection()
        ser.baudrate = settings.BOUDRATE
        ser.parity = 'N'
        ser.stopbits = 1
        if self.m_toggleBtn2.GetValue() == 1:
            try:
                ser.open()
            except Exception:
                AddTextLog(self, 'Порт занят')
                self.m_toggleBtn2.SetValue(0)
                return
            if ser.is_open == True:
                AddTextLog(self, 'Подключен к ком порту: ' + ser.port)
                DisableComParts(self)
                CurrentConnectionState = 'Connected'

            else:
                AddTextLog(self, 'Не удалось подключиться к com-порту')
        else:
            ser.close()
            EnableComParts(self)
            AddTextLog(self, 'Отключились от порта')
    elif CurrentConnectionState == 'Connected':
        ser.close()
        EnableComParts(self)
        CurrentConnectionState = 'Disconnected'
        AddTextLog(self, 'Отключен')

def FlashStart(self):
    global CurrentConnectionState
    if self.m_toggleBtn2.GetValue() == 0:   #если нет подключения к ком порту то выходим из функции
        AddTextLog(self, 'Нет подкчлюения к COM порту')
        return 1
    if self.OpenedFileLenth == 0:   #если не выбран файл то выходим из функции
        AddTextLog(self, 'Файл не выбран')
        return 3
    RCN = ReadCpuName(self)
    if RCN == 3:
        return 8
    elif RCN != 0:
        for i in range(0, 100):
            if CmdBootOn(self) == 0:
                if ReadCpuName(self) != 0:
                    return 7
                break
            else:
                if i == 99:
                    return 3

    sleep(0.5)
    if EraseFlash(self) != 0:
        return 4
    self.m_gauge1.SetRange(self.StringToSend)
    self.m_gauge1.SetValue(0)
    SendedStrings=0
    for e in range(0,self.OpenedFileLenth):
        if self.OpenedFile[e] == ':':
            cmd = bytes(self.OpenedFile[e + 1:e + 3], encoding='utf-8')
            if cmd == b'10':
                buf = []
                buf.append(settings.WM_Command)
                buf.append(255-settings.WM_Command)
                buf.append(settings.MAGIC_WORD[0])
                buf.append(settings.MAGIC_WORD[1])
                buf.append(settings.MAGIC_WORD[2])
                buf.append(settings.MAGIC_WORD[3])
                buf.append(int(self.OpenedFile[e + 3:e + 5], 16))
                buf.append(int(self.OpenedFile[e + 5:e + 7], 16))
                for b in range(0, 16):
                    buf.append(int(self.OpenedFile[e + 9 + 2 * b:e + 11 + 2 * b], 16))
                crc = 0
                for c in range(0, len(buf)):
                    crc = crc + buf[c]
                    if crc >= 256:
                        crc = crc-256
                if crc == 0:
                    buf.append(crc)
                else:
                    buf.append(256-crc)
                print(buf)
                ser.write(buf)
                answer = ser.read(1)
                if len(answer) == 0:
                    AddTextLog(self, 'Нет ответа от МК')
                    AddTextLog(self, 'Прошивка не удалась')
                    self.m_gauge1.SetValue(0)
                    return 5
                answer = (ord(answer))
                if answer == settings.ACK:
                    print('ack')
                    SendedStrings = SendedStrings+1
                    self.m_gauge1.SetValue(SendedStrings)
                    self.m_gauge1.Refresh()
                    if self.StringToSend == SendedStrings:
                        AddTextLog(self, 'Прошивка завершена')
                elif answer == settings.NACK:
                    print('nack')
                    return 6

    sleep(0.1)
    RESET_MCU(self)
    return 0

def SetKeyWord(self):
    if ser.is_open == False:
        AddTextLog(self, 'Не подключен COM-порт')
        return
    BytesToSend = [settings.SET_KEY_Command, 255-settings.SET_KEY_Command, settings.BOOTLOADER_KEY_VALUE[0], settings.BOOTLOADER_KEY_VALUE[1], settings.BOOTLOADER_KEY_VALUE[2], settings.BOOTLOADER_KEY_VALUE[3]]
    ser.write(BytesToSend)
    answer = ser.read(1)
    if len(answer) == 0:
        AddTextLog(self, 'Нет ответа от МК')
        return
    print(ord(answer))
    answer = (ord(answer))
    if answer == settings.ACK:
        print('ack')
        AddTextLog(self, 'Key_word установлен')
        Key_word_set = True
    elif answer == settings.NACK:
        print('nack')
        Key_word_set = False
        AddTextLog(self, 'Key_word не установлен')


def EraseFlash(self):
    if ser.is_open == False:
        AddTextLog(self, 'Не подключен COM-порт')
        return 1
    ser.timeout = 0.5
    BytesToSend =[]
    BytesToSend.append(settings.FLASH_ERASE)
    BytesToSend.append(255-settings.FLASH_ERASE)
    BytesToSend.append(settings.MAGIC_WORD[0])
    BytesToSend.append(settings.MAGIC_WORD[1])
    BytesToSend.append(settings.MAGIC_WORD[2])
    BytesToSend.append(settings.MAGIC_WORD[3])
    BytesToSend.append(255)
    crc = CheckumCalc(BytesToSend, len(BytesToSend))
    BytesToSend.append(crc)
    print(BytesToSend)
    ser.write(BytesToSend)
    answer = ser.read(1)
    ser.timeout = 0.2
    if len(answer) == 0:
        AddTextLog(self, 'Нет ответа от МК')
        return 2

    answer = (ord(answer))
    if answer == settings.ACK:
        print('ack')
        AddTextLog(self, 'Удалось стереть flash')
    elif answer == settings.NACK:
        print('nack')
        AddTextLog(self, 'Не удалось стереть flash')
    return 0

def RESET_MCU(self):

    if ser.is_open == False:
        AddTextLog(self, 'Не подключен COM-порт')
        return 1
    BytesToSend = [settings.RESET_Command, 255 - settings.RESET_Command]
    BytesToSend.append(settings.MAGIC_WORD[0])
    BytesToSend.append(settings.MAGIC_WORD[1])
    BytesToSend.append(settings.MAGIC_WORD[2])
    BytesToSend.append(settings.MAGIC_WORD[3])
    crc = CheckumCalc(BytesToSend, len(BytesToSend))
    BytesToSend.append(crc)
    ser.write(BytesToSend)
    answer = ser.read(1)
    if len(answer) == 0:
        AddTextLog(self, 'Нет ответа от МК')
        return 2
    print(ord(answer))
    answer = (ord(answer))
    if answer == settings.ACK:
        print('ack')
        AddTextLog(self, 'Перезагрузка MCU')
    elif answer == settings.NACK:
        print('nack')
        AddTextLog(self, 'Не удалось перезагрузить')
        return 3
    return 0

def ReadCpuName(self):
    if ser.is_open == False:
        AddTextLog(self, 'Не подключен COM-порт')
        return 1
    BytesToSend = [settings.READ_CPU_NAME, 255 - settings.READ_CPU_NAME, settings.MAGIC_WORD[0],
                   settings.MAGIC_WORD[1], settings.MAGIC_WORD[2], settings.MAGIC_WORD[3]]
    crc = CheckumCalc(BytesToSend, len(BytesToSend))
    BytesToSend.append(crc)
    print(BytesToSend)
    ser.write(BytesToSend)
    answer = ser.read(30)
    if len(answer) == 0:
        AddTextLog(self, 'Нет ответа от МК')
        return 2
    print(answer)
    tmp=answer.decode('UTF-8')

    AddTextLog(self, tmp)
    return 0

def CmdBootOn(self):
    if ser.is_open == False:
        AddTextLog(self, 'Не подключен COM-порт')
        return 1
    BytesToSend =[]
    BytesToSend.append(settings.CMD_BOOT_ON)
    BytesToSend.append(255-settings.CMD_BOOT_ON)
    BytesToSend.append(settings.MAGIC_WORD[0])
    BytesToSend.append(settings.MAGIC_WORD[1])
    BytesToSend.append(settings.MAGIC_WORD[2])
    BytesToSend.append(settings.MAGIC_WORD[3])
    crc = CheckumCalc(BytesToSend, len(BytesToSend))
    BytesToSend.append(crc)
    print(BytesToSend)
    ser.write(BytesToSend)
    answer = ser.read(1)
    if len(answer) == 0:
        AddTextLog(self, 'Нет ответа от МК')
        return 2
    answer = (ord(answer))
    if answer == settings.ACK:
        print('ack')
        AddTextLog(self, 'Удалось войти в режим бутлоадера')
    elif answer == settings.NACK:
        print('nack')
        AddTextLog(self, 'Не удалось войти в режим бутлоадера')
    return 0

def CheckumCalc(data, len):

    ret_val=0
    for k in range(0,len):
        ret_val = ret_val + data[k]
        if ret_val>= 256:
            ret_val = ret_val-256
    if ret_val==0:
        return 0
    else:
        return 256-ret_val

