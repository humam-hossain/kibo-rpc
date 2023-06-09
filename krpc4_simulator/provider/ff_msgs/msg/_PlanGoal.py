# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/PlanGoal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import geometry_msgs.msg
import std_msgs.msg

class PlanGoal(genpy.Message):
  _md5sum = "8a3c023dc4c031730a0eb5ee3812c31e"
  _type = "ff_msgs/PlanGoal"
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
# This message describes the PLAN action offered by the PLANNER

geometry_msgs/PoseStamped[] states            # Desired state sequence

bool faceforward                              # Face-forward trajectory?
bool check_obstacles                          # Check against obstacles?

float32 desired_vel                           # Desired (max) velocity
float32 desired_accel                         # Desired (max) accel
float32 desired_omega                         # Desired (max) omega
float32 desired_alpha                         # Desired (max) alpha
float32 desired_rate                          # Desired rate

duration max_time                             # Max generation time


================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

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

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['states','faceforward','check_obstacles','desired_vel','desired_accel','desired_omega','desired_alpha','desired_rate','max_time']
  _slot_types = ['geometry_msgs/PoseStamped[]','bool','bool','float32','float32','float32','float32','float32','duration']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       states,faceforward,check_obstacles,desired_vel,desired_accel,desired_omega,desired_alpha,desired_rate,max_time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PlanGoal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.states is None:
        self.states = []
      if self.faceforward is None:
        self.faceforward = False
      if self.check_obstacles is None:
        self.check_obstacles = False
      if self.desired_vel is None:
        self.desired_vel = 0.
      if self.desired_accel is None:
        self.desired_accel = 0.
      if self.desired_omega is None:
        self.desired_omega = 0.
      if self.desired_alpha is None:
        self.desired_alpha = 0.
      if self.desired_rate is None:
        self.desired_rate = 0.
      if self.max_time is None:
        self.max_time = genpy.Duration()
    else:
      self.states = []
      self.faceforward = False
      self.check_obstacles = False
      self.desired_vel = 0.
      self.desired_accel = 0.
      self.desired_omega = 0.
      self.desired_alpha = 0.
      self.desired_rate = 0.
      self.max_time = genpy.Duration()

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
      length = len(self.states)
      buff.write(_struct_I.pack(length))
      for val1 in self.states:
        _v1 = val1.header
        _x = _v1.seq
        buff.write(_get_struct_I().pack(_x))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v3 = val1.pose
        _v4 = _v3.position
        _x = _v4
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v5 = _v3.orientation
        _x = _v5
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_get_struct_2B5f2i().pack(_x.faceforward, _x.check_obstacles, _x.desired_vel, _x.desired_accel, _x.desired_omega, _x.desired_alpha, _x.desired_rate, _x.max_time.secs, _x.max_time.nsecs))
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
      if self.states is None:
        self.states = None
      if self.max_time is None:
        self.max_time = genpy.Duration()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.states = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.PoseStamped()
        _v6 = val1.header
        start = end
        end += 4
        (_v6.seq,) = _get_struct_I().unpack(str[start:end])
        _v7 = _v6.stamp
        _x = _v7
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v6.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v6.frame_id = str[start:end]
        _v8 = val1.pose
        _v9 = _v8.position
        _x = _v9
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v10 = _v8.orientation
        _x = _v10
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.states.append(val1)
      _x = self
      start = end
      end += 30
      (_x.faceforward, _x.check_obstacles, _x.desired_vel, _x.desired_accel, _x.desired_omega, _x.desired_alpha, _x.desired_rate, _x.max_time.secs, _x.max_time.nsecs,) = _get_struct_2B5f2i().unpack(str[start:end])
      self.faceforward = bool(self.faceforward)
      self.check_obstacles = bool(self.check_obstacles)
      self.max_time.canon()
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
      length = len(self.states)
      buff.write(_struct_I.pack(length))
      for val1 in self.states:
        _v11 = val1.header
        _x = _v11.seq
        buff.write(_get_struct_I().pack(_x))
        _v12 = _v11.stamp
        _x = _v12
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v11.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v13 = val1.pose
        _v14 = _v13.position
        _x = _v14
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v15 = _v13.orientation
        _x = _v15
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_get_struct_2B5f2i().pack(_x.faceforward, _x.check_obstacles, _x.desired_vel, _x.desired_accel, _x.desired_omega, _x.desired_alpha, _x.desired_rate, _x.max_time.secs, _x.max_time.nsecs))
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
      if self.states is None:
        self.states = None
      if self.max_time is None:
        self.max_time = genpy.Duration()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.states = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.PoseStamped()
        _v16 = val1.header
        start = end
        end += 4
        (_v16.seq,) = _get_struct_I().unpack(str[start:end])
        _v17 = _v16.stamp
        _x = _v17
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v16.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v16.frame_id = str[start:end]
        _v18 = val1.pose
        _v19 = _v18.position
        _x = _v19
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v20 = _v18.orientation
        _x = _v20
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.states.append(val1)
      _x = self
      start = end
      end += 30
      (_x.faceforward, _x.check_obstacles, _x.desired_vel, _x.desired_accel, _x.desired_omega, _x.desired_alpha, _x.desired_rate, _x.max_time.secs, _x.max_time.nsecs,) = _get_struct_2B5f2i().unpack(str[start:end])
      self.faceforward = bool(self.faceforward)
      self.check_obstacles = bool(self.check_obstacles)
      self.max_time.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B5f2i = None
def _get_struct_2B5f2i():
    global _struct_2B5f2i
    if _struct_2B5f2i is None:
        _struct_2B5f2i = struct.Struct("<2B5f2i")
    return _struct_2B5f2i
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
