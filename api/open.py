import threading
import subprocess
from pathlib import Path
from api.settings import my_platform

BASE_DIR = Path(__file__).resolve().parent


def myPlatformDependency():
    return my_platform == "Windows"


dependency = myPlatformDependency()


def app1():
    subprocess.run(
        ["python", str(BASE_DIR / "manage.py"), "runserver"], shell=dependency
    )


def app2():
    subprocess.run(["python", str(BASE_DIR / "my_bot/bot.py")], shell=dependency)


if __name__ == "__main__":
    t1 = threading.Thread(target=app1)
    t2 = threading.Thread(target=app2)
    t1.start()
    t2.start()
