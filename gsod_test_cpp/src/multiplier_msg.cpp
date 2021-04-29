#include <chrono>
#include <memory>
#include <stdlib.h>


#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int16.hpp"
#include "custom_msg_interface/msg/request.hpp"

using namespace std::chrono_literals;
using std::placeholders::_1;

class MultiplierNode : public rclcpp::Node
{
public:
  MultiplierNode()
  : Node("mutiplier_node"), count_(0)
  {
    publisher_ = this->create_publisher<std_msgs::msg::Int16>("result", 10);
    subscription_ = this->create_subscription<custom_msg_interface::msg::Request>(
      "input", 10, std::bind(&MultiplierNode::topic_callback, this, _1));

  }

private:
  void timer_callback()
  {

  }

  void topic_callback(const custom_msg_interface::msg::Request::SharedPtr recv) const
  {
    RCLCPP_INFO(this->get_logger(), "Recieved: '%d', '%d'", recv->num1, recv->num2);
    auto message = std_msgs::msg::Int16();
    message.data = recv->num1 * recv->num2;
    RCLCPP_INFO(this->get_logger(), "Publishing: '%d'", message.data);
    publisher_->publish(message);
  }

  rclcpp::Publisher<std_msgs::msg::Int16>::SharedPtr publisher_;
  size_t count_;
  rclcpp::Subscription<custom_msg_interface::msg::Request>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MultiplierNode>());
  rclcpp::shutdown();
  return 0;
}
