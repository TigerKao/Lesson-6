# 讀取檔案
def read_file(filename):
    chat = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        for line in f:
            chat.append(line.strip())
    return chat

# 改寫檔案
def convert(chat):
    new = []
    person = None
    for line in chat:
        if line == "Allen":
            person = "Allen"
            continue
        elif line == "Tom":
            person = "Tom"
            continue
        if person:
            new.append(person + ": " + line)
    return new

# 寫入檔案
def write_file(filename, new):
    with open(filename, "w", encoding = "utf-8-sig") as f:
        for line in new:
            f.write(line + "\n")

# 主程式執行
def main():
    chat = read_file("input.txt")
    chat = convert(chat)
    write_file("output.txt", chat)

if __name__ == "__main__":
    main()
