# git cli usage

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

# 버전
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

git checkout <branch>
 
