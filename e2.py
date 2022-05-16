def morse_number(number):
    result = ""
    preconverted_values = ["-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
    for i in number:
        result += preconverted_values[int(i)]
        result += " "
    return result

n = input("enter number: ")
print("\nnumber ", n, " in morse code:\n", morse_number(n))