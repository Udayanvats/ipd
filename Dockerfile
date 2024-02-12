FROM python:3.10.11

WORKDIR /app

# Install X11 dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxi6 libxtst6 libnss3 libcups2 libxrandr2 libasound2 libatk-bridge2.0-0 libgtk-3-0

# Install XQuartz on Mac
# COPY XQuartz-2.8.1.dmg /tmp/
# RUN hdiutil attach /tmp/XQuartz-2.8.1.dmg \
#     && sudo installer -pkg /Volumes/XQuartz-2.8.1/XQuartz.pkg -target / \
#     && hdiutil detach /Volumes/XQuartz-2.8.1

# Set the DISPLAY environment variable
ENV DISPLAY=host.docker.internal:0

RUN pip install dlib.00
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY dependencies /app/dependencies

CMD ["python", "run.py"]