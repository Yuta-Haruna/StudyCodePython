
import sys
from cmd.BaseCmd import BaseCmd


# 基礎的な文法
print("Hello, World!")


# インスタンス生成
cmd = BaseCmd()
# メソッド呼び出し (引数self用) 
cmd.show_python_version()

# メソッド呼び出し　通常実行
print( BaseCmd.function_name("aaaaa"))
print(BaseCmd.addCalc(1,2))


print("--------------------------------------------------------")


# 適当なプログラム　練習用
print("1は1件(int)、2は複数入力: ", end='')
mode_input = int(input())


# 入力が1件のみ　数値
if mode_input == 1:
    # 改行しないpattern
    print("Enter a number: ", end='')

    # 数字の入力を受け取る
    user_input = input()
    # print(type(user_input))

    print("int型チェック結果　：" + str(BaseCmd.CheckInt(user_input)))

    # int型の場合は、再格納する
    if BaseCmd.CheckInt(user_input):
        user_input = int(user_input)
    else:
        print("無効な値が入力された_1111")
        # 処理の終了
        sys.exit()

    print(type(user_input))

elif mode_input == 2:
    # スペース区切りの数値を受け取る
    input_values = input("Enter 2 space-separated numbers: ").split()

    # 取得した値を整数に変換してリストに格納
    numbers = [int(value) for value in input_values]

    # 格納用
    numList = []

    # 初回データを取り込む
    for num in range(numbers[0]):
        print("Enter a number: ", end='')
        temp = int(input())
        numList.append(temp)

    # 

