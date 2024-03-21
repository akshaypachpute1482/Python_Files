import time
from plyer import notification

if __name__ == '__main__':
    notification.notify(
        title = "WATER NOTIFICATION",
        message = "Please Drink Water!!!!",
        timeout= 2
    )
    