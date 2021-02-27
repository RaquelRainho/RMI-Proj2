; Auto-generated. Do not edit!


(cl:in-package rmi-srv)


;//! \htmlinclude MoveArm-request.msg.html

(cl:defclass <MoveArm-request> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (z
    :reader z
    :initarg :z
    :type cl:float
    :initform 0.0)
   (roll
    :reader roll
    :initarg :roll
    :type cl:float
    :initform 0.0)
   (pitch
    :reader pitch
    :initarg :pitch
    :type cl:float
    :initform 0.0)
   (yaw
    :reader yaw
    :initarg :yaw
    :type cl:float
    :initform 0.0)
   (gripping
    :reader gripping
    :initarg :gripping
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass MoveArm-request (<MoveArm-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveArm-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveArm-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rmi-srv:<MoveArm-request> is deprecated: use rmi-srv:MoveArm-request instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <MoveArm-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rmi-srv:x-val is deprecated.  Use rmi-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <MoveArm-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rmi-srv:y-val is deprecated.  Use rmi-srv:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <MoveArm-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rmi-srv:z-val is deprecated.  Use rmi-srv:z instead.")
  (z m))

(cl:ensure-generic-function 'roll-val :lambda-list '(m))
(cl:defmethod roll-val ((m <MoveArm-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rmi-srv:roll-val is deprecated.  Use rmi-srv:roll instead.")
  (roll m))

(cl:ensure-generic-function 'pitch-val :lambda-list '(m))
(cl:defmethod pitch-val ((m <MoveArm-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rmi-srv:pitch-val is deprecated.  Use rmi-srv:pitch instead.")
  (pitch m))

(cl:ensure-generic-function 'yaw-val :lambda-list '(m))
(cl:defmethod yaw-val ((m <MoveArm-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rmi-srv:yaw-val is deprecated.  Use rmi-srv:yaw instead.")
  (yaw m))

(cl:ensure-generic-function 'gripping-val :lambda-list '(m))
(cl:defmethod gripping-val ((m <MoveArm-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rmi-srv:gripping-val is deprecated.  Use rmi-srv:gripping instead.")
  (gripping m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveArm-request>) ostream)
  "Serializes a message object of type '<MoveArm-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'roll))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pitch))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'yaw))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'gripping) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveArm-request>) istream)
  "Deserializes a message object of type '<MoveArm-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'roll) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pitch) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yaw) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'gripping) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveArm-request>)))
  "Returns string type for a service object of type '<MoveArm-request>"
  "rmi/MoveArmRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveArm-request)))
  "Returns string type for a service object of type 'MoveArm-request"
  "rmi/MoveArmRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveArm-request>)))
  "Returns md5sum for a message object of type '<MoveArm-request>"
  "74ba88dd7a232cebfc2c0ee0e397f0fc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveArm-request)))
  "Returns md5sum for a message object of type 'MoveArm-request"
  "74ba88dd7a232cebfc2c0ee0e397f0fc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveArm-request>)))
  "Returns full string definition for message of type '<MoveArm-request>"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%float32 roll~%float32 pitch~%float32 yaw~%bool gripping~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveArm-request)))
  "Returns full string definition for message of type 'MoveArm-request"
  (cl:format cl:nil "float32 x~%float32 y~%float32 z~%float32 roll~%float32 pitch~%float32 yaw~%bool gripping~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveArm-request>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveArm-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveArm-request
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
    (cl:cons ':roll (roll msg))
    (cl:cons ':pitch (pitch msg))
    (cl:cons ':yaw (yaw msg))
    (cl:cons ':gripping (gripping msg))
))
;//! \htmlinclude MoveArm-response.msg.html

(cl:defclass <MoveArm-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass MoveArm-response (<MoveArm-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoveArm-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoveArm-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rmi-srv:<MoveArm-response> is deprecated: use rmi-srv:MoveArm-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <MoveArm-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rmi-srv:success-val is deprecated.  Use rmi-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoveArm-response>) ostream)
  "Serializes a message object of type '<MoveArm-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoveArm-response>) istream)
  "Deserializes a message object of type '<MoveArm-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoveArm-response>)))
  "Returns string type for a service object of type '<MoveArm-response>"
  "rmi/MoveArmResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveArm-response)))
  "Returns string type for a service object of type 'MoveArm-response"
  "rmi/MoveArmResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoveArm-response>)))
  "Returns md5sum for a message object of type '<MoveArm-response>"
  "74ba88dd7a232cebfc2c0ee0e397f0fc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoveArm-response)))
  "Returns md5sum for a message object of type 'MoveArm-response"
  "74ba88dd7a232cebfc2c0ee0e397f0fc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoveArm-response>)))
  "Returns full string definition for message of type '<MoveArm-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoveArm-response)))
  "Returns full string definition for message of type 'MoveArm-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoveArm-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoveArm-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MoveArm-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MoveArm)))
  'MoveArm-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MoveArm)))
  'MoveArm-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoveArm)))
  "Returns string type for a service object of type '<MoveArm>"
  "rmi/MoveArm")