import time
import winsound


def alarm():
    try:
        mytime = list(map(int, input("Enter time in hr min sec \n").split()))
        if len(mytime) == 3:
            total_seconds = mytime[0]*60*60 + mytime[1]*60 + mytime[2]
            time.sleep(total_seconds)
            frequency = 2500
            duration = 1000
            winsound.Beep(frequency, duration)
        else:
            print("Please enter time in correct format as mentioned\n")
            alarm()

    except Exception as e:
        print("This is the exception\n", e, "So!, please enter correct details.")
        alarm()


alarm()