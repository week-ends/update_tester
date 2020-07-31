# update_tester

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-flask](https://img.shields.io/badge/Made%20with-Flask-1f425f.svg)](https://flask.palletsprojects.com/)

<br/>

- 실행시 url에서 버전을 확인한다.
- This software check the version in the url at the time of execution.

- 낮은 버전으로 확인될 경우 로고를 업데이트한다.
- Logo(app/img/logo.png) of the software if confirmed with a lower version.


---

<br/>

## [문일주](https://github.com/mooniljoo)

### [ [LinkedIn](https://www.linkedin.com/in/oneweek/) ] [ [Blog](https://mooniljoo.github.io/) ]

---

<br/>

## How to Test



1. server 디렉토리로 이동 후 server.py 구동

```
$ cd server
```

```
$ python server.py
```

2. app 디렉토리로 이동 후 app.py 구동

```
$ cd ../app
```

```
$ python app.py
```

3. 정상적으로 재시작되고 이미지가 바뀌었는지 확인

- 기존 버전의 칼라이미지에서 업데이트되면 흑백으로 바뀐다.
- If the update is successful, check the change from the existing version of the color logo to the monochrome logo.

### File Description

```
.
├── app                     # app files
│   ├── img
│   │   └── logo.png        # **target to update**
│   └── app.py              # **app**
│
└── server                  # server files
    ├── files
    │   └── 1.1.zip         # **updated contents**
    ├── static
    │   └── version.txt     # **string of new version**
    ├── templates           # practices for Flask (not need)
    │   └── index.html
    │   └── update.html
    │   └── upload.html
    └── server.py           # **server**
```

### app.py

```
__version__ = 1.0
```
