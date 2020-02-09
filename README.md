# cozmo-turtle
a :robot: :turtle: friend to accompany the book Mindstorms

## setup

```bash
virtualenv .env -p python3
source ./env/bin/activate
pip install -r requirements.txt
```

Enter your LOGO commands in a file like this

```logo
PENDOWN
FORWARD(100)
ANGLE(50)
PENUP
```

Run the Cozmo-Turtle

```bash
python turtle.py -c commands.txt
```

### Extra credit

To make Cozmo sing, try this:

```bash
python sing.py
```

I made this to remind myself how to work Cozmo. And I'm keeping it.