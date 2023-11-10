import random
import xml.etree.ElementTree as ET

def load_config():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    n = int(root.find('n').text)
    return x1, x2, n

def generate_target_number(x1, x2):
    return random.randint(x1, x2)

def main():
    x1, x2, n = load_config()
    target_number = generate_target_number(x1, x2)

    print(f"猜猜看目標數字是在 {x1} 和 {x2} 之間。")

    for _ in range(n):
        guess = int(input("請輸入你的猜測: "))
        if guess == target_number:
            print("恭喜你，猜對了！")
            break
        elif guess < target_number:
            print("太低了，再試一次。")
        else:
            print("太高了，再試一次。")
    else:
        print(f"抱歉，你已經猜了{n}次，仍未猜對。目標數字是 {target_number}。")

if __name__ == "__main__":
    main()
