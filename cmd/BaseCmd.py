import sys
import subprocess


class BaseCmd:


    # 基本的なPython関数の書き方
    def function_name(parameters):
        # 関数の本体（処理）
        # ...
        result = 'result' + parameters
        return result  # 必要に応じて戻り値を返す

    def show_python_version(self):
        # Pythonのバージョンを表示する
        print(sys.version)

    def print_hello_world(self):
        # Hello, World! を表示する
        print("Hello, World!")


    def addCalc(a, b):
        # 足し算するだけ
        return a + b


    # 入力された値がInt型かどうかチェックすr
    def CheckInt(user_input):
        try:
            # 変数を整数に変換
            int(user_input)
            return True
        except ValueError:
            # 変換が失敗した場合は False を返す
            return False

