# talk_bot

- run terminal commands (for example - run certain app) using voice recognition
- gui - django webowka
- komenda wywołująca - bot
- ogarnąć rozróżnienie pomiędzy windą a unixem

# Getting started

## First setup

1. Clone the repository:

``` shell
git clone https://github.com/bafaurazan/talk_bot.git
```

2. Navigate to the project directory:

``` shell
cd talk_bot
```

## Starting app development

1. Copy the .env.example file:

``` shell
cp .env.example .env
```

- Modify the environment variables to suit your requirements.

2. Launching services

- Install app requirements

``` shell
python app_run.py --install
```

- run app

``` shell
python app_run.py
```

## If you strugle with python version, type the following

``` shell
poetry env use 3.12
```
