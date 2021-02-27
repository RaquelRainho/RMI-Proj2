;; Auto-generated. Do not edit!


(when (boundp 'rmi::MoveArm)
  (if (not (find-package "RMI"))
    (make-package "RMI"))
  (shadow 'MoveArm (find-package "RMI")))
(unless (find-package "RMI::MOVEARM")
  (make-package "RMI::MOVEARM"))
(unless (find-package "RMI::MOVEARMREQUEST")
  (make-package "RMI::MOVEARMREQUEST"))
(unless (find-package "RMI::MOVEARMRESPONSE")
  (make-package "RMI::MOVEARMRESPONSE"))

(in-package "ROS")





(defclass rmi::MoveArmRequest
  :super ros::object
  :slots (_x _y _z _roll _pitch _yaw _gripping ))

(defmethod rmi::MoveArmRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:roll __roll) 0.0)
    ((:pitch __pitch) 0.0)
    ((:yaw __yaw) 0.0)
    ((:gripping __gripping) nil)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _roll (float __roll))
   (setq _pitch (float __pitch))
   (setq _yaw (float __yaw))
   (setq _gripping __gripping)
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:gripping
   (&optional __gripping)
   (if __gripping (setq _gripping __gripping)) _gripping)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _z
    4
    ;; float32 _roll
    4
    ;; float32 _pitch
    4
    ;; float32 _yaw
    4
    ;; bool _gripping
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z
       (sys::poke _z (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _roll
       (sys::poke _roll (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; bool _gripping
       (if _gripping (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z
     (setq _z (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _roll
     (setq _roll (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pitch
     (setq _pitch (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _yaw
     (setq _yaw (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; bool _gripping
     (setq _gripping (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass rmi::MoveArmResponse
  :super ros::object
  :slots (_success ))

(defmethod rmi::MoveArmResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass rmi::MoveArm
  :super ros::object
  :slots ())

(setf (get rmi::MoveArm :md5sum-) "74ba88dd7a232cebfc2c0ee0e397f0fc")
(setf (get rmi::MoveArm :datatype-) "rmi/MoveArm")
(setf (get rmi::MoveArm :request) rmi::MoveArmRequest)
(setf (get rmi::MoveArm :response) rmi::MoveArmResponse)

(defmethod rmi::MoveArmRequest
  (:response () (instance rmi::MoveArmResponse :init)))

(setf (get rmi::MoveArmRequest :md5sum-) "74ba88dd7a232cebfc2c0ee0e397f0fc")
(setf (get rmi::MoveArmRequest :datatype-) "rmi/MoveArmRequest")
(setf (get rmi::MoveArmRequest :definition-)
      "float32 x
float32 y
float32 z
float32 roll
float32 pitch
float32 yaw
bool gripping
---
bool success
")

(setf (get rmi::MoveArmResponse :md5sum-) "74ba88dd7a232cebfc2c0ee0e397f0fc")
(setf (get rmi::MoveArmResponse :datatype-) "rmi/MoveArmResponse")
(setf (get rmi::MoveArmResponse :definition-)
      "float32 x
float32 y
float32 z
float32 roll
float32 pitch
float32 yaw
bool gripping
---
bool success
")



(provide :rmi/MoveArm "74ba88dd7a232cebfc2c0ee0e397f0fc")


