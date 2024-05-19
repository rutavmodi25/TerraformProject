import os
import subprocess
from templates import naming_module_template, parent_module_template, test_module_template

# Define the directory structure and corresponding templates
directory_structure = {
    "naming_module": {
        "main.tf": naming_module_template,
    },
    "parent_module": {
        "main.tf": parent_module_template,
    },
    "test": {
        "main.tf": test_module_template,
    },
}

# Create the directories and files based on the templates
for dir_name, files in directory_structure.items():
    os.makedirs(dir_name, exist_ok=True)
    for file_name, content in files.items():
        with open(os.path.join(dir_name, file_name), 'w') as file:
            file.write(content)

print("Files and directories created successfully.")


def run_terraform_commands():
    # Change to the directory where your Terraform configuration is located
    terraform_directory = "/workspace/test"

    try:
        # Initialize the Terraform configuration
        subprocess.run(["terraform", "init"], check=True, cwd=terraform_directory)

        # Run Terraform plan
        subprocess.run(["terraform", "plan"], check=True, cwd=terraform_directory)

        # Apply the Terraform configuration
        subprocess.run(["terraform", "apply", "-auto-approve"], check=True, cwd=terraform_directory)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Terraform: {e}")


# Call the function to run the commands
run_terraform_commands()