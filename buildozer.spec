
[app]
title = Zuoyou Game
package.name = zuoyougame
package.domain = org.example
source.dir = .
source.include_exts = py, wav, mp3, jpg, png, json, ttf
version = 1.0.0
main.py = zuoyou_game.py
requirements = python3, pygame, sdl2, pygame_sdl2, pyjnius
orientation = landscape
fullscreen = 1
include_patterns = *.wav, *.ttf, *.json
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
