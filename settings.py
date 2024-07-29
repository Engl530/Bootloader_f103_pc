# константы
BytesPerPage = 1024
MainAppOffset = 0
ACK = 0x79
NACK = 0x1F
CPU_NAME = 'STM32F030F4P6'
BOARD_NAME = 'KEBI 01'
SW_VERSION = '2100'
BOUDRATE = 115200
MAX_BIN_SYMBOLS = 42000      # максимальное количество символов в прошивке
# индексы буфера
COMMAND_INDEX = 0   # команда
NEG_COMMAND_INDEX= 1   # команда
MAGIC_WORD = [0x43, 0x21, 0xAB, 0xCD]
#N_PAGE = 2  # номер страницы для записи
#SIZE_MES = 3  # колчисетво байт далее
#FIRST_BYTE_IN_MES = 3  # колчисетво байт далее
# номера команд
RM_Command = 0x11           # read memory
GO_Command = 0x21           # GO command
WM_Command = 0x2B           # write memory
RESET_Command = 0x3C        # reset mcu
RESET_KEY_Command = 0xAB    # reset key word in mcu
SET_KEY_Command = 0xBB      # set key word in mcu
READ_CPU_NAME = 0x02        # read cpu name
FLASH_ERASE = 0x43          # erase cpu flash
CMD_BOOT_ON = 0x6E          #

