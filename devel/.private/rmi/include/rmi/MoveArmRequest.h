// Generated by gencpp from file rmi/MoveArmRequest.msg
// DO NOT EDIT!


#ifndef RMI_MESSAGE_MOVEARMREQUEST_H
#define RMI_MESSAGE_MOVEARMREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rmi
{
template <class ContainerAllocator>
struct MoveArmRequest_
{
  typedef MoveArmRequest_<ContainerAllocator> Type;

  MoveArmRequest_()
    : x(0.0)
    , y(0.0)
    , z(0.0)
    , roll(0.0)
    , pitch(0.0)
    , yaw(0.0)
    , gripping(false)  {
    }
  MoveArmRequest_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , z(0.0)
    , roll(0.0)
    , pitch(0.0)
    , yaw(0.0)
    , gripping(false)  {
  (void)_alloc;
    }



   typedef float _x_type;
  _x_type x;

   typedef float _y_type;
  _y_type y;

   typedef float _z_type;
  _z_type z;

   typedef float _roll_type;
  _roll_type roll;

   typedef float _pitch_type;
  _pitch_type pitch;

   typedef float _yaw_type;
  _yaw_type yaw;

   typedef uint8_t _gripping_type;
  _gripping_type gripping;





  typedef boost::shared_ptr< ::rmi::MoveArmRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rmi::MoveArmRequest_<ContainerAllocator> const> ConstPtr;

}; // struct MoveArmRequest_

typedef ::rmi::MoveArmRequest_<std::allocator<void> > MoveArmRequest;

typedef boost::shared_ptr< ::rmi::MoveArmRequest > MoveArmRequestPtr;
typedef boost::shared_ptr< ::rmi::MoveArmRequest const> MoveArmRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rmi::MoveArmRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rmi::MoveArmRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rmi::MoveArmRequest_<ContainerAllocator1> & lhs, const ::rmi::MoveArmRequest_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.z == rhs.z &&
    lhs.roll == rhs.roll &&
    lhs.pitch == rhs.pitch &&
    lhs.yaw == rhs.yaw &&
    lhs.gripping == rhs.gripping;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rmi::MoveArmRequest_<ContainerAllocator1> & lhs, const ::rmi::MoveArmRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rmi

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::rmi::MoveArmRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rmi::MoveArmRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rmi::MoveArmRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rmi::MoveArmRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rmi::MoveArmRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rmi::MoveArmRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rmi::MoveArmRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4b84f97ccd989e0a30d6c6f784a28f52";
  }

  static const char* value(const ::rmi::MoveArmRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4b84f97ccd989e0aULL;
  static const uint64_t static_value2 = 0x30d6c6f784a28f52ULL;
};

template<class ContainerAllocator>
struct DataType< ::rmi::MoveArmRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rmi/MoveArmRequest";
  }

  static const char* value(const ::rmi::MoveArmRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rmi::MoveArmRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 x\n"
"float32 y\n"
"float32 z\n"
"float32 roll\n"
"float32 pitch\n"
"float32 yaw\n"
"bool gripping\n"
;
  }

  static const char* value(const ::rmi::MoveArmRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rmi::MoveArmRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
      stream.next(m.roll);
      stream.next(m.pitch);
      stream.next(m.yaw);
      stream.next(m.gripping);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveArmRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rmi::MoveArmRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rmi::MoveArmRequest_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<float>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<float>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<float>::stream(s, indent + "  ", v.z);
    s << indent << "roll: ";
    Printer<float>::stream(s, indent + "  ", v.roll);
    s << indent << "pitch: ";
    Printer<float>::stream(s, indent + "  ", v.pitch);
    s << indent << "yaw: ";
    Printer<float>::stream(s, indent + "  ", v.yaw);
    s << indent << "gripping: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.gripping);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RMI_MESSAGE_MOVEARMREQUEST_H
