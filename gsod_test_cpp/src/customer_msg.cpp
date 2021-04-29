#include <chrono>
#include <memory>
#include <stdlib.h>


#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int16.hpp"
#include "custom_msg_interface/msg/request.hpp"

using namespace std::chrono_literals;
using std::placeholders::_1;

class CustomerNode : public rclcpp::Node
{
public:
  CustomerNode()
  : Node("customer_node"), count_(0)
  {
    publisher_ = this->create_publisher<custom_msg_interface::msg::Request>("input", 10);
    timer_ = this->create_wall_timer(
      500ms, std::bind(&CustomerNode::timer_callback, this));
    subscription_ = this->create_subscription<std_msgs::msg::Int16>(
      "result", 10, std::bind(&CustomerNode::topic_callback, this, _1));

  }

private:
  void timer_callback()
  {
    auto message = custom_msg_interface::msg::Request();
    int min = 0;
    int max = 100;
    // https://stackoverflow.com/questions/5008804/generating-random-integer-from-a-range
    message.num1 = min + (rand() % static_cast<int>(max - min + 1));
    message.num2 = min + (rand() % static_cast<int>(max - min + 1));
    RCLCPP_INFO(this->get_logger(), "Publishing: '%d', '%d'", message.num1, message.num2);
    publisher_->publish(message);
  }

  void topic_callback(const std_msgs::msg::Int16::SharedPtr msg) const
  {
    RCLCPP_INFO(this->get_logger(), "Recieved: '%d'", msg->data);
  }

  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<custom_msg_interface::msg::Request>::SharedPtr publisher_;
  size_t count_;
  rclcpp::Subscription<std_msgs::msg::Int16>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<CustomerNode>());
  rclcpp::shutdown();
  return 0;
}
