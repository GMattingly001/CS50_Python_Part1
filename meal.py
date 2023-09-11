def main():
    time = input("What time is it? ")
    time_converted = convert(time)
    if 7.0 < time_converted < 8.0:
        print("Breakfast Time")
    elif 12.0 < time_converted < 13.0:
        print("Lunch Time")
    if 18.0 < time_converted < 19.0:
        print("Dinner Time")
    else:
        pass



def convert(time):
    try:
        x,y = time.split(":")
        y = int(y) / 60
        return int(x) + y
    except:
        print("Not a valid time.")
        return 0

if __name__ == "__main__":
    main()
