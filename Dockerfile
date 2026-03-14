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
RUN set -eux; \
    CHROME_VERSION="$(google-chrome --product-version)"; \
    CHROME_BUILD="$(echo "${CHROME_VERSION}" | cut -d. -f1-3)"; \
    CHROME_MILESTONE="$(echo "${CHROME_VERSION}" | cut -d. -f1)"; \
    CHROMEDRIVER_VERSION="$(curl -fsSL "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_BUILD}" || curl -fsSL "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_MILESTONE}")"; \
    wget -O /tmp/chromedriver.zip "https://storage.googleapis.com/chrome-for-testing-public/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip"; \
    mkdir -p /home/namsigdang-crawler/chromedriver /tmp/chromedriver; \
    unzip /tmp/chromedriver.zip -d /tmp/chromedriver; \
    mv /tmp/chromedriver/chromedriver-linux64/chromedriver /home/namsigdang-crawler/chromedriver/chromedriver; \
    chmod +x /home/namsigdang-crawler/chromedriver/chromedriver

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

# docker build --platform=linux/amd64 -t namsigdang-crawler:1.0 -f Dockerfile .
