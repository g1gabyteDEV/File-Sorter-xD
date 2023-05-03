import shutil
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("files") if isfile(join("files", f))]
for i in files:
  if i.find(".docx") != -1 or i.find(".doc") != -1 or i.find(".odt") != -1 or i.find(".pdf") != -1:
    shutil.move(f"files/{i}", f"files/Documents/{i}")
  elif i.find(".jpg") != -1 or i.find(".png") != -1 or i.find(".gif") != -1 or i.find(".jpeg") != -1 or i.find(".bmp") != -1 or i.find(".svg") != -1:
    shutil.move(f"files/{i}", f"files/Pictures/{i}")
  elif i.find(".mp3") != -1 or i.find(".wav") != -1 or i.find(".ogg") != -1 or i.find(".flac") != -1:
    shutil.move(f"files/{i}", f"files/Music/{i}")
  elif i.find(".mp4") != -1 or i.find(".mov") != -1 or i.find(".m4v") != -1 or i.find(".wmv") != -1:
    shutil.move(f"files/{i}", f"files/Videos/{i}")
  elif i.find(".exe") != -1 or i.find(".msi") != -1 or i.find(".bat") != -1 or i.find(".ps1") != -1 or i.find(".lnk") != -1:
    shutil.move(f"files/{i}", f"files/Executables/{i}")