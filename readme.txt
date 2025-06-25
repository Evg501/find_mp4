
работает
pyinstaller --onefile --console --add-data "pack;pack" app.py

pyinstaller --onefile --console ^
    --add-data "pack;pack" ^
    app.py

не работало
pyinstaller --onefile --console --hidden-import=pack --hidden-import=pack.file_lib app.py


