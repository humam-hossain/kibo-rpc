# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/ArmGoal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ArmGoal(genpy.Message):
  _md5sum = "2132b678d6b320fdf79bc08b99d42769"
  _type = "ff_msgs/ArmGoal"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
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
# This message describes the ARM action offered by the PERCHING ARM

uint8 command                                 # What to do
uint8 ARM_STOP            = 0                 # Stop the arm (vel = 0)
uint8 ARM_DEPLOY          = 1                 # Deploy the arm
uint8 ARM_STOW            = 2                 # Retract the arm
uint8 ARM_PAN             = 3                 # Pan the arm
uint8 ARM_TILT            = 4                 # Tilt the arm
uint8 ARM_MOVE            = 5                 # Pan and tilt the
uint8 GRIPPER_SET         = 6                 # Set the gripper value
uint8 GRIPPER_OPEN        = 7                 # Open the gripper
uint8 GRIPPER_CLOSE       = 8                 # Close the gripper
uint8 DISABLE_SERVO       = 9                 # Disable the servos

float32 pan                                   # PAN from -90 to +90
float32 tilt                                  # TILT from -120 to +90
float32 gripper                               # SET from 20 to 45

"""
  # Pseudo-constants
  ARM_STOP = 0
  ARM_DEPLOY = 1
  ARM_STOW = 2
  ARM_PAN = 3
  ARM_TILT = 4
  ARM_MOVE = 5
  GRIPPER_SET = 6
  GRIPPER_OPEN = 7
  GRIPPER_CLOSE = 8
  DISABLE_SERVO = 9

  __slots__ = ['command','pan','tilt','gripper']
  _slot_types = ['uint8','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       command,pan,tilt,gripper

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ArmGoal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.command is None:
        self.command = 0
      if self.pan is None:
        self.pan = 0.
      if self.tilt is None:
        self.tilt = 0.
      if self.gripper is None:
        self.gripper = 0.
    else:
      self.command = 0
      self.pan = 0.
      self.tilt = 0.
      self.gripper = 0.

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
      buff.write(_get_struct_B3f().pack(_x.command, _x.pan, _x.tilt, _x.gripper))
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
      _x = self
      start = end
      end += 13
      (_x.command, _x.pan, _x.tilt, _x.gripper,) = _get_struct_B3f().unpack(str[start:end])
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
      buff.write(_get_struct_B3f().pack(_x.command, _x.pan, _x.tilt, _x.gripper))
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
      _x = self
      start = end
      end += 13
      (_x.command, _x.pan, _x.tilt, _x.gripper,) = _get_struct_B3f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B3f = None
def _get_struct_B3f():
    global _struct_B3f
    if _struct_B3f is None:
        _struct_B3f = struct.Struct("<B3f")
    return _struct_B3f
