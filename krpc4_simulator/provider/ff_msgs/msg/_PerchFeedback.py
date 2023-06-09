# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/PerchFeedback.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ff_msgs.msg
import std_msgs.msg

class PerchFeedback(genpy.Message):
  _md5sum = "ce91b2c26500c663aeec651c3bf03ceb"
  _type = "ff_msgs/PerchFeedback"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

# Feedback
ff_msgs/PerchState state


================================================================================
MSG: ff_msgs/PerchState
# Copyright (c) 2017, United States Government, as represented by the
# Administrator of the National Aeronautics and Space Administration.
#
# All rights reserved.
#
# The Astrobee platform is licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# The state of the perching system

# Header with timestamp
std_msgs/Header header

# Feedback
int8 state

int8 RECOVERY_MOVING_TO_RECOVERY_POSE   = 18
int8 RECOVERY_SWITCHING_TO_ML_LOC       = 17
int8 RECOVERY_STOWING_ARM               = 16
int8 RECOVERY_MOVING_TO_APPROACH_POSE   = 15
int8 RECOVERY_OPENING_GRIPPER           = 14
int8 INITIALIZING                       = 13
int8 UNKNOWN                            = 12
# Used to check the perching/unperching ranges
int8 PERCHING_MAX_STATE                 = 11
int8 PERCHING_SWITCHING_TO_HR_LOC       = 11
int8 PERCHING_MOVING_TO_APPROACH_POSE   = 10
int8 PERCHING_ENSURING_APPROACH_POSE    = 9
int8 PERCHING_DEPLOYING_ARM             = 8
int8 PERCHING_OPENING_GRIPPER           = 7
int8 PERCHING_MOVING_TO_COMPLETE_POSE   = 6
int8 PERCHING_CLOSING_GRIPPER           = 5
int8 PERCHING_CHECKING_ATTACHED         = 4
int8 PERCHING_WAITING_FOR_SPIN_DOWN     = 3
int8 PERCHING_SWITCHING_TO_PL_LOC       = 2
int8 PERCHING_STOPPING                  = 1
int8 PERCHED                            = 0
int8 UNPERCHING_SWITCHING_TO_HR_LOC     = -1
int8 UNPERCHING_WAITING_FOR_SPIN_UP     = -2
int8 UNPERCHING_OPENING_GRIPPER         = -3
int8 UNPERCHING_MOVING_TO_APPROACH_POSE = -4
int8 UNPERCHING_STOWING_ARM             = -5
int8 UNPERCHING_SWITCHING_TO_ML_LOC     = -6
int8 UNPERCHED                          = -7
# Used to check the perching/unperching ranges
int8 UNPERCHING_MAX_STATE               = -7

# A human readable version of the (event) -> [state] transition
string fsm_event
string fsm_state

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['state']
  _slot_types = ['ff_msgs/PerchState']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       state

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PerchFeedback, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.state is None:
        self.state = ff_msgs.msg.PerchState()
    else:
      self.state = ff_msgs.msg.PerchState()

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
      _x = self
      buff.write(_get_struct_3I().pack(_x.state.header.seq, _x.state.header.stamp.secs, _x.state.header.stamp.nsecs))
      _x = self.state.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state.state
      buff.write(_get_struct_b().pack(_x))
      _x = self.state.fsm_event
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state.fsm_state
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
      if self.state is None:
        self.state = ff_msgs.msg.PerchState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.state.header.seq, _x.state.header.stamp.secs, _x.state.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state.header.frame_id = str[start:end]
      start = end
      end += 1
      (self.state.state,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state.fsm_event = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state.fsm_event = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state.fsm_state = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state.fsm_state = str[start:end]
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
      _x = self
      buff.write(_get_struct_3I().pack(_x.state.header.seq, _x.state.header.stamp.secs, _x.state.header.stamp.nsecs))
      _x = self.state.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state.state
      buff.write(_get_struct_b().pack(_x))
      _x = self.state.fsm_event
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.state.fsm_state
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
      if self.state is None:
        self.state = ff_msgs.msg.PerchState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.state.header.seq, _x.state.header.stamp.secs, _x.state.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state.header.frame_id = str[start:end]
      start = end
      end += 1
      (self.state.state,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state.fsm_event = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state.fsm_event = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state.fsm_state = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.state.fsm_state = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
