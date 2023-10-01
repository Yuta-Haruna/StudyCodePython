class Test(object):
    def mergeAlternately(word1, word2):
        # print(word1)

        minSize = len(word1)

        # 文字の長さを確認
        if len(word1) > len(word2):
            minSize = len(word2)

        resultStr = ""
        # 小さいほうを基準に交互に代入する
        for num in range(minSize):
            resultStr = resultStr + word1[num] + word2[num] 

        if minSize < len(word2):
            for num in range(len(word2) - minSize):
                resultStr = resultStr + word2[minSize + num]
                print(resultStr)
        elif minSize < len(word1):
            for num in range(len(word1) - minSize):
                resultStr = resultStr + word1[minSize + num]
                print(resultStr)

        return resultStr
