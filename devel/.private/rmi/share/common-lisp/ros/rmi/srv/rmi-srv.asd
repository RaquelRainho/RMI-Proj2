
(cl:in-package :asdf)

(defsystem "rmi-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MoveArm" :depends-on ("_package_MoveArm"))
    (:file "_package_MoveArm" :depends-on ("_package"))
  ))