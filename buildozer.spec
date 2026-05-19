[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain
package.domain = org.example

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf,otf

# (list) Directories to exclude
source.exclude_dirs = .git,__pycache__,bin,.buildozer,venv,env

# (list) Files to exclude
source.exclude_exts = spec,pyc,pyo

# (str) Version
version = 1.0

# (list) Application requirements
requirements = python3==3.11.9,kivy==2.3.1,kivymd==1.2.0,pillow==10.4.0,requests,urllib3,certifi,charset-normalizer,idna,filetype,docutils,Pygments

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Android API
android.api = 34

# (int) Minimum API
android.minapi = 24

# (int) Android SDK
android.sdk = 34

# (str) Android NDK
android.ndk = 25b

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (bool) Enable AndroidX
android.enable_androidx = True

# (list) Target architectures
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (str) Debug artifact format
android.debug_artifact = apk

# (str) Release artifact format
android.release_artifact = aab

# (str) Bootstrap
p4a.bootstrap = sdl2

# (bool) Copy libs instead of libpymodules.so
android.copy_libs = 1

# (str) Logcat filters
android.logcat_filters = *:S python:D

# (bool) Show logs only for app PID
android.logcat_pid_only = False

# (str) App theme
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (str) Presplash image
# presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon
# icon.filename = %(source.dir)s/assets/icon.png

# (str) Adaptive icon foreground
# icon.adaptive_foreground.filename = %(source.dir)s/assets/icon_fg.png

# (str) Adaptive icon background
# icon.adaptive_background.filename = %(source.dir)s/assets/icon_bg.png

#
# Python for Android
#

# (str) Bootstrap
# p4a.bootstrap = sdl2

# (bool) Use setup.py
p4a.setup_py = false

#
# iOS specific
#

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2

ios.codesign.allowed = false

#
# Buildozer settings
#

[buildozer]

# (int) Log level
log_level = 2

# (bool) Warn on root
warn_on_root = 1

# (str) Build directory
build_dir = ./.buildozer

# (str) Bin directory
bin_dir = ./bin
