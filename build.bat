set appVersion="1.0.0"

pyinstaller -w main.py -y

robocopy .meta dist/main\.meta /E


IF EXIST .releases\%appVersion% (
    rmdir /S /Q .releases\%appVersion%
)
mkdir .releases\%appVersion%

ISCC install.iss /DMyAppVersion=%appVersion%