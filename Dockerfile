FROM hashicorp/terraform:latest

# Install Python
RUN apk add --no-cache python3 py3-pip

# Set the working directory
WORKDIR /workspace

# Copy the Python script into the container
COPY terraform-project.py .

# Override the default entrypoint
ENTRYPOINT ["/bin/sh", "-c"]

# Run the Python script
CMD ["python3 terraform-project.py"]
