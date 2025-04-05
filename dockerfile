FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:xtradeb/apps \
    && apt-get update \
    && apt-get install -y \
    ungoogled-chromium \
    chromium-chromedriver \
    libnss3 \
    libgbm1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    libxshmfence1 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install selenium webdriver-manager beautifulsoup4

COPY all_git_passes.py /app/all_git_passes.py
COPY pythoncode_one.py /app/pythoncode_one.py
COPY pythoncode_one.py /app/pythoncode_two.py
COPY pythoncode_one.py /app/pythoncode_three.py
COPY pythoncode_one.py /app/pythoncode_four.py
COPY pythoncode_one.py /app/pythoncode_five.py
COPY pythoncode_one.py /app/pythoncode_six.py
COPY pythoncode_one.py /app/pythoncode_seven.py
COPY pythoncode_one.py /app/pythoncode_eight.py
COPY pythoncode_one.py /app/pythoncode_nine.py
COPY pythoncode_one.py /app/pythoncode_ten.py
COPY pythoncode_one.py /app/pythoncode_eleven.py
COPY pythoncode_one.py /app/pythoncode_twelve.py
COPY pythoncode_one.py /app/pythoncode_rebirth.py
COPY pythoncode_one.py /app/pythoncode_die.py

# Set working directory
WORKDIR /app
