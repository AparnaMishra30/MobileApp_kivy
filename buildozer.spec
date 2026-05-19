[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf,otf
source.exclude_dirs = .git,__pycache__,bin,.buildozer,venv,env
source.exclude_exts = spec,pyc,pyo

version = 1.0

requirements = python3,kivy,kivymd,requests,pillow

orientation = portrait
fullscreen = 0

[android]
android.permissions = INTERNET
android.api = 34
android.minapi = 24
android.ndk = 25b
android.enable_androidx = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

p4a.bootstrap = sdl2
android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1