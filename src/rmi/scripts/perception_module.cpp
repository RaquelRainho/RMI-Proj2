#include "ros/ros.h"
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/filters/passthrough.h>
#include <pcl/filters/conditional_removal.h>
#include <pcl/common/centroid.h>
#include <ros/console.h>
#include <tf/transform_listener.h>
#include <tf/transform_datatypes.h>

#include "rmi/GetRingPose.h"
#include "rmi/PoseCoords.h"
#include <iostream>
using namespace std;

sensor_msgs::PointCloud2 updatedPC;
ros::Publisher pub;

void processPC(int ringId, rmi::PoseCoords &pose){
  // Convert the point cloud type to pcl::PointXYZRGB 
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr pointCloud(new pcl::PointCloud<pcl::PointXYZRGB>);
  pcl::fromROSMsg(updatedPC, *pointCloud);

  // Apply filters
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr pcPassFiltered(new pcl::PointCloud<pcl::PointXYZRGB>);

  // Passthrough filter - removes the table and all the points below it
  pcl::PassThrough<pcl::PointXYZRGB> passThroughFilter;
  passThroughFilter.setInputCloud(pointCloud);
  passThroughFilter.setFilterFieldName("z");
  passThroughFilter.setFilterLimits(0.0, 1.19);
  passThroughFilter.filter(*pcPassFiltered);

  // Used to verify the filter applied to the point cloud
  //sensor_msgs::PointCloud2 outputPassFiltered;
  //pcl::toROSMsg( *pcPassFiltered, outputPassFiltered);
  //pub.publish(outputPassFiltered);

  // Color segmentation - filter ring by color
  pcl::ConditionAnd<pcl::PointXYZRGB>::Ptr colorCond (new pcl::ConditionAnd<pcl::PointXYZRGB> ());
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr pcChosenRing(new pcl::PointCloud<pcl::PointXYZRGB>);

  // red r_max=255, r_min=123, g_max=23, g_min=0, b_max=23, b_min=0
  // blue r_max=23, r_min=0, g_max=23, g_min=0, b_max=255, b_min=123
  // purple r_max=145, r_min=110, g_max=23, g_min=0, b_max=145, b_min=110
  // colors[ringId] = {r_min, r_max, g_min, g_max, b_min, b_max}
  int colors [][6] = {{110,145,0,23,110,145},{0,23,0,23,123,255},{123,255,0,23,0,23}};
  
  colorCond->addComparison (pcl::PackedRGBComparison<pcl::PointXYZRGB>::Ptr (new pcl::PackedRGBComparison<pcl::PointXYZRGB> ("r", pcl::ComparisonOps::GT, colors[ringId][0])));
  colorCond->addComparison (pcl::PackedRGBComparison<pcl::PointXYZRGB>::Ptr (new pcl::PackedRGBComparison<pcl::PointXYZRGB> ("r", pcl::ComparisonOps::LT, colors[ringId][1])));
  colorCond->addComparison (pcl::PackedRGBComparison<pcl::PointXYZRGB>::Ptr (new pcl::PackedRGBComparison<pcl::PointXYZRGB> ("g", pcl::ComparisonOps::GT, colors[ringId][2])));
  colorCond->addComparison (pcl::PackedRGBComparison<pcl::PointXYZRGB>::Ptr (new pcl::PackedRGBComparison<pcl::PointXYZRGB> ("g", pcl::ComparisonOps::LT, colors[ringId][3])));
  colorCond->addComparison (pcl::PackedRGBComparison<pcl::PointXYZRGB>::Ptr (new pcl::PackedRGBComparison<pcl::PointXYZRGB> ("b", pcl::ComparisonOps::GT, colors[ringId][4])));
  colorCond->addComparison (pcl::PackedRGBComparison<pcl::PointXYZRGB>::Ptr (new pcl::PackedRGBComparison<pcl::PointXYZRGB> ("b", pcl::ComparisonOps::LT, colors[ringId][5])));

  pcl::ConditionalRemoval<pcl::PointXYZRGB> condRem (colorCond);
  condRem.setInputCloud (pcPassFiltered);
  condRem.setKeepOrganized(false);
  condRem.filter (*pcChosenRing);

  sensor_msgs::PointCloud2 outputColorSegm;
  pcl::toROSMsg( *pcChosenRing, outputColorSegm);
  pub.publish(outputColorSegm);

  // Calculate centroid
  Eigen::Vector4f centroid;
  pcl::compute3DCentroid( *pcChosenRing, centroid);

  // Transform position in order to correspond to the world points
  tf::TransformListener listener;
  tf::StampedTransform transform;
  try
      {
        listener.waitForTransform("/camera_depth_optical_frame", "/base_link", ros::Time(), ros::Duration(5.0));
        listener.lookupTransform("/camera_depth_optical_frame", "/base_link", ros::Time(), transform);
      }
      catch(tf::TransformException ex)
      {
        ROS_WARN("Transform unavailable %s", ex.what());
      }
  
  tf::Vector3 point(centroid.coeff(0,0), centroid.coeff(1,0), centroid.coeff(2,0));
  tf::Vector3 pointFinal = transform * point;

  // Return pose
  pose.x = pointFinal.getX() + 0.041; // depth camera offset
  pose.y = pointFinal.getY() + 0.012;  // ring hole offset
  pose.z = pointFinal.getZ();
  pose.roll = 0;
  pose.pitch = 0;
  pose.yaw = 0; // for now, we assume that the pieces are in the correct orientation
}

// Service's callback
bool getRingPose(rmi::GetRingPose::Request &req, rmi::GetRingPose::Response &resp)
{
  ROS_INFO("Service called.");
  //ROS_INFO_STREAM("Ring ID: " << req.ring_id);
  rmi::PoseCoords pose;
  
  // Process and change point cloud in order to detect the ring
  processPC(req.ring_id, pose);

  // Get and return ring pose
  resp.pose = pose;

  return true;
}

// Subscriber's callback - updates the point cloud
void updatePointCloud (const sensor_msgs::PointCloud2ConstPtr& cloud_msg)
{
  updatedPC = *cloud_msg;
}

int main (int argc, char** argv)
{
  // Initialize ROS
  ros::init (argc, argv, "perception_module");
  ROS_INFO("perception_module node started...");
  ros::NodeHandle handler;

  //Initialize service
  ros::ServiceServer service = handler.advertiseService("get_ring_pose", getRingPose);
  ROS_INFO("Ready to get ring pose.");

  // Initialize publisher that will be used to debug
  pub = handler.advertise<sensor_msgs::PointCloud2>("point_cloud_debug", 1);

  // Initialize subscriber for the input point cloud
  ros::Subscriber sub = handler.subscribe ("/camera/depth/points", 1, updatePointCloud);

  ros::spin();
    
  return 0;

}