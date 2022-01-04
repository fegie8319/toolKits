from shutil import copyfile
from tqdm import tqdm

def combine_name():
    trade_name = "L8"
    L8_trade = []
    for i in range(31,68):
        L8_trade.append(trade_name+str(i).zfill(3))

    for j in range(301,338):
        L8_trade.append(trade_name+str(j).zfill(3))

    copy_var(L8_trade)

def copy_var(L8_trade):
    source_path = r"X:\ifxfolder\Dev\var\tran\L8"
    target_path = r"D:\SKL\iFX\Dev\var\tran\L8"
    progess = tqdm(total=len(L8_trade))
    for trade in L8_trade:
        source_trade = source_path+'\\'+trade+".var"
        targer_trade = target_path+'\\'+trade+".var"
        copyfile(source_trade,targer_trade)
        progess.update(1)
    copy_tim(L8_trade)

def copy_tim(L8_trade):
    source_path = r"Y:\tim\L8"
    target_path = r"D:\SKL\iTX\tim\L8"
    progess = tqdm(total=len(L8_trade))
    for trade in L8_trade:
        source_trade = source_path+'\\'+trade+".tim"
        targer_trade = target_path+'\\'+trade+".tim"
        copyfile(source_trade,targer_trade)
        progess.update(1)
    copy_tom(L8_trade)

def copy_tom(L8_trade):
    source_path = r"Y:\tom\L8"
    target_path = r"D:\SKL\iTX\tom\L8"
    progess = tqdm(total=len(L8_trade)*2)
    for trade in L8_trade:
        source_trade = source_path+'\\'+trade+".tom"
        targer_trade = target_path+'\\'+trade+".tom"
        copyfile(source_trade,targer_trade)
        progess.update(1)
    for trade in L8_trade:
        source_trade = source_path+'\\'+trade+"_OC.tom"
        targer_trade = target_path+'\\'+trade+"_OC.tom"
        copyfile(source_trade,targer_trade)
        progess.update(1)

if __name__ == '__main__':
    combine_name()