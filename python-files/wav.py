import sys
import os
from windows_toasts import WindowsToaster, ToastText1

wintoaster = WindowsToaster('ECO')


#Defining Notifications
ErrorFormatToast = ToastText1()
ErrorFormatToast.SetBody('ERROR: Invalid Format')

ConvertingToast = ToastText1()
ConvertingToast.SetBody('Converting File...')

ConvertedToast = ToastText1()
ConvertedToast.SetBody('File Converted!')

valid_formats = [
    "mp3",
    "wav",
    "ogg",
    "flac",
    "aac",
    "m4a",
    "wma",
    "aiff",
    "ape",
    "mid",
    "opus",
    "amr",
    "mka"
]

#Get the file
file = sys.argv[1]
print("File:", file)

#Get the format
fileFormat = file.split('.')
fileFormat = fileFormat[-1].lower()
print('Format:', fileFormat)

# Get the path and the name
FilePath = file.split("\\")

FileName = FilePath[-1].split('.')
FileName.pop()
FileName = ".".join(FileName)

FilePath.pop()
FilePath = "\\".join(FilePath)
print('Path:',FilePath)

#If the file format is valid
if fileFormat in valid_formats:
    ConvertedFilePath = FilePath + "\\" + FileName + '_converted.wav'
    OsCommand = r'"C:\Program Files\ECO\ffmpeg\bin\ffmpeg" -i ' + file + ' ' + ConvertedFilePath
    wintoaster.show_toast(ConvertingToast)
    os.system(OsCommand)
    wintoaster.show_toast(ConvertedToast)

else:
    wintoaster.show_toast(ErrorFormatToast)