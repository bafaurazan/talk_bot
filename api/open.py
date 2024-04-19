import threading
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def app1():
    subprocess.run(["python", str(BASE_DIR / "manage.py"), "runserver"], shell=True)


def app2():
    subprocess.run(["python", str(BASE_DIR / "my_bot/bot.py")], shell=True)


if __name__ == "__main__":
    t1 = threading.Thread(target=app1)
    t2 = threading.Thread(target=app2)
    t1.start()
    t2.start()
