def main():
    correct_answer = "サムギョプサル"
    while True:
        user_input = input("答えを入力してください: ")
        if user_input == correct_answer:
            print("正解です！")
            break
        else:
            print("答えが違います。もう一度入力してください。")

if __name__ == "__main__":
    main()
