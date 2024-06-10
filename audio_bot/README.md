# my_bot

1. Navigate to the directory:

``` shell
cd talk_bot/my_bot
```

2. To run only my_bot 

- first install project requirements (info in main path README.md) then:

``` shell
poetry run python bot_config/bot.py
```

3. To get access to admin-site

- in your main system terminal type:

``` shell
poetry run python manage.py createsuperuser
```

**warning:** The project may not function completely correctly.
Its better to run the whole project.

**important**
- google api speech_recognition limit time 30 sec for command
- if problem with downloading pyaudio download from the source
https://www.wheelodex.org/projects/pyaudio/wheels/PyAudio-0.2.14-cp311-cp311-win_amd64.whl/
and `pip install ./path/to/downloaded/file`
