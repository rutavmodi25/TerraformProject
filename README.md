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
  This command will create a Docker container based on the previously built image. It mounts the current directory ($(shell pwd)) inside the container at the WORKDIR location.
  This command will also execute the Python script which will create our terraform files and apply them. Also added a test module that will test our functionality and output our results.
# Launch Docker Shell
- To launch the docker shell, execute:

		make docker-shell
  This command will launch the docker shell.
run Terraform commands.

# Cleaning Up
- To remove the Docker image from your system, use:

		make docker-clean
This command will remove the Docker image with the specified IMAGE_NAME.

# How to Test

Step 1: Testing terraform code manually.

We have three modules, a test module, a parent module, and a naming module. Test module ==> parent module ==> naming module. To test our code.

 	a. Build a docker image that contains terraform using make docker-build. 
  	b. Launch the docker shell using make docker-shell. 
   	c. cd into the test module, do terraform init, this will initialize terraform, then do terraform apply, this will apply the main.tf in test folder, which will further call parent and naming module. 
  	
Step 2: Testing terraform code through code generation (python file).

 	a. Build a docker image that contains terraform using make docker-build. 
  	b. Do docker run, this will run our Python script that creates all three directories and applies them in order. 
	

# Result

- Once all the above commands are executed you will be able to see the **naming_module** and **parent_module** directory with their respective terraform files. Additionally, the test module has been added to ensure the functionalities of the code.
  <img width="1656" alt="Screenshot 2024-05-20 at 12 09 22 PM" src="https://github.com/rutavmodi25/TerraformProject/assets/69160502/952726b1-db64-4247-9c3a-5e2212ca139c">
  <img width="1358" alt="Screenshot 2024-05-29 at 6 46 31 PM" src="https://github.com/rutavmodi25/TerraformProject/assets/69160502/9c79eb04-8f1b-440a-a070-8d69f97e48d8">








