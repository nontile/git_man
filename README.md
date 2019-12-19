홈디렉토리 .gitconfig

## 옵션
--global

## 사용자 설정

git config user.name <사용자 이름>

git config user.email <사용자 이메일>

git config --list

git config credential.helper store

git conifg --global credential.helper 'cache --timeout 7200'

1 day: 86400
7 day: 604800
30day: 2592000

## 프로젝트 가져오기

git clone <URL.git> ./dir

git remote add origin <git url>

git remote -v

------------------------------------------

@ git remote add origin master <원격저장주소>
-> 원격저장소 등록

@ git remote -v
-> 원격저장소 보기

@ git push -u origin master :
-> 앞으로 현재 브랜치를 원격저장소 origin의 master에 동기화하겠다.

@ git remote remove <원격저장소이름>
-> 원격저장소로 등록한 이름과 주소 삭제

-----------------------------------------
원격저장소에 이미 파일이 있는 경우 pull을 먼저한다.(push 아닌)

git init .

git remote add origin <repository-url>
 
git pull origin master

※ git pull 충돌시 해결 방법 정리

1. git stash

2. git pull

3 git stash pop

## 버전
git add .

git commit -m ""

git push 

## 로그
git log --oneline --decorate --graph --all

git l
## merge
git checkout master

git merge dev

## branch
git branch -r

git branch -a

git checkout "<branch>"
 
