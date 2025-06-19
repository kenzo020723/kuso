def main():
    correct_answer = "サムギョプサル"
    while True:
        user_input = input("答えを入力してください: ")
        if user_input == correct_answer:
            print("正解！")
            print("どうぞ。こちらがURLです" + "https://kenzo020723.github.io/kuso2/")
            break
        else:
            print("間違ってるよ")

    input("Enter を押して閉じる") 

if __name__ == "__main__":
    main()
