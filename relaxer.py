import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="**Please Drink Water Now!! and take some rest ",
            message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon=r"C:\Users\91996\Desktop\Practise\python\Aha-Soft-Free-3d-Glossy-First-aid.ico",
            timeout=12
        )
        time.sleep(60*60)

        # This gives remainders for every one hour
