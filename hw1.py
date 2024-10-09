from typing import List #導入Typing函式庫中的List

def countLetters(sentence: str) -> List[int]: #定義一個計算字母出現次數的自訂函數
    letterCount: List[int] = [0] * 26 #創立一個長度26的列表，用來儲存每個字母的次數[a-z]

    for char in sentence: #利用For迴圈遍布所有字母
        if char.isalpha(): #如果字元為字母則執行以下
            index = ord(char) - ord('a') #判斷字母所處位置
            letterCount[index] += 1 #將對應字母次數增加1

    return letterCount #返回此自訂函數列表
pass

def printLetterCount(letterCount: List[int]) -> None: #定義一個列印字母出現次數的自訂函數

    for i in range(26): 
        if letterCount[i] > 0: #如果這個字母出現大於0，執行以下
            print(f"{chr(i + ord('a'))}: {letterCount[i]}") #列印出該字母和出現次數
pass

inputSentence: str = "this is an apple" #輸入所要檢測的字串
letterCount: List[int] = countLetters(inputSentence) #計算字母出現次數
printLetterCount(letterCount) #列印字母出現次數