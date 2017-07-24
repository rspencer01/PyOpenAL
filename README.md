# python-openal

python-openal provides OpenAL bindings for python as well as an interface to them.

You can even open OGG VORBIS and OGG OPUS files when you also have PyOgg https://github.com/Zuzu-Typ/PyOgg

Documentation will follow.

For now:
There are classes for Listener, Source and Buffer.

All of python-openal's own functions have the prefix "oal", here's a small sample list:
oalInit() // it initializes automatically (unless OAL_DONT_AUTO_INIT is set)
oalLoadFile(filepath [,extension_hint]) // returns a Source object (this function requires PyOgg)
oalGetListener() // returns a Listener object that can be used to change OpenAL's listener's position, orientation ,etc.