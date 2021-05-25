class Token():
    def __init__(self):
        self.INCREMENT_POINTER = ">"
        self.DECREMENT_POINTER = "<"
        self.INCREMENT_BYTE = "+"
        self.DECREMENT_BYTE = "-"
        self.OUTPUT = "."
        self.INPUT = ","
        #TODO: Implement jumps
        self.valid_tokens = [">", "<", "+", "-", ".", ","]

    def get_tokens(self, string):
        tokens = []
        for char in string:
            if char not in self.valid_tokens:
                print(f'{char} is not a valid command')
                continue
            tokens.append(char)

        return tokens


def __main__():
    tokenizer = Token()
    while True:
        input_string = input("brainfuck$ ")
        if input_string == "quit":
            break
        tokens = tokenizer.get_tokens(input_string)
        print(tokens)

if __name__ == "__main__":
    __main__()
