def check_HDL(HDL):
    if HDL >= 60:
        return "Normal"
    elif 40 <= HDL < 60:
        return "Borderline Low"
    else:
        return "Low"
def cholesterol_check():
    print("Cholesterol Check")
    chol = input("Enter your cholesterol result: ")
    chol_data = chol.split("=")
    if chol_data[0] == "HDL":
        result = check_HDL(int(chol_data[1]))
        print("The cholesterol level is {}.".format(result))
def interface():
    keep_running = True
    while keep_running:
        print("My Program")
        print("Options:")
        print("1 - Cholesterol Check")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            keep_running = False
        elif choice == '1':
            cholesterol_check()
    return
if __name__ == '__main__':
        interface()
