def reverse_number():
    while True:
        try:
            # 輸入處理
            n = int(input("請輸入一個正整數 (1 <= N <= 100000): "))
            
            # 檢查是否在有效範圍內
            if 1 <= n <= 100000:
                # 反轉數字並輸出
                print(f"反轉後的數字為: {int(str(n)[::-1])}")
                break
            else:
                # 超出範圍提示
                print("輸入的數字超出範圍，請重新輸入！")
        
        except ValueError:
            # 捕捉非數字輸入的錯誤
            print("無效輸入，請輸入一個正整數！")

# 主程序調用
reverse_number()