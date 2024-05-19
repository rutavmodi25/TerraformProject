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

