To check out the applications visit https://www.stuffbyyc.com/ go to the download section
# Kivy_Calculator

Requirements
```cmd
python -m pip install --upgrade pip wheel setuptools
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer
python -m pip install kivy.deps.angle
python -m pip install pygame
python -m pip install kivy
```
## ---------------To Create android Application from Kivy-----------------
```cmd
$ git clone https://github.com/kivy/buildozer.git
$ cd buildozer
$ sudo python setup.py install
```
Go to the folder where you have you python and kivy file
```cmd
$ buildozer init
```
edit the buildozer.spec, then

1. Change Application title

2. rename your python file to main.py

3. Icon -- Remove comment 
(str) Icon of the application
icon.filename = %(source.dir)s/logo.png

4. Presplash -- Remove comment
(str) Presplash of the application
presplash.filename = %(source.dir)s/logo.png

Run below command to run applications
```cmd
$ buildozer android debug deploy run   
```
additional details : https://kivy.org/doc/stable/guide/packaging-windows.html

## ---------------To Create Windows Application from Kivy-------------
Open CMD in windows 
```cmd
$ pip install PyInstaller
```
Execute below command in the folder where your python, kivy and logo file are present
```cmd
$ PyInstaller --name Calculator@stuffbyyc --icon logo.ico -w main.py
```
Edit Collect in Calculator@stuffbyyc.spec file 
Create a Folder named Final

Add below statement to the coll:
1. Tree('Final\\')
2. *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)]

```python
The coll will after adding statements
coll = COLLECT(exe, Tree('Final\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='Calculator@stuffbyyc')
```              
Excute command
```cmd
PyInstaller Calculator@stuffbyyc.spec
```
You can pack you application using Nsis tool
additional details : https://kivy.org/doc/stable/guide/packaging-android.html

## ---------------To Create iOS Application from Kivy-----------------

https://kivy.org/doc/stable/guide/packaging-ios.html

## ---------------To Create OS X Application from Kivy-----------------

https://kivy.org/doc/stable/guide/packaging-osx.html


## -------------Applications--------------------------
https://www.stuffbyyc.com/ 
Android : https://www.amazon.com/gp/product/B085RZMF6T
Windows : http://wix.to/xsD9CEc
