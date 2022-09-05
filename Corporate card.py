
from msilib.schema import ComboBox
import gspread
# from gspread_pandas import spread, client
import pandas as pd
from tkinter import *

# def read():
#     gc = gspread.service_account(filename="./h.json")
#     sh = gc.open('개발실 법인카드 이용내역').worksheet('2022년 9월')
#     print(sh.get('H3'))


gc = gspread.service_account(filename="./h.json")
sh = gc.open('개발실 법인카드 이용내역').worksheet('가맹점')

pd_data = pd.DataFrame(sh.get('B:C'))

root = Tk()
root.title('법카 등록')

root.resizable(False,False)

drop1 = ComboBox(root,value = ['2'] )

mainloop()
#local-catalyst-361600-4bfdd3e79a7c