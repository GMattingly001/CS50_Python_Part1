def main():

    x,y,z = input("Expression: ").split(" ")
    if x.isnumeric() and z.isnumeric():
        x = float(x)
        z = float(z)
        match y:
            case "+":
                print(x + z)
            case "-":
                print(x - z)
            case "*":
                print(x * z)
            case "/":
                print(x / z)

    else:
        pass


main()