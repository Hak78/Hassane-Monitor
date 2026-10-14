[app]
title = Hassane Monitor
package.name = hassanemonitor
package.domain = com.hak78.hassanemonitor
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
