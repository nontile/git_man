# git cli usage

## 옵션
--global

## 사용자 설정

git config user.name <사용자 이름>

git config user.email <사용자 이메일>

git config --list

## 프로젝트 가져오기

git clone <URL.git>   # URL 뒤에 .git이 있어야됩니다

git remote add origin <git url>

git remote -v

# 

git push 

## 로그
git log --oneline --decorate --graph --all

## merge
git checkout master

git merge dev

