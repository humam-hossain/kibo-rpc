# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/MotionActionFeedback.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import actionlib_msgs.msg
import ff_msgs.msg
import genpy
import geometry_msgs.msg
import std_msgs.msg

class MotionActionFeedback(genpy.Message):
  _md5sum = "5f91d48e530821eb4c3318d980598eba"
  _type = "ff_msgs/MotionActionFeedback"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalStatus status
MotionFeedback feedback

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
MSG: actionlib_msgs/GoalStatus
GoalID goal_id
uint8 status
uint8 PENDING         = 0   # The goal has yet to be processed by the action server
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing
                            #   and has since completed its execution (Terminal State)
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due
                            #    to some failure (Terminal State)
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,
                            #    because the goal was unattainable or invalid (Terminal State)
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing
                            #    and has not yet completed execution
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,
                            #    but the action server has not yet confirmed that the goal is canceled
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing
                            #    and was successfully cancelled (Terminal State)
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be
                            #    sent over the wire by an action server

#Allow for the user to associate a string with GoalStatus for debugging
string text


================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: ff_msgs/MotionFeedback
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

# The state of the teleop command
ff_msgs/MotionState state

# Control progress
ff_msgs/ControlFeedback progress

# Planner progress
float32 perc_complete
float32 secs_remaining


================================================================================
MSG: ff_msgs/MotionState
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
# Locked topic that registers updates to the internal dock state

# Header with timestamp
std_msgs/Header header

# The state of the mobility subsystem
int8 state
int8 INITIALIZING        = 0
int8 IDLE                = 1
int8 STOPPED             = 2
int8 IDLING              = 3
int8 STOPPING            = 4
int8 PREPPING            = 5
int8 BOOTSTRAPPING       = 6
int8 PLANNING            = 7
int8 PREPARING           = 8
int8 CONTROLLING         = 9
int8 REPLANNING          = 10
int8 HALTING             = 11
int8 REPLAN_WAIT         = 12

# A human readble version of the (event) -> [state] transition
string fsm_event
string fsm_state

================================================================================
MSG: ff_msgs/ControlFeedback
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

uint32 index                                # Index being processed

ff_msgs/ControlState setpoint               # Current setpoint

float32 error_position                      # Position error
float32 error_attitude                      # Attitude error
float32 error_velocity                      # Velocity error
float32 error_omega                         # Omega error


================================================================================
MSG: ff_msgs/ControlState
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
# Full state vector containing Time, Pose, Vel, and Accel
# 
# when {time}
# flight_mode {string} - disctates, gains, tolerances, etc.
# pose {Point position, Quaternion orientation}
# twist {Vector3 linear, Vector3 angular}
# accel {Vector3 linear, Vector3 angular}

time when
geometry_msgs/Pose pose
geometry_msgs/Twist twist
geometry_msgs/Twist accel

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

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['header','status','feedback']
  _slot_types = ['std_msgs/Header','actionlib_msgs/GoalStatus','ff_msgs/MotionFeedback']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,status,feedback

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MotionActionFeedback, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.feedback is None:
        self.feedback = ff_msgs.msg.MotionFeedback()
    else:
      self.header = std_msgs.msg.Header()
      self.status = actionlib_msgs.msg.GoalStatus()
      self.feedback = ff_msgs.msg.MotionFeedback()

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs))
      _x = self.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.status.status
      buff.write(_get_struct_B().pack(_x))
      _x = self.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.feedback.state.header.seq, _x.feedback.state.header.stamp.secs, _x.feedback.state.header.stamp.nsecs))
      _x = self.feedback.state.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.feedback.state.state
      buff.write(_get_struct_b().pack(_x))
      _x = self.feedback.state.fsm_event
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.feedback.state.fsm_state
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I19d6f().pack(_x.feedback.progress.index, _x.feedback.progress.setpoint.when.secs, _x.feedback.progress.setpoint.when.nsecs, _x.feedback.progress.setpoint.pose.position.x, _x.feedback.progress.setpoint.pose.position.y, _x.feedback.progress.setpoint.pose.position.z, _x.feedback.progress.setpoint.pose.orientation.x, _x.feedback.progress.setpoint.pose.orientation.y, _x.feedback.progress.setpoint.pose.orientation.z, _x.feedback.progress.setpoint.pose.orientation.w, _x.feedback.progress.setpoint.twist.linear.x, _x.feedback.progress.setpoint.twist.linear.y, _x.feedback.progress.setpoint.twist.linear.z, _x.feedback.progress.setpoint.twist.angular.x, _x.feedback.progress.setpoint.twist.angular.y, _x.feedback.progress.setpoint.twist.angular.z, _x.feedback.progress.setpoint.accel.linear.x, _x.feedback.progress.setpoint.accel.linear.y, _x.feedback.progress.setpoint.accel.linear.z, _x.feedback.progress.setpoint.accel.angular.x, _x.feedback.progress.setpoint.accel.angular.y, _x.feedback.progress.setpoint.accel.angular.z, _x.feedback.progress.error_position, _x.feedback.progress.error_attitude, _x.feedback.progress.error_velocity, _x.feedback.progress.error_omega, _x.feedback.perc_complete, _x.feedback.secs_remaining))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.feedback is None:
        self.feedback = ff_msgs.msg.MotionFeedback()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.goal_id.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.status.status,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.text = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.feedback.state.header.seq, _x.feedback.state.header.stamp.secs, _x.feedback.state.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.state.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.feedback.state.header.frame_id = str[start:end]
      start = end
      end += 1
      (self.feedback.state.state,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.state.fsm_event = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.feedback.state.fsm_event = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.state.fsm_state = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.feedback.state.fsm_state = str[start:end]
      _x = self
      start = end
      end += 188
      (_x.feedback.progress.index, _x.feedback.progress.setpoint.when.secs, _x.feedback.progress.setpoint.when.nsecs, _x.feedback.progress.setpoint.pose.position.x, _x.feedback.progress.setpoint.pose.position.y, _x.feedback.progress.setpoint.pose.position.z, _x.feedback.progress.setpoint.pose.orientation.x, _x.feedback.progress.setpoint.pose.orientation.y, _x.feedback.progress.setpoint.pose.orientation.z, _x.feedback.progress.setpoint.pose.orientation.w, _x.feedback.progress.setpoint.twist.linear.x, _x.feedback.progress.setpoint.twist.linear.y, _x.feedback.progress.setpoint.twist.linear.z, _x.feedback.progress.setpoint.twist.angular.x, _x.feedback.progress.setpoint.twist.angular.y, _x.feedback.progress.setpoint.twist.angular.z, _x.feedback.progress.setpoint.accel.linear.x, _x.feedback.progress.setpoint.accel.linear.y, _x.feedback.progress.setpoint.accel.linear.z, _x.feedback.progress.setpoint.accel.angular.x, _x.feedback.progress.setpoint.accel.angular.y, _x.feedback.progress.setpoint.accel.angular.z, _x.feedback.progress.error_position, _x.feedback.progress.error_attitude, _x.feedback.progress.error_velocity, _x.feedback.progress.error_omega, _x.feedback.perc_complete, _x.feedback.secs_remaining,) = _get_struct_3I19d6f().unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs))
      _x = self.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.status.status
      buff.write(_get_struct_B().pack(_x))
      _x = self.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.feedback.state.header.seq, _x.feedback.state.header.stamp.secs, _x.feedback.state.header.stamp.nsecs))
      _x = self.feedback.state.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.feedback.state.state
      buff.write(_get_struct_b().pack(_x))
      _x = self.feedback.state.fsm_event
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.feedback.state.fsm_state
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I19d6f().pack(_x.feedback.progress.index, _x.feedback.progress.setpoint.when.secs, _x.feedback.progress.setpoint.when.nsecs, _x.feedback.progress.setpoint.pose.position.x, _x.feedback.progress.setpoint.pose.position.y, _x.feedback.progress.setpoint.pose.position.z, _x.feedback.progress.setpoint.pose.orientation.x, _x.feedback.progress.setpoint.pose.orientation.y, _x.feedback.progress.setpoint.pose.orientation.z, _x.feedback.progress.setpoint.pose.orientation.w, _x.feedback.progress.setpoint.twist.linear.x, _x.feedback.progress.setpoint.twist.linear.y, _x.feedback.progress.setpoint.twist.linear.z, _x.feedback.progress.setpoint.twist.angular.x, _x.feedback.progress.setpoint.twist.angular.y, _x.feedback.progress.setpoint.twist.angular.z, _x.feedback.progress.setpoint.accel.linear.x, _x.feedback.progress.setpoint.accel.linear.y, _x.feedback.progress.setpoint.accel.linear.z, _x.feedback.progress.setpoint.accel.angular.x, _x.feedback.progress.setpoint.accel.angular.y, _x.feedback.progress.setpoint.accel.angular.z, _x.feedback.progress.error_position, _x.feedback.progress.error_attitude, _x.feedback.progress.error_velocity, _x.feedback.progress.error_omega, _x.feedback.perc_complete, _x.feedback.secs_remaining))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.feedback is None:
        self.feedback = ff_msgs.msg.MotionFeedback()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.goal_id.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.status.status,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status.text = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.feedback.state.header.seq, _x.feedback.state.header.stamp.secs, _x.feedback.state.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.state.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.feedback.state.header.frame_id = str[start:end]
      start = end
      end += 1
      (self.feedback.state.state,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.state.fsm_event = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.feedback.state.fsm_event = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.feedback.state.fsm_state = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.feedback.state.fsm_state = str[start:end]
      _x = self
      start = end
      end += 188
      (_x.feedback.progress.index, _x.feedback.progress.setpoint.when.secs, _x.feedback.progress.setpoint.when.nsecs, _x.feedback.progress.setpoint.pose.position.x, _x.feedback.progress.setpoint.pose.position.y, _x.feedback.progress.setpoint.pose.position.z, _x.feedback.progress.setpoint.pose.orientation.x, _x.feedback.progress.setpoint.pose.orientation.y, _x.feedback.progress.setpoint.pose.orientation.z, _x.feedback.progress.setpoint.pose.orientation.w, _x.feedback.progress.setpoint.twist.linear.x, _x.feedback.progress.setpoint.twist.linear.y, _x.feedback.progress.setpoint.twist.linear.z, _x.feedback.progress.setpoint.twist.angular.x, _x.feedback.progress.setpoint.twist.angular.y, _x.feedback.progress.setpoint.twist.angular.z, _x.feedback.progress.setpoint.accel.linear.x, _x.feedback.progress.setpoint.accel.linear.y, _x.feedback.progress.setpoint.accel.linear.z, _x.feedback.progress.setpoint.accel.angular.x, _x.feedback.progress.setpoint.accel.angular.y, _x.feedback.progress.setpoint.accel.angular.z, _x.feedback.progress.error_position, _x.feedback.progress.error_attitude, _x.feedback.progress.error_velocity, _x.feedback.progress.error_omega, _x.feedback.perc_complete, _x.feedback.secs_remaining,) = _get_struct_3I19d6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3I19d6f = None
def _get_struct_3I19d6f():
    global _struct_3I19d6f
    if _struct_3I19d6f is None:
        _struct_3I19d6f = struct.Struct("<3I19d6f")
    return _struct_3I19d6f
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
