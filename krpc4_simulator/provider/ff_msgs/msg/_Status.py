# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/Status.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ff_msgs.msg

class Status(genpy.Message):
  _md5sum = "ce2a77030078d6182709c37909b7659f"
  _type = "ff_msgs/Status"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Copyright (c) 2017, United States Government, as represented by the
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
# Sub-type for a command's status in a PlanStatus' history.

int32 point                         # Station or segment
int32 command                       # Subcommand within station/segment or -1
int32 duration                      # How long it took
ff_msgs/AckCompletedStatus status   # The completion status

================================================================================
MSG: ff_msgs/AckCompletedStatus
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
# Completed command status. Based on AckCompletedStatus from RAPID DDS

uint8 NOT = 0           # Command not completed
uint8 OK = 1            # Command completed successfully
uint8 BAD_SYNTAX = 2    # Command not recognized, bad parameters, etc.
uint8 EXEC_FAILED = 3   # Command failed to execute
uint8 CANCELED = 4      # Command was canceled by operator

# Completed command status
uint8 status
"""
  __slots__ = ['point','command','duration','status']
  _slot_types = ['int32','int32','int32','ff_msgs/AckCompletedStatus']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       point,command,duration,status

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Status, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.point is None:
        self.point = 0
      if self.command is None:
        self.command = 0
      if self.duration is None:
        self.duration = 0
      if self.status is None:
        self.status = ff_msgs.msg.AckCompletedStatus()
    else:
      self.point = 0
      self.command = 0
      self.duration = 0
      self.status = ff_msgs.msg.AckCompletedStatus()

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
      buff.write(_get_struct_3iB().pack(_x.point, _x.command, _x.duration, _x.status.status))
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
      if self.status is None:
        self.status = ff_msgs.msg.AckCompletedStatus()
      end = 0
      _x = self
      start = end
      end += 13
      (_x.point, _x.command, _x.duration, _x.status.status,) = _get_struct_3iB().unpack(str[start:end])
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
      buff.write(_get_struct_3iB().pack(_x.point, _x.command, _x.duration, _x.status.status))
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
      if self.status is None:
        self.status = ff_msgs.msg.AckCompletedStatus()
      end = 0
      _x = self
      start = end
      end += 13
      (_x.point, _x.command, _x.duration, _x.status.status,) = _get_struct_3iB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3iB = None
def _get_struct_3iB():
    global _struct_3iB
    if _struct_3iB is None:
        _struct_3iB = struct.Struct("<3iB")
    return _struct_3iB
