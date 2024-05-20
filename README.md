# TerraformProject for UCLA Health

# Prerequisites
Docker installed on your system

# Building the Docker Image
- To build the Docker image, run the following command:

		make docker-build
This command will build the Docker image with the specified IMAGE_NAME and tag it as the latest.

# Running the Docker Container
- To run the Docker container interactively, execute:

		make docker-run
This command will create a Docker container based on the previously built image. It mounts the current directory ($(shell pwd)) inside the container at the WORKDIR location. You can interact with the container's shell to run Terraform commands.

This command will also execute the Python script which will create our terraform files and apply them. Also added a test module that will test our functionality and output our results.

# Cleaning Up
- To remove the Docker image from your system, use:
 make docker-clean

		make docker-clean
This command will remove the Docker image with the specified IMAGE_NAME.

# Result

- Once all the above commands are executed you will be able to see the **naming_module** and **parent_module** directory with their respective terraform files.
  
<img width="1700" alt="Screenshot 2024-05-19 at 5 29 47 PM" src="https://github.com/rutavmodi25/TerraformProject/assets/69160502/87d31d52-d894-4901-b1bf-bc7423e2e623">


