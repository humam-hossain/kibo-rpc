# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/MotionActionResult.msg. Do not edit."""
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

class MotionActionResult(genpy.Message):
  _md5sum = "2e058e9ae58f45d7fea44e44a053b8f6"
  _type = "ff_msgs/MotionActionResult"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalStatus status
MotionResult result

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
MSG: ff_msgs/MotionResult
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

# Motion result
int32 response                            # Motion action response
int32 ALREADY_THERE                         =   2  # MOVE: We are already at the location
int32 SUCCESS                               =   1  # ALL: Motion succeeded
int32 PREEMPTED                             =   0  # ALL: Motion preempted by thirdparty
int32 PLAN_FAILED                           =  -1  # MOVE/EXEC: Plan/bootstrap failed
int32 VALIDATE_FAILED                       =  -2  # MOVE/EXEC: No comms with mapper
int32 PMC_FAILED                            =  -3  # MOVE/EXEC: PMC failed
int32 CONTROL_FAILED                        =  -4  # ALL: Control failed
int32 OBSTACLE_DETECTED                     =  -5  # ALL: Obstacle / replan disabled
int32 REPLAN_NOT_ENOUGH_TIME                =  -6  # MOVE/EXEC: Not enough time to replan
int32 REPLAN_FAILED                         =  -7  # MOVE/EXEC: Replanning failed
int32 REVALIDATE_FAILED                     =  -8  # MOVE/EXEC: Revalidating failed
int32 NOT_IN_WAITING_MODE                   =  -9  # ALL: Internal failure
int32 INVALID_FLIGHT_MODE                   =  -10 # ALL: No flight mode specified
int32 UNEXPECTED_EMPTY_SEGMENT              =  -11 # EXEC: Segment empty
int32 COULD_NOT_RESAMPLE                    =  -12 # EXEC: Could not resample segment
int32 UNEXPECTED_EMPTY_STATES               =  -13 # MOVE: State vector empty
int32 INVALID_COMMAND                       =  -14 # Command rejected
int32 CANNOT_QUERY_ROBOT_POSE               =  -15 # TF2 failed to find the current pose
int32 NOT_ON_FIRST_POSE                     =  -16 # EXEC: Not on first pose of exec
int32 BAD_DESIRED_VELOCITY                  =  -17 # Requested vel too high
int32 BAD_DESIRED_ACCELERATION              =  -18 # Requested accel too high
int32 BAD_DESIRED_OMEGA                     =  -19 # Requested omega too high
int32 BAD_DESIRED_ALPHA                     =  -20 # Requested alpha too high
int32 BAD_DESIRED_RATE                      =  -21 # Requested rate too low
int32 TOLERANCE_VIOLATION_POSITION_ENDPOINT =  -22 # Position tolerance violated
int32 TOLERANCE_VIOLATION_POSITION          =  -23 # Position tolerance violated
int32 TOLERANCE_VIOLATION_ATTITUDE          =  -24 # Attitude tolerance violated
int32 TOLERANCE_VIOLATION_VELOCITY          =  -25 # Velocity tolerance violated
int32 TOLERANCE_VIOLATION_OMEGA             =  -26 # Omega tolerance violated
int32 VIOLATES_RESAMPLING                   =  -27 # Validation: could not resample@10Hz
int32 VIOLATES_KEEP_OUT                     =  -28 # Validation: Keep out violation
int32 VIOLATES_KEEP_IN                      =  -29 # Validation: Keep in violation
int32 VIOLATES_MINIMUM_FREQUENCY            =  -30 # Validation: Sample frequency too low
int32 VIOLATES_STATIONARY_ENDPOINT          =  -31 # Validation: Last setpoint not static
int32 VIOLATES_FIRST_IN_PAST                =  -32 # Validation: First timestamp in past
int32 VIOLATES_MINIMUM_SETPOINTS            =  -33 # Validation: Not enough setpoints
int32 VIOLATES_HARD_LIMIT_VEL               =  -34 # Validation: Velocity too high
int32 VIOLATES_HARD_LIMIT_ACCEL             =  -35 # Validation: Acceleration too high
int32 VIOLATES_HARD_LIMIT_OMEGA             =  -36 # Validation: Omega too high
int32 VIOLATES_HARD_LIMIT_ALPHA             =  -37 # Validation: Alpha too high
int32 CANCELLED                             =  -38 # ALL: Motion cancelled by callee
int32 INVALID_REFERENCE_FRAME               =  -39 # ALL: Unknown reference frame

# Human readable FSM result for debugging
string fsm_result

# The flight mode parameters used
ff_msgs/FlightMode flight_mode

# The final segment that was flown
ff_msgs/ControlState[] segment


================================================================================
MSG: ff_msgs/FlightMode
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
# This message captures all information in a flight mode

Header header                     # Metadata

string name                       # Name of the flight mode

bool control_enabled              # Is control enabled?

float32 collision_radius          # Collision radius in meters

# Tolerances (all in SI units)
float32 tolerance_pos_endpoint    # Endpoint position tolerance in m
float32 tolerance_pos             # Position tolerance in m
float32 tolerance_vel             # Velocity tolerance in m/s
float32 tolerance_att             # Attitude tolerance in rads
float32 tolerance_omega           # Angular acceleration tolerance in rad/s
float32 tolerance_time            # Acceptable lag betwee TX and RX of control

# Controller gains
geometry_msgs/Vector3 att_kp      # Positional proportional constant
geometry_msgs/Vector3 att_ki      # Positional integrative constant
geometry_msgs/Vector3 omega_kd    # Attidue derivative constant
geometry_msgs/Vector3 pos_kp      # Positional proportional contant
geometry_msgs/Vector3 pos_ki      # Positional integrative constant
geometry_msgs/Vector3 vel_kd      # Positional derivative constant

# Hard limit on planning
float32 hard_limit_vel            # Position tolerance in m/s
float32 hard_limit_accel          # Position tolerance in m/s^2
float32 hard_limit_omega          # Position tolerance in rads/s
float32 hard_limit_alpha          # Position tolerance in rads/s^2

# Impeller speed
uint8 speed                       # Current speed gain
uint8 SPEED_MIN        = 0        # Min acceptable gain
uint8 SPEED_OFF        = 0        # Blowers off
uint8 SPEED_QUIET      = 1        # Quiet mode
uint8 SPEED_NOMINAL    = 2        # Nomainal mode
uint8 SPEED_AGGRESSIVE = 3        # Aggressive mode
uint8 SPEED_MAX        = 3        # Max acceptable gain

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
float64 z
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
"""
  __slots__ = ['header','status','result']
  _slot_types = ['std_msgs/Header','actionlib_msgs/GoalStatus','ff_msgs/MotionResult']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,status,result

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MotionActionResult, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.result is None:
        self.result = ff_msgs.msg.MotionResult()
    else:
      self.header = std_msgs.msg.Header()
      self.status = actionlib_msgs.msg.GoalStatus()
      self.result = ff_msgs.msg.MotionResult()

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
      _x = self.result.response
      buff.write(_get_struct_i().pack(_x))
      _x = self.result.fsm_result
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.result.flight_mode.header.seq, _x.result.flight_mode.header.stamp.secs, _x.result.flight_mode.header.stamp.nsecs))
      _x = self.result.flight_mode.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.result.flight_mode.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B7f18d4fB().pack(_x.result.flight_mode.control_enabled, _x.result.flight_mode.collision_radius, _x.result.flight_mode.tolerance_pos_endpoint, _x.result.flight_mode.tolerance_pos, _x.result.flight_mode.tolerance_vel, _x.result.flight_mode.tolerance_att, _x.result.flight_mode.tolerance_omega, _x.result.flight_mode.tolerance_time, _x.result.flight_mode.att_kp.x, _x.result.flight_mode.att_kp.y, _x.result.flight_mode.att_kp.z, _x.result.flight_mode.att_ki.x, _x.result.flight_mode.att_ki.y, _x.result.flight_mode.att_ki.z, _x.result.flight_mode.omega_kd.x, _x.result.flight_mode.omega_kd.y, _x.result.flight_mode.omega_kd.z, _x.result.flight_mode.pos_kp.x, _x.result.flight_mode.pos_kp.y, _x.result.flight_mode.pos_kp.z, _x.result.flight_mode.pos_ki.x, _x.result.flight_mode.pos_ki.y, _x.result.flight_mode.pos_ki.z, _x.result.flight_mode.vel_kd.x, _x.result.flight_mode.vel_kd.y, _x.result.flight_mode.vel_kd.z, _x.result.flight_mode.hard_limit_vel, _x.result.flight_mode.hard_limit_accel, _x.result.flight_mode.hard_limit_omega, _x.result.flight_mode.hard_limit_alpha, _x.result.flight_mode.speed))
      length = len(self.result.segment)
      buff.write(_struct_I.pack(length))
      for val1 in self.result.segment:
        _v1 = val1.when
        _x = _v1
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _v2 = val1.pose
        _v3 = _v2.position
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v4 = _v2.orientation
        _x = _v4
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _v5 = val1.twist
        _v6 = _v5.linear
        _x = _v6
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v7 = _v5.angular
        _x = _v7
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v8 = val1.accel
        _v9 = _v8.linear
        _x = _v9
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v10 = _v8.angular
        _x = _v10
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
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
      if self.result is None:
        self.result = ff_msgs.msg.MotionResult()
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
      start = end
      end += 4
      (self.result.response,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.fsm_result = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.result.fsm_result = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.result.flight_mode.header.seq, _x.result.flight_mode.header.stamp.secs, _x.result.flight_mode.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.flight_mode.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.result.flight_mode.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.flight_mode.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.result.flight_mode.name = str[start:end]
      _x = self
      start = end
      end += 190
      (_x.result.flight_mode.control_enabled, _x.result.flight_mode.collision_radius, _x.result.flight_mode.tolerance_pos_endpoint, _x.result.flight_mode.tolerance_pos, _x.result.flight_mode.tolerance_vel, _x.result.flight_mode.tolerance_att, _x.result.flight_mode.tolerance_omega, _x.result.flight_mode.tolerance_time, _x.result.flight_mode.att_kp.x, _x.result.flight_mode.att_kp.y, _x.result.flight_mode.att_kp.z, _x.result.flight_mode.att_ki.x, _x.result.flight_mode.att_ki.y, _x.result.flight_mode.att_ki.z, _x.result.flight_mode.omega_kd.x, _x.result.flight_mode.omega_kd.y, _x.result.flight_mode.omega_kd.z, _x.result.flight_mode.pos_kp.x, _x.result.flight_mode.pos_kp.y, _x.result.flight_mode.pos_kp.z, _x.result.flight_mode.pos_ki.x, _x.result.flight_mode.pos_ki.y, _x.result.flight_mode.pos_ki.z, _x.result.flight_mode.vel_kd.x, _x.result.flight_mode.vel_kd.y, _x.result.flight_mode.vel_kd.z, _x.result.flight_mode.hard_limit_vel, _x.result.flight_mode.hard_limit_accel, _x.result.flight_mode.hard_limit_omega, _x.result.flight_mode.hard_limit_alpha, _x.result.flight_mode.speed,) = _get_struct_B7f18d4fB().unpack(str[start:end])
      self.result.flight_mode.control_enabled = bool(self.result.flight_mode.control_enabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.result.segment = []
      for i in range(0, length):
        val1 = ff_msgs.msg.ControlState()
        _v11 = val1.when
        _x = _v11
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        _v12 = val1.pose
        _v13 = _v12.position
        _x = _v13
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v14 = _v12.orientation
        _x = _v14
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        _v15 = val1.twist
        _v16 = _v15.linear
        _x = _v16
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v17 = _v15.angular
        _x = _v17
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v18 = val1.accel
        _v19 = _v18.linear
        _x = _v19
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v20 = _v18.angular
        _x = _v20
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.result.segment.append(val1)
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
      _x = self.result.response
      buff.write(_get_struct_i().pack(_x))
      _x = self.result.fsm_result
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.result.flight_mode.header.seq, _x.result.flight_mode.header.stamp.secs, _x.result.flight_mode.header.stamp.nsecs))
      _x = self.result.flight_mode.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.result.flight_mode.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B7f18d4fB().pack(_x.result.flight_mode.control_enabled, _x.result.flight_mode.collision_radius, _x.result.flight_mode.tolerance_pos_endpoint, _x.result.flight_mode.tolerance_pos, _x.result.flight_mode.tolerance_vel, _x.result.flight_mode.tolerance_att, _x.result.flight_mode.tolerance_omega, _x.result.flight_mode.tolerance_time, _x.result.flight_mode.att_kp.x, _x.result.flight_mode.att_kp.y, _x.result.flight_mode.att_kp.z, _x.result.flight_mode.att_ki.x, _x.result.flight_mode.att_ki.y, _x.result.flight_mode.att_ki.z, _x.result.flight_mode.omega_kd.x, _x.result.flight_mode.omega_kd.y, _x.result.flight_mode.omega_kd.z, _x.result.flight_mode.pos_kp.x, _x.result.flight_mode.pos_kp.y, _x.result.flight_mode.pos_kp.z, _x.result.flight_mode.pos_ki.x, _x.result.flight_mode.pos_ki.y, _x.result.flight_mode.pos_ki.z, _x.result.flight_mode.vel_kd.x, _x.result.flight_mode.vel_kd.y, _x.result.flight_mode.vel_kd.z, _x.result.flight_mode.hard_limit_vel, _x.result.flight_mode.hard_limit_accel, _x.result.flight_mode.hard_limit_omega, _x.result.flight_mode.hard_limit_alpha, _x.result.flight_mode.speed))
      length = len(self.result.segment)
      buff.write(_struct_I.pack(length))
      for val1 in self.result.segment:
        _v21 = val1.when
        _x = _v21
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _v22 = val1.pose
        _v23 = _v22.position
        _x = _v23
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v24 = _v22.orientation
        _x = _v24
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _v25 = val1.twist
        _v26 = _v25.linear
        _x = _v26
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v27 = _v25.angular
        _x = _v27
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v28 = val1.accel
        _v29 = _v28.linear
        _x = _v29
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v30 = _v28.angular
        _x = _v30
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
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
      if self.result is None:
        self.result = ff_msgs.msg.MotionResult()
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
      start = end
      end += 4
      (self.result.response,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.fsm_result = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.result.fsm_result = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.result.flight_mode.header.seq, _x.result.flight_mode.header.stamp.secs, _x.result.flight_mode.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.flight_mode.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.result.flight_mode.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.flight_mode.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.result.flight_mode.name = str[start:end]
      _x = self
      start = end
      end += 190
      (_x.result.flight_mode.control_enabled, _x.result.flight_mode.collision_radius, _x.result.flight_mode.tolerance_pos_endpoint, _x.result.flight_mode.tolerance_pos, _x.result.flight_mode.tolerance_vel, _x.result.flight_mode.tolerance_att, _x.result.flight_mode.tolerance_omega, _x.result.flight_mode.tolerance_time, _x.result.flight_mode.att_kp.x, _x.result.flight_mode.att_kp.y, _x.result.flight_mode.att_kp.z, _x.result.flight_mode.att_ki.x, _x.result.flight_mode.att_ki.y, _x.result.flight_mode.att_ki.z, _x.result.flight_mode.omega_kd.x, _x.result.flight_mode.omega_kd.y, _x.result.flight_mode.omega_kd.z, _x.result.flight_mode.pos_kp.x, _x.result.flight_mode.pos_kp.y, _x.result.flight_mode.pos_kp.z, _x.result.flight_mode.pos_ki.x, _x.result.flight_mode.pos_ki.y, _x.result.flight_mode.pos_ki.z, _x.result.flight_mode.vel_kd.x, _x.result.flight_mode.vel_kd.y, _x.result.flight_mode.vel_kd.z, _x.result.flight_mode.hard_limit_vel, _x.result.flight_mode.hard_limit_accel, _x.result.flight_mode.hard_limit_omega, _x.result.flight_mode.hard_limit_alpha, _x.result.flight_mode.speed,) = _get_struct_B7f18d4fB().unpack(str[start:end])
      self.result.flight_mode.control_enabled = bool(self.result.flight_mode.control_enabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.result.segment = []
      for i in range(0, length):
        val1 = ff_msgs.msg.ControlState()
        _v31 = val1.when
        _x = _v31
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        _v32 = val1.pose
        _v33 = _v32.position
        _x = _v33
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v34 = _v32.orientation
        _x = _v34
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        _v35 = val1.twist
        _v36 = _v35.linear
        _x = _v36
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v37 = _v35.angular
        _x = _v37
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v38 = val1.accel
        _v39 = _v38.linear
        _x = _v39
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v40 = _v38.angular
        _x = _v40
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.result.segment.append(val1)
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
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_B7f18d4fB = None
def _get_struct_B7f18d4fB():
    global _struct_B7f18d4fB
    if _struct_B7f18d4fB is None:
        _struct_B7f18d4fB = struct.Struct("<B7f18d4fB")
    return _struct_B7f18d4fB
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i