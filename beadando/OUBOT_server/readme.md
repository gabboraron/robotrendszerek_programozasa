# ROS2 on OUBOT
1. install ROS2 to docker: https://docs.ros.org/en/foxy/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html
2. example test code: 
   ```bash
   ros2 run demo_nodes_cpp listener &
   ros2 run demo_nodes_cpp talker
   ```
3. example for talking: `docker run -it --rm osrf/ros:foxy-desktop ros2 run demo_nodes_cpp talker`
4. example for listening: `docker run -it --rm osrf/ros:foxy-desktop ros2 run demo_nodes_cpp listener`