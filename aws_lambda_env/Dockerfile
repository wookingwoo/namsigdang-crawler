FROM public.ecr.aws/lambda/python:3.9 as build

LABEL maintainer="contact@wookingwoo.com"

RUN yum install -y unzip curl && \
    curl -Lo /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_linux64.zip" && \
    curl -Lo /tmp/chrome-linux.zip "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F938549%2Fchrome-linux.zip?alt=media" && \
    unzip /tmp/chromedriver.zip -d /opt/ && \
    unzip /tmp/chrome-linux.zip -d /opt/ && \
    rm -f /tmp/chromedriver.zip /tmp/chrome-linux.zip && \
    yum clean all && \
    rm -rf /var/cache/yum


FROM public.ecr.aws/lambda/python:3.9

LABEL maintainer="contact@wookingwoo.com"

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN yum install -y --setopt=tsflags=nodocs \
    atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt dbus-glib && \
    yum clean all && \
    rm -rf /var/cache/yum

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=build /opt/chrome-linux /opt/chrome
COPY --from=build /opt/chromedriver /opt/

# Copy only the runtime files Lambda actually uses.
COPY namsigdang_crawler/crawler_main.py ./
COPY namsigdang_crawler/firebase_db.py ./
COPY namsigdang_crawler/lambda_function.py ./
COPY namsigdang_crawler/slack.py ./
COPY namsigdang_crawler/constants/*.py ./constants/
COPY namsigdang_crawler/data/account/*.py ./data/account/
COPY namsigdang_crawler/data/account/namsigdang-crawler-firebase-adminsdk-fbsvc-c3f9e3e036_namsigdang-crawler.json ./data/account/

RUN mkdir -p ./data/log ./data/crawling_menu

CMD ["lambda_function.lambda_handler"]

# docker build -f aws_lambda_env/Dockerfile --tag aws-lambda-namsigdang-crawler:1.0 .
