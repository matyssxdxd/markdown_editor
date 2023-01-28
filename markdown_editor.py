class MarkdownEditor:

    def __init__(self, string):
        self.string = string

    def format(self, text):
        if self.string == "plain":
            return text
        if self.string == "bold":
            return "**" + text + "**"
        if self.string == "italic":
            return "*" + text + "*"
        if self.string == "inline-code":
            return "`" + text + "`"

    def lists(self, text, row):
        if self.string == "ordered-list":
            return str(row) + ". " + text + "\n"
        elif self.string == "unordered-list":
            return "* " + text + "\n"


available_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list",
                        "new-line", "unordered-list", "ordered-list"]
formatted = []

print("Markdown Editor")
print("If you need any help: !help")

while True:
    user_input = input("\nChoose a formatter: ")

    if user_input in available_formatters:
        markdown = MarkdownEditor(user_input)
        if user_input == "header":
            while True:
                header_level = int(input("Level: "))
                if 6 >= header_level >= 1:
                    break
                else:
                    print("The level should be within the range of 1 to 6")
                    continue
            user_text = input("Text: ")
            format_header = (lambda x, y: "#" * x + " " + y + "\n")(header_level, user_text)
            formatted.append(format_header)
        elif user_input in ["plain", "bold", "italic", "inline-code"]:
            user_text = input("Text: ")
            formatted.append(markdown.format(user_text))
        elif user_input == "new-line":
            formatted.append("\n")
        elif user_input == "link":
            user_label = input("Label: ")
            user_link = input("URL: ")
            format_link = (lambda x, y: "[" + x + "]" + "(" + y + ")")(user_label, user_link)
            formatted.append(format_link)
        elif user_input in ["unordered-list", "ordered-list"]:
            while True:
                user_rows = int(input("Number of rows: "))
                if 1 > user_rows:
                    print("The number of rows should be greater than zero")
                    continue
                else:
                    break
            for rows in range(user_rows):
                user_text = input(f"Row #{rows+1}: ")
                formatted.append(markdown.lists(user_text, rows+1))
    elif user_input == "!done":
        with open("output.md", 'w') as file:
            for i in range(len(formatted)):
                file.writelines(formatted[i])
            file.close()
        break
    elif user_input == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
        continue
    else:
        print("Unknown formatting type or command")
        continue
    print("".join(formatted))
