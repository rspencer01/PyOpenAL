from ._al import *
from ._alc import *

import ctypes

import os, sys

import traceback ## remove later

try:
    from pyogg import *
    PYOGG_AVAIL = True
except ImportError:
    PYOGG_AVAIL = False

try:
    OAL_DONT_AUTO_INIT
except:
    OAL_DONT_AUTO_INIT = False

__name__ = "python-openal"

MAX_FLOAT = sys.float_info.max

class OalError(Exception):
    pass

def _err(msg):
    raise OalError(msg)

class vec6:
    def __init__(self, *args):
        if len(args) == 6:
            self.x = float(args[0])
            self.y = float(args[1])
            self.z = float(args[2])
            self.a = float(args[3])
            self.b = float(args[4])
            self.c = float(args[5])
            
        elif len(args) == 1 and type(args[0]) in (ctypes.c_float*6, ctypes.c_int*6, tuple):
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
            self.a = args[0][3]
            self.b = args[0][4]
            self.c = args[0][5]
        elif len(args) == 1:
            self.x = args[0].x
            self.y = args[0].y
            self.z = args[0].z
            self.a = args[0].a
            self.b = args[0].b
            self.c = args[0].c
        else:
            self.x = self.y = self.z = self.a = self.b = self.c = 0.
    def __add__(self, *args):
        x = self.x
        y = self.y
        z = self.z
        a = self.a
        b = self.b
        c = self.c
        if len(args) == 6:
            x += float(args[0])
            y += float(args[1])
            z += float(args[2])
            a += float(args[3])
            b += float(args[4])
            c += float(args[5])
            
        elif len(args) == 1 and type(args[0]) in (ctypes.c_float*6, ctypes.c_int*6, tuple):
            x += args[0][0]
            y += args[0][1]
            z += args[0][2]
            a += args[0][3]
            b += args[0][4]
            c += args[0][5]
        elif len(args) == 1 and type(args[0]) in (int, float):
            x += args[0]
            y += args[0]
            z += args[0]
            a += args[0]
            b += args[0]
            c += args[0]
        else:
            x += args[0].x
            y += args[0].y
            z += args[0].z
            a += args[0].a
            b += args[0].b
            c += args[0].c
        return (x,y,z, a, b, c)
    def __mul__(self, *args):
        x = self.x
        y = self.y
        z = self.z
        a = self.a
        b = self.b
        c = self.c
        if len(args) == 6:
            x *= float(args[0])
            y *= float(args[1])
            z *= float(args[2])
            a *= float(args[3])
            b *= float(args[4])
            c *= float(args[5])
            
        elif len(args) == 1 and type(args[0]) in (ctypes.c_float*6, ctypes.c_int*6, tuple):
            x *= args[0][0]
            y *= args[0][1]
            z *= args[0][2]
            a *= args[0][3]
            b *= args[0][4]
            c *= args[0][5]
        elif len(args) == 1 and type(args[0]) in (int, float):
            x *= args[0]
            y *= args[0]
            z *= args[0]
            a *= args[0]
            b *= args[0]
            c *= args[0]
        else:
            x *= args[0].x
            y *= args[0].y
            z *= args[0].z
            a *= args[0].a
            b *= args[0].b
            c *= args[0].c
        return (x,y,z, a, b, c)
    def __sub__(self, *args):
        x = self.x
        y = self.y
        z = self.z
        a = self.a
        b = self.b
        c = self.c
        if len(args) == 6:
            x -= float(args[0])
            y -= float(args[1])
            z -= float(args[2])
            a -= float(args[3])
            b -= float(args[4])
            c -= float(args[5])
            
        elif len(args) == 1 and type(args[0]) in (ctypes.c_float*6, ctypes.c_int*6, tuple):
            x -= args[0][0]
            y -= args[0][1]
            z -= args[0][2]
            a -= args[0][3]
            b -= args[0][4]
            c -= args[0][5]
        elif len(args) == 1 and type(args[0]) in (int, float):
            x -= args[0]
            y -= args[0]
            z -= args[0]
            a -= args[0]
            b -= args[0]
            c -= args[0]
        else:
            x -= args[0].x
            y -= args[0].y
            z -= args[0].z
            a -= args[0].a
            b -= args[0].b
            c -= args[0].c
        return (x,y,z)
    def __div__(self, *args):
        x = self.x
        y = self.y
        z = self.z
        a = self.a
        b = self.b
        c = self.c
        if len(args) == 6:
            x /= float(args[0])
            y /= float(args[1])
            z /= float(args[2])
            a /= float(args[3])
            b /= float(args[4])
            c /= float(args[5])
            
        elif len(args) == 1 and type(args[0]) in (ctypes.c_float*6, ctypes.c_int*6, tuple):
            x /= args[0][0]
            y /= args[0][1]
            z /= args[0][2]
            a /= args[0][3]
            b /= args[0][4]
            c /= args[0][5]
        elif len(args) == 1 and type(args[0]) in (int, float):
            x /= args[0]
            y /= args[0]
            z /= args[0]
            a /= args[0]
            b /= args[0]
            c /= args[0]
        else:
            x /= args[0].x
            y /= args[0].y
            z /= args[0].z
            a /= args[0].a
            b /= args[0].b
            c /= args[0].c
        return (x,y,z,a,b,c)
    def __iadd__(self, *args):
        self.x, self.y, self.z, self.a, self.b, self.c = self.__add__(*args)
        return self
    def __isub__(self, *args):
        self.x, self.y, self.z, self.a, self.b, self.c = self.__sub__(*args)
        return self
    def __imul__(self, *args):
        self.x, self.y, self.z, self.a, self.b, self.c = self.__mul__(*args)
        return self
    def __idiv__(self, *args):
        self.x, self.y, self.z, self.a, self.b, self.c = self.__div__(*args)
        return self
    def __str__(self):
        return "vec6( {} , {} , {} , {} , {} , {})".format(self.x, self.y, self.z, self.a, self.b, self.c)

    def asTuple(self):
        return (self.x, self.y, self.z, self.a, self.b, self.c )

    def asCTuple(self):
        return (ctypes.c_float*6)(*self.asTuple())

class vec3:
    def __init__(self, *args):
        if len(args) == 3:
            self.x = float(args[0])
            self.y = float(args[1])
            self.z = float(args[2])
            
        elif len(args) == 1 and type(args[0]) in (ctypes.c_float*3, ctypes.c_int*3, tuple):
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
        elif len(args) == 1:
            self.x = args[0].x
            self.y = args[0].y
            self.z = args[0].z
        else:
            self.x = self.y = self.z = 0.
    def __add__(self, *args):
        x = self.x
        y = self.y
        z = self.z
        if len(args) == 3:
            x += float(args[0])
            y += float(args[1])
            z += float(args[2])
            
        elif len(args) == 1 and type(args[0]) in (ctypes.c_float*3, ctypes.c_int*3, tuple):
            x += args[0][0]
            y += args[0][1]
            z += args[0][2]
        elif len(args) == 1 and type(args[0]) in (int, float):
            x += args[0]
            y += args[0]
            z += args[0]
        else:
            x += args[0].x
            y += args[0].y
            z += args[0].z
        return (x,y,z)
    def __mul__(self, *args):
        x = self.x
        y = self.y
        z = self.z
        if len(args) == 3:
            x *= float(args[0])
            y *= float(args[1])
            z *= float(args[2])
            
        elif len(args) == 1 and type(args[0]) in (ctypes.c_float*3, ctypes.c_int*3, tuple):
            x *= args[0][0]
            y *= args[0][1]
            z *= args[0][2]
        elif len(args) == 1 and type(args[0]) in (int, float):
            x *= args[0]
            y *= args[0]
            z *= args[0]
        else:
            x *= args[0].x
            y *= args[0].y
            z *= args[0].z
        return (x,y,z)
    def __sub__(self, *args):
        x = self.x
        y = self.y
        z = self.z
        if len(args) == 3:
            x -= float(args[0])
            y -= float(args[1])
            z -= float(args[2])
            
        elif len(args) == 1 and type(args[0]) in (ctypes.c_float*3, ctypes.c_int*3, tuple):
            x -= args[0][0]
            y -= args[0][1]
            z -= args[0][2]
        elif len(args) == 1 and type(args[0]) in (int, float):
            x -= args[0]
            y -= args[0]
            z -= args[0]
        else:
            x -= args[0].x
            y -= args[0].y
            z -= args[0].z
        return (x,y,z)
    def __div__(self, *args):
        x = self.x
        y = self.y
        z = self.z
        if len(args) == 3:
            x /= float(args[0])
            y /= float(args[1])
            z /= float(args[2])
            
        elif len(args) == 1 and type(args[0]) in (ctypes.c_float*3, ctypes.c_int*3, tuple):
            x /= args[0][0]
            y /= args[0][1]
            z /= args[0][2]
        elif len(args) == 1 and type(args[0]) in (int, float):
            x /= args[0]
            y /= args[0]
            z /= args[0]
        else:
            x /= args[0].x
            y /= args[0].y
            z /= args[0].z
        return (x,y,z)
    def __iadd__(self, *args):
        self.x, self.y, self.z = self.__add__(*args)
        return self
    def __isub__(self, *args):
        self.x, self.y, self.z = self.__sub__(*args)
        return self
    def __imul__(self, *args):
        self.x, self.y, self.z = self.__mul__(*args)
        return self
    def __idiv__(self, *args):
        self.x, self.y, self.z = self.__div__(*args)
        return self
    def __str__(self):
        return "vec3( {} , {} , {} )".format(self.x,self.y,self.z)

    def asTuple(self):
        return (self.x,self.y,self.z)

    def asCTuple(self):
        return (ctypes.c_float*3)(*self.asTuple())

_oaldevice = None

_oalcontext = None

def oalInit():
    """Sets up OpenAL device and context (if not yet created)"""
    global _oaldevice, _oalcontext
    
    if not _oaldevice:
        _oaldevice = alcOpenDevice(None)
        
    if not _oaldevice:
        raise OalError("Default OpenAL device couldn't be opened")

    if not _oalcontext:
        _oalcontext = alcCreateContext(_oaldevice, None)
        
    if not _oalcontext:
        raise OalError("OpenAL context couldn't be created")

    alcMakeContextCurrent(_oalcontext)

def oalGetDevice():
    """Returns the OpenAL device oal is using"""
    global _oaldevice
    return _oaldevice

def oalGetContext():
    """Returns the OpenAL context oal is using"""
    global _oalcontext
    return _oalcontext

def oalGetInit():
    global _oaldevice, _oalcontext

    return bool(_oaldevice) and bool(_oalcontext)

def _nlError():
    _err("{} wasn't loaded yet, please run oalInit() first".format(__name__))

def _check():
    if not oalGetInit():
        if OAL_DONT_AUTO_INIT:
            _nlError()
        else:
            oalInit()

def _no_pyogg_error(*args, **kw):
    _err("You have to set up pyogg in order to use this function. Go to https://github.com/Zuzu-Typ/PyOgg to get it")

class Listener:
    def __init__(self):
        self.gain = 0.
        self.position = vec3(0.,0.,0.)
        self.orientation = vec6(0.,0.,-1.,0.,1.,0.)
        self.velocity = vec3(0.,0.,0.)

    def _setPos(self):
        _check()
        alListenerfv(AL_POSITION, self.position.asCTuple())

    def _setGain(self):
        _check()
        alListenerf(AL_GAIN, ctypes.c_float(self.gain))

    def _setOrientation(self):
        _check()
        alListenerfv(AL_ORIENTATION, self.orientation.asCTuple())

    def _setVelocity(self):
        _check()
        alListenerfv(AL_VELOCITY, self.velocity.asCTuple())

    def move(self, v):
        try:
            self.position += v
            self._setPos()
        except:
            raise OalError("Unsupported argument for move: {}".format(v))

    def move_to(self, v):
        try:
            self.position = vec3(v)
            self._setPos()
        except:
            raise OalError("Unsupported argument for move_to: {}".format(v))

    def set_position(self,v):
        try:
            self.position = vec3(v)
            self._setPos()
        except:
            raise OalError("Unsupported argument for set_position: {}".format(v))

    def set_orientation(self,v):
        try:
            self.orientation = vec6(v)
            self._setOrientation()
        except:
            raise OalError("Unsupported argument for set_orientation: {}".format(v))

    def set_velocity(self, v):
        try:
            self.velocity = vec3(v)
            self._setVelocity()
        except:
            raise OalError("Unsupported argument for set_velocity: {}".format(v))

    def set_gain(self, value):
        try:
            self.gain = value
            self._setGain()
        except:
            raise OalError("Unsupported argument for set_gain: {}".format(value))

_listener = Listener()

def _to_int(i):
    if type(i) == int:
        return i
    elif type(i) in (ctypes.c_int, ctypes.c_char):
        return i.value

def _to_c_int(i):
    if type(i) == int:
        return ctypes.c_int(i)
    elif type(i) in (ctypes.c_uint, ctypes.c_char):
        return ctypes.c_int(i.value)

def _channels_to_al(ch):
    if ch == 1:
        return(ctypes.c_int(AL_FORMAT_MONO16))
    elif ch == 2:
        return(ctypes.c_int(AL_FORMAT_STEREO16))

class Buffer:
    def __init__(self, *args):
        _check()
        self.id = ctypes.c_uint()
        alGenBuffers(1, ctypes.pointer(self.id))

        self.fill(*args)

    def geti(self):
        return ctypes.c_int(self.id.value)

    def getui(self):
        return self.id

    def fill(self, *args):
        if PYOGG_AVAIL and len(args) == 1:
            file_ = args[0]
            alBufferData(self.getui(), _channels_to_al(file_.channels), file_.buffer, _to_c_int(file_.buffer_length), _to_c_int(file_.frequency))
        else:
            alBufferData(self.getui(), _to_int(args[0]), args[1], _to_int(args[2]), _to_int(args[3]))

class Source:
    def __init__(self, buffer_ = None):
        _check()
        self.id = ctypes.c_uint()
        alGenSources(1, ctypes.pointer(self.id))

        self.pitch = 1.

        self.gain = 1.

        self.max_distance = MAX_FLOAT

        self.rolloff_factor = 1.

        self.reference_distance = 1.

        self.min_gain = 0.

        self.max_gain = 1.

        self.cone_outer_gain = 0.

        self.cone_inner_angle = 360.

        self.cone_outer_angle = 360.

        self.position = vec3(0.,0.,0.)

        self.velocity = vec3(0.,0.,0.)

        self.looping = False

        self.direction = vec3(0.,0.,0.)

        self.source_relative = False

        self.source_type = AL_UNDETERMINED

        self.buffers_queued = None

        self.buffers_processed = None

        if buffer_:
            self.set_buffer(buffer_)

    def geti(self):
        return ctypes.c_int(self.id.value)

    def getui(self):
        return self.id

    def set_buffer(self, buffer_):
        self.buffer = buffer_

        alSourcei(self.id, AL_BUFFER, self.buffer.geti())

    def play(self):
        alSourcePlay(self.id)

    def stop(self):
        alSourceStop(self.id)

    def pause(self):
        alSourcePause(self.id)

    def rewind(self):
        alSourceRewind(self.id)
        

def oalGetListener():
    global _listener
    return _listener

if PYOGG_AVAIL:
    def oalLoadFile(path, ext_hint=None):
        """oalLoadFile(filepath [, extension_hint]) -> Source
        loads an ogg file to a source and returns it.
        You can use ext_hint to suggest the file type,
        in case the file extension is not ogg, vorbis or opus"""
        _check()
        if not ext_hint:
            ext_hint = os.path.splitext(path)[1]
        ext_hint = ext_hint.lower()
        if ext_hint in ("ogg", "vorbis", ".ogg", ".vorbis"):
            file_ = VorbisFile(path)
        elif ext_hint in ("opus", ".opus"):
            file_ = OpusFile(path)
        else:
            _err("Unsupported file extension {}. You might want to consider using the ext_hint parameter to pass the file format".format(ext_hint))
            
        buffer_ = Buffer(file_)

        source = Source(buffer_)

        return source

else:
    oalLoadFile = _no_pyogg_error
