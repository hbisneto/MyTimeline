---
This project was created using [PyBridge](https://github.com/hbisneto/PyBridge)

---

# MyTimeline

## Requirements and Dependencies

MyTimeline requires:

- Python 3.9.0 or later
- Tweepy (Version 4.14 is recommended)
- Twitter Keys and Tokens

## How to Run

```
1. Download this repository
2. Install dependecies
3. Open the file __init__.py
4. Run
```

<details>
<summary>Working With Virtual Environment</summary>

### Creating a Virtual Environment

Open Terminal follow:

**1. Choose a directory:**

```
cd /Users/YourName/Desktop/Projects/
```

**2. Create a Virtual Environment:**

```
virtualenv mytimeline
```

**3. Change Directory:**

```
cd mytimeline
```

**4. Activate Environment:**

```
source bin/activate
```

Your environment is activated and now you can install dependencies

**5. Install Dependencies:**

```
pip install tweepy
pip install --upgrade pip
```

**6. Structure:**

To run the project, make sure your "init.py" file is located in the root of the project as below:

```
.
├── __init__
├── bin
│ ├── activate
│ └── ...
├── exception
│ └── Exceptions.py
├── lib
│ ├── python3.x
│ └── ...
├── system
│ └── SystemRequirements.py
├── linux
│ ├── Linux.py
│ ├── LinuxApp.py
│ ├── FileSystem.py
│ └── SplashScreen.py
├── mac
│ ├── Mac.py
│ ├── MacApp.py
│ ├── FileSystem.py
│ └── SplashScreen.py
├── windows
│ ├── Windows.py
│ ├── WindowsApp.py
│ ├── FileSystem.py
│ └── SplashScreen.py
├── LICENSE
├── pyvenv.cfg
├── Twitter.py
└── README.md
```

**7. Run Program:**

On Terminal, run:

```
python3 __init__.py
```
</details>


## External Links

Here are some external links to learn more about the project

- [Twitter Developer Portal](https://developer.twitter.com/)
- [Tweepy Documentation](https://docs.tweepy.org/en/stable/index.html)

#

Copyright © 2023 Bisneto. All rights reserved.