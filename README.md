# update_tester

## Used Webframework

- [Flask](https://github.com/pallets/flask)

## Description

- 소프트웨어(app.py) 실행시 url에 접속해 업데이트한다.
- app/img/logo.png 업데이트가 이루어지는지 테스트한다.

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

## Specification



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
