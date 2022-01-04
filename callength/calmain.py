import os

def countMain(path):
    ans = 0
    f_tom = open(path, mode='r', encoding='UTF-8').readlines()
    for everyTom in f_tom:
        everyTom = everyTom.replace('\n', '')  # 處理換行符號

        # 長度部分，依逗號分割
        value_string = everyTom.split(',')[1]
        # 宣告部分
        value_dec = everyTom.split(',')[0]

        if value_dec[-1] in ('X','x'):
            try:
                a = int(value_string.split('.')[0])
                b = int(value_string.split('.')[1])
                value = a * b
            except:
                value = int(value_string)
        else:
            try:
                a = int(value_string.split('.')[0])
                b = int(value_string.split('.')[1])
                value = a+b
            except:
                value = int(value_string)

        ans = ans + value

    return ans


def getFilepath(trade_name):
    '''取得檔案路徑與檢查是否存在'''
    path_list = []
    nas_path = r"\\192.168.10.8\itxDoc\tom"
    menu = trade_name[0:2]
    trade_path = os.path.join(nas_path,menu)
    '''取所有相符檔名'''
    try:
        for file in os.scandir(trade_path):
            filename = file.name[0:5]
            if filename == trade_name:
                path_list.append(os.path.join(trade_path,file.name))
        if path_list:
            return(path_list)
        else:
            print("無相符檔案，請重新輸入")
            main()
    except:
        print('無相符路徑，請重新輸入')
        main()
    

def main():
    '''主程式區塊'''
    trade_name = input("請輸入交易名稱，或按Ctrl+C離開: ")
    path = getFilepath(trade_name)
    for single in path:
        a = single.split('\\')
        
        re_msg = countMain(single)
        print(f"{a[-1]}長度為:{re_msg}")
    main()


if __name__ == '__main__':
    main()
