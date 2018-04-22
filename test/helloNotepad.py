# coding: utf-8
from pywinauto.application import Application
import time
app= Application().start("notepad.exe")
app.UntitledNotepad.menu_select("도움말->메모장 정보")
# time.sleep(1) #없어도 충분히 기다림
app['메모장 정보'].확인.click()
app.UntitledNotepad.Edit.type_keys("동작하네",with_spaces= True)