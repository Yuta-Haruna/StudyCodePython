
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

