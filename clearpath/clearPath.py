import shutil
import os


def main():
    main_path_trade = 'C:/SKL/iTX/src/main/java/com/st1/itx/trade/'
    main_path_db = 'C:/SKL/iTX/src/main/java/com/st1/itx/db/'
    main_path_single = 'C:/SKL/iTX/src/main/java/com/st1/itx/utol/common'
    trade = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9']
    db = ['domain', 'repository/day', 'repository/hist','repository/mon',
          'repository/online', 'service','service/springjpa','service/springjpa/cm',]
    for trade_sub in trade:
        main_path_trade_use = main_path_trade+trade_sub
        print(main_path_trade_use)
        try:
            shutil.rmtree(main_path_trade_use)
        except:
            pass
        os.makedirs(main_path_trade_use)

    for db_sub in db:
        main_path_db_use = main_path_db+db_sub
        print(main_path_db_use)
        try:
            shutil.rmtree(main_path_db_use)
        except: 
            pass
        os.makedirs(main_path_db_use)
    try:
        shutil.rmtree(main_path_single)
    except:
        pass


if __name__ == '__main__':
    main()
