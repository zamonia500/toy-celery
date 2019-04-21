### 프로그램 설명

- front-end에서 image를 전송하여 back-end에 저장할 수 있다.
- image를 저장하고 thumbnail 을 생성한다.
- image와 thumbnail은 같은 폴더에 저장되어야하나?
- image들은 usage를 가진다.
- image들은 usage에 상관없이 같은 dir에 저장된다.

### MongoDB

| Info 종류 | Name             | Description                     |      |
| --------- | ---------------- | ------------------------------- | ---- |
| Path      | images           | image 들이 저장되는 최상위 폴더 |      |
| Path      | images/original  | 원본 이미지들이 저장되는 폴더   |      |
| Path      | images/thumbnail | 썸네일 이미지들이 저장되는 폴더 |      |
|           |                  |                                 |      |



### Directory Tree

```
​```
project
│
└───images
│   └───original
│   │   image1.jpg
│   │   image2.jpg
│   │
│   └───thumbnail
│   │   thumbnail-image1.jpg
│   │   thumbnail-image2.jpg
│       
​```
```

이미지, 썸네일, 메타데이터? - 원본 이미지만 메타데이터가 있을까? 아니면 썸네일도 메타데이터를 가지고 있을까?

가지고 있다고 생각한다.

mongoDB가 가지고 있는 정보들

- image folder path
- 

python type hinting을 넣는다.