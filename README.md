### 프로그램 설명

- 로그인 기능은 없다
- front-end에서 image를 전송하여 back-end에 저장할 수 있다.
- image를 저장하고 thumbnail 을 생성한다.
- image와 thumbnail은 같은 폴더에 저장되어야하나?
- image들은 usage를 가진다.
- image들은 usage에 상관없이 같은 dir에 저장된다.
- file I/O 는 많을 것 같지만 같은 파일에 여러번 접근하는 경우는 별로 없을 것 같다.

### MongoDB

| Info 종류       | Name                        | Description                                                  |      |
| -------------- | --------------------------- | ------------------------------------------------------------ | ---- |
| Path           | images                      | image 들이 저장되는 최상위 폴더                              |      |
| Path           | images/original             | 원본 이미지들이 저장되는 폴더                                |      |
| Path           | images/thumbnail            | 썸네일 이미지들이 저장되는 폴더                              |      |
| Image          | filename(unique)            | 동일한 이름의 이미지 파일이 넘어온다면 <br />index number를 붙여서 unique 하게 만든 다음에 db에 넣고<br />파일 해당 파일 이름으로 저장한다. |      |
| Image metadata | image-usage                 | 이미지들의 usage [training, test, validation, unuse]         |      |
| Image metadata | size (width, height, depth) | 이미지 크기와 depth                                          |      |
|                |                             |                                                              |      |

### Directory Tree

```
​```
user
│
└───project
    │
    └──images
       │ 
       └───original
       │   image1.jpg
       │   image2.jpg
       │
       └───thumbnail
           thumbnail-image1.jpg
           thumbnail-image2.jpg
           
​```
```

이미지, 썸네일, 메타데이터? - 원본 이미지만 메타데이터가 있을까? 아니면 썸네일도 메타데이터를 가지고 있을까?

가지고 있다고 생각한다.

mongoDB가 가지고 있는 정보들

- image folder path
- 

python type hinting을 넣는다.

### Testing
- test framework pytest



### Start Backend
1. install mongodb
2. install python requirements
3. run mongodb
4. run executor
5. run broker (If needed)
6. run webserver
