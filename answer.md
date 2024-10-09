# 第1次作業-作業-HW1
>
>學號：112111206
><br />
>姓名：李儲亮
><br />
>作業撰寫時間：60m
><br />
>最後撰寫文件日期：2024/10/09
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容
- [x] 個人認為完成作業須具備觀念

## 說明程式與內容

開始寫說明，該說明需說明想法，
並於之後再對上述想法的每一部分將程式進一步進行展現，
若需引用程式區則使用下面方法，
若為.cs檔內程式除了於敘述中需註明檔案名稱外，
還需使用語法` ```語言種類 程式碼 ``` `，其中語言種類若是要用python則使用py，java則使用java，C/C++則使用cpp，
下段程式碼為語言種類選擇csharp使用後結果：

```csharp
public void mt_getResult(){
    ...
}
```

若要於內文中標示部分網頁檔，則使用以下標籤` ```html 程式碼 ``` `，
下段程式碼則為使用後結果：

```html
<%@ Page Language="C#" AutoEventWireup="true" ...>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" ...>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
    </form>
</body>
</html>
```
更多markdown方法可參閱[https://ithelp.ithome.com.tw/articles/10203758](https://ithelp.ithome.com.tw/articles/10203758)

請在撰寫"說明程式與內容"該塊內容，請把原該塊內上述敘述刪除，該塊上述內容只是用來指引該怎麼撰寫內容。

1. 請解釋何謂git中下列指令代表什麼？並舉個例子，同時必須說明該例子的結果。其指令有add、commit、push、fetch、pull、branch、checkout與merge。

Ans:
    
    git add 將變更的文件添加到暫存區（stage），以便準備提交
    git commit 將暫存區的變更提交到本地倉庫，並附上描述信息
    git push 將本地倉庫的提交推送到遠端倉庫
    git fetch 從遠端倉庫下載變更（不自動合併），更新本地的遠端追蹤分支
    git pull 從遠端倉庫下載變更並自動合併到當前分支
    git branch 列出、創建或刪除分支
    git checkout 切換到另一個分支或恢復文件到某個版本
    git merge 將另一個分支的變更合併到當前分支



2. 於專案下的檔案—**hw1.py**，撰寫註解，以說明該程式每列中之背後意義。

    該hw1.py題目如下：

    ```
    統計字母數。假設今天輸入一句子，句子中有許多單字，單字皆為英文字母小寫，
    請統計句子中字母出現的字數，輸出實需要照字母排序輸出，且若該字母為0則不輸出

    如輸入
    this is an apple
    輸出
    a: 2
    e: 1
    h: 1
    i: 2
    l: 1
    n: 1
    p: 2
    s: 2
    t: 1
    ```

Ans:



3. 請新增檔案**hw1_2.py，**輸入一個正整數(N)，其中$1\le N \le 100000$，請將該正整數輸出進行反轉

    ```
    如輸入
    1081

    輸出
    1801

    如輸入
    1000

    輸出
    1
    ```

Ans:


4. **[課外題]**：請找尋資料，說明何謂**單元測試**，請新增檔案**hw1_3.py**，並利用溫度計攝氏轉華氏撰寫單元測試。

Ans:
# 主程式：攝氏轉華氏的函數
def c_to_f(c: float) -> float:
    return c * 9 / 5 + 32

# 簡單的測試函數，使用 assert 進行測試
def test_c_to_f():
    test_cases = [
        (0, 32),
        (100, 212),
        (-40, -40),
        (37, 98.6)
    ]
    for celsius, expected in test_cases:
        assert c_to_f(celsius) == expected
    print("簡單測試：All passed")

# 使用 unittest 模組進行進一步的單元測試
import unittest

class TestTemperatureConversion(unittest.TestCase):
    def test_cases(self):
        test_cases = [
            (100, 212), (0, 32), (37, 98.6),
            (-40, -40), (-20, -4),
            (1, 33.8), (-1, 30.2)
        ]
        for celsius, expected in test_cases:
            self.assertAlmostEqual(c_to_f(celsius), expected)

# 主程序：執行簡單測試和單元測試
if __name__ == '__main__':
    test_c_to_f()
    unittest.main()






## 個人認為完成作業須具備觀念

開始寫說明，需要說明本次練習需學會那些觀念 (需寫成文章，需最少50字，並且文內不得有你、我、他三種文字)且必須提供完整與練習相關過程的notion筆記連結