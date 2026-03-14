FROM python:3.11

LABEL maintainer="contact@wookingwoo.com"

RUN apt-get update
RUN apt-get install -y wget unzip curl

RUN mkdir /home/namsigdang-crawler

# 컨테이너 내 프로젝트 root directory 설정
WORKDIR /home/namsigdang-crawler

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb # 크롬 다운
RUN apt -y install ./google-chrome-stable_current_amd64.deb # 크롬 설치

# Install ChromeDriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip # 크롬 드라이버 다운
RUN mkdir chromedriver # 크롬 드라이버를 설치할 경로로 chromedriver 디렉토리를 생성
RUN unzip /tmp/chromedriver.zip chromedriver -d /home/namsigdang-crawler/chromedriver # 크롬 드라이버 압축 해제

# Install namsigdang-crawler dependencies using file requirements.txt
COPY ./requirements.txt .
RUN pip install --upgrade pip # pip 업그레이드
RUN pip install -r requirements.txt # 패키지 설치

# Copy namsigdnag-crawler codes
COPY ./namsigdang_crawler ./namsigdang_crawler

# 컨테이너 내 프로젝트 root directory 설정
WORKDIR /home/namsigdang-crawler/namsigdang_crawler

ENV CHROME_DRIVER_OPTION=python_docker

# 실행
CMD ["python", "crawler_main.py"]

# docker build --tag namsigdang-crawler:1.0 .
