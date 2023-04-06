# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/ArmResult.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ArmResult(genpy.Message):
  _md5sum = "5c229b93f1064b9f1f7e8f3320eff359"
  _type = "ff_msgs/ArmResult"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

# Machine-readable reseult code
int32 response
int32 SUCCESS             =  1                # Successfully completed
int32 PREEMPTED           =  0                # Action was preempted
int32 INVALID_COMMAND     = -1                # Invalid command
int32 BAD_TILT_VALUE      = -2                # Invalid value for tilt
int32 BAD_PAN_VALUE       = -3                # Invalid value for pan
int32 BAD_GRIPPER_VALUE   = -4                # Invalid value for gripper
int32 NOT_ALLOWED         = -5                # Not allowed
int32 TILT_FAILED         = -6                # Tilt command failed
int32 PAN_FAILED          = -7                # Pan command failed
int32 GRIPPER_FAILED      = -8                # Gripper command failed
int32 COMMUNICATION_ERROR = -9                # Cannot communicate with arm
int32 COLLISION_AVOIDED   = -10               # No panning when tilt < 90
int32 ENABLE_FAILED       = -11               # Cannot enable the servos
int32 DISABLE_FAILED      = -12               # Cannot disable the servos
int32 CALIBRATE_FAILED    = -13               # Cannot calibrate the gripper
int32 NO_GOAL             = -14               # Unknown call to calibration

# Human readable FSM result for debugging
string fsm_result

"""
  # Pseudo-constants
  SUCCESS = 1
  PREEMPTED = 0
  INVALID_COMMAND = -1
  BAD_TILT_VALUE = -2
  BAD_PAN_VALUE = -3
  BAD_GRIPPER_VALUE = -4
  NOT_ALLOWED = -5
  TILT_FAILED = -6
  PAN_FAILED = -7
  GRIPPER_FAILED = -8
  COMMUNICATION_ERROR = -9
  COLLISION_AVOIDED = -10
  ENABLE_FAILED = -11
  DISABLE_FAILED = -12
  CALIBRATE_FAILED = -13
  NO_GOAL = -14

  __slots__ = ['response','fsm_result']
  _slot_types = ['int32','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       response,fsm_result

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ArmResult, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.response is None:
        self.response = 0
      if self.fsm_result is None:
        self.fsm_result = ''
    else:
      self.response = 0
      self.fsm_result = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.response
      buff.write(_get_struct_i().pack(_x))
      _x = self.fsm_result
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (self.response,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.fsm_result = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.fsm_result = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.response
      buff.write(_get_struct_i().pack(_x))
      _x = self.fsm_result
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (self.response,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.fsm_result = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.fsm_result = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
