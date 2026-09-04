# Task 4: Deploy a Docker Container on Cloud VM

## Objective
Install Docker on a Google Cloud virtual machine, deploy an Nginx container, expose it to the internet, and verify the containerized web server using the VM's public IP address.

## Cloud Platform
Google Cloud Platform (GCP)

## Technologies Used
- Google Compute Engine
- Ubuntu 24.04 LTS
- Docker
- Nginx
- Google Cloud VPC Firewall
- SSH

## VM Configuration
- **VM Name:** internspark-cloud-vm
- **Region:** asia-south1
- **Zone:** asia-south1-c
- **Operating System:** Ubuntu 24.04 LTS
- **Docker Container Name:** internspark-nginx
- **Docker Image:** nginx
- **Container Port:** 80
- **Public Port:** 8080

## Commands Used

1. Update package list:

    sudo apt update

2. Install Docker:

    sudo apt install docker.io -y

3. Enable and start Docker:

    sudo systemctl enable --now docker

4. Verify Docker installation:

    docker --version

5. Run the Nginx Docker container:

    sudo docker run -d --name internspark-nginx -p 8080:80 nginx

6. Verify the running container:

    sudo docker ps

## Firewall Configuration

A Google Cloud VPC firewall rule was created with the following settings:

- **Rule Name:** allow-docker-8080
- **Direction:** Ingress
- **Action:** Allow
- **Target Tag:** http-server
- **Source IPv4 Range:** 0.0.0.0/0
- **Protocol:** TCP
- **Port:** 8080

## Implementation

1. Connected to the existing Google Compute Engine VM using SSH.
2. Updated the Ubuntu package list.
3. Installed Docker on the VM.
4. Enabled and started the Docker service.
5. Verified Docker using the `docker --version` command.
6. Downloaded the official Nginx Docker image.
7. Created a Docker container named `internspark-nginx`.
8. Mapped VM port `8080` to container port `80`.
9. Verified the running container using `docker ps`.
10. Created a firewall rule to allow incoming TCP traffic on port 8080.
11. Opened the VM's public IP address with port 8080 in the browser.
12. Verified that the Nginx welcome page was successfully displayed.

## Public URL

http://35.200.181.149:8080

## Result

The Nginx Docker container was successfully deployed on the Google Cloud VM and made publicly accessible through port 8080. The browser successfully displayed the default Nginx welcome page.

## Internship Details

- **Internship:** InternSpark Cloud Computing Internship
- **Candidate Name:** Syed Haseebullah Hussaini
- **Candidate ID:** IS-2026-17285
- **Domain:** Cloud Computing
