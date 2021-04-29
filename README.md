# GSoD-OSRF-Task-2021
This repository contains solutions for Google Summer of Docs (GSoD) assignment 2021. The task is about writting ROS2 nodes as publisher and subscriber to perform service-like behavior for doubling a number.

In this task, I have chosen ROS2 Foxy Fitzroy.



## Installation and preparing the environment:

There are 2 ways to use ROS2 that I have found: normal installation or using Docker

### Normal installation:
Install ROS2 Foxy Fitzroy according to the installation section in the [documentation](https://docs.ros.org/en/foxy/Installation.html).

After installation, you can check the following tutorials:

* [Configure environment tutorial](https://docs.ros.org/en/foxy/Tutorials/Configuring-ROS2-Environment.html).

* [Creating Workspace tutorial](https://docs.ros.org/en/foxy/Tutorials/Workspace/Creating-A-Workspace.html)

* Place the packages by copying``gsod_test_cpp``, ``gsod_test_py``, ``custom_msg_interface`` to dev_ws/src or clone the repo as in ``Creating Workspace tutorial``

* Then, start build the packages:

Build the message interface package to avoid errors of dependencies from other packages:

```colcon build --packages-select custom_msg_interface```

```. install/setup.bash``` or ``setup.zsh`` if you are using .zsh

Build the other packages:

```colcon build```

```. install/setup.bash``` or ``setup.zsh`` if you are using .zsh

### Use ROS2 through Docker

I have found this working repository and with good steps to use ROS2 Foxy Fitzroy through Docker: [repository link](https://github.com/PXLAIRobotics/ROS2FoxyDocker/blob/master/02_run_container.sh).

Then, removed lines 33 and 49 from ``02_run_container.sh`` in order not to have problems with run multiple docker continers from the same image simultanosuly.
<!-- one to run the first node  (that sends the numbers) and the other to run the second node (that multiplies the numbers)  -->

I have used the latter method to use ROS2 through Docker as I have ROS melodic and Ubutuntu 18.04 which are not compatible with ROS2 Foxy. Moreover, working using Docker is very simple and straightforward. So, I personally recommend to use this method.

After following the ``README.md`` inside the mentioned repository for docker, you may copy the packages or copy the repository inside the ``Projects`` in the cloned repository.

Full steps:

* ```git clone https://github.com/PXLAIRobotics/ROS2FoxyDocker.git```

* ```cd ROS2FoxyDocker```

* ```./01_build_image.sh```

* ```chmod +x 01_build_image.sh```

* ```chmod +x 02_run_container_sh```

* Remove lines 33 and 49 from ``02_run_container.sh``

* ``` cd Projects/dev_ws_src/ && git clone https://github.com/hany606/GSoD-OSRF-Task-2021.git``` or clone it somewhere else and copy the packages directory inside ``ROS2FoxyDocker/Projects/dev_ws_src`` (This directory/volume is being accessed from inside the container)

* ```./02_run_container.sh```

* ```cd Projects/dev_ws```

* Then, start build the packages:

Build the message interface package to avoid errors of dependencies from other packages:

```colcon build --packages-select custom_msg_interface```

```. install/setup.bash```

Build the other packages:

```colcon build```

```. install/setup.bash```

## Architechture
We have two nodes:

* 1st node "Customer": the node that publishes the number to be doubled (or for the extra task publishes two numbers to be multiplied) in ``/input`` topic. Moreover, it subscirbes to ``/result`` to get the result of the multiplication.

* 2nd node ``Multiplier``: the node that subscribes to ``/input`` topic and do the multiplication process and returns the result by publishing it to ``/result`` topic.


![Architechture](https://github.com/hany606/GSoD-OSRF-Task-2021/blob/master/assets/nodes_graph.png)



## TODO:

[x] Add about docker: https://github.com/PXLAIRobotics/ROS2FoxyDocker/blob/master/02_run_container.sh

[x] Add about steps and modification to run the dockerfile

[x] Write about creating the packages

[0.8] Write steps to run all the stuff

[ ] Write about concepts of custom messages, publishers and subscribers

[ ] Write small documentation about creating packages

[ ] Add references: https://docs.ros.org/en/foxy/Tutorials/Creating-Your-First-ROS2-Package.html , https://docs.ros.org/en/foxy/Tutorials/Writing-A-Simple-Py-Publisher-And-Subscriber.html , https://docs.ros.org/en/foxy/Tutorials/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html

[ ] Write about the build of the custom message interface before the build