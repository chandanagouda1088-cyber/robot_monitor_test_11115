import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class RobotMonitor(Node):
	def __init__(self):
		super().__init__('robot_monitor_node')
		self.battery_publisher = self.create_publisher(Int32,'/robot/battery_percentage',10)
		self.temperature_publisher = self.create_publisher(Int32,'/robot/temperature_celcius',10)
		self.battery = 85
		self.temperature = 35
		self.timer = self.create_timer(1.0,self.publish_status)
	def publish_status(self):
		self.battery = random.randint(0,100)
		self.temperature = random.randint(0,70)
		battery_msg = Int32()
		battery_msg.data = self.battery
		self.battery_publisher.publish(battery_msg)
		temperature_msg = Int32()
		temperature_msg.data = self.temperature
		self.temperature_publisher.publish(temperature_msg)
		self.get_logger().info(f'Battery: {self.battery:.1f}% |'f'Temperature: {self.temperature:.1f} C')
def main(args=None):
	rclpy.init(args=args)
	node = RobotMonitor()
	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		pass
	finally:
		node.destroy_node()
		rclpy.shutdown()
if __name__ == '__main__':
	main()
