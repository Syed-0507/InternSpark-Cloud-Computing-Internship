# Task 2: Deploy a Virtual Machine and Install a Web Server

## Objective
Create an Ubuntu virtual machine on Google Cloud, configure HTTP access, install Nginx, and host a custom webpage accessible through the VM's public IP address.

## Cloud Platform
Google Cloud Platform (GCP)

## Technologies Used
- Google Compute Engine
- Ubuntu 24.04 LTS
- Nginx
- SSH
- Google Cloud Firewall

## VM Configuration
- **VM Name:** internspark-cloud-vm
- **Region:** asia-south1
- **Zone:** asia-south1-c
- **Machine Type:** e2-micro
- **Operating System:** Ubuntu 24.04 LTS
- **HTTP Traffic:** Enabled
- **Web Server:** Nginx

## Commands Used

1. Update package list:

    sudo apt update

2. Install Nginx:

    sudo apt install nginx -y

3. Check Nginx status:

    sudo systemctl status nginx

4. Create the custom webpage:

        echo "&lt;h1&gt;Hello from Cloud VM&lt;/h1&gt;" | sudo tee /var/www/html/index.html

## Implementation

1. Created an Ubuntu virtual machine using Google Compute Engine.
2. Selected the `e2-micro` machine type.
3. Used Ubuntu 24.04 LTS as the operating system.
4. Enabled HTTP traffic for the virtual machine.
5. Connected to the VM using the Google Cloud SSH terminal.
6. Updated the Ubuntu package list.
7. Installed the Nginx web server.
8. Verified that Nginx was active and running.
9. Replaced the default Nginx webpage with a custom webpage.
10. Accessed the webpage using the VM's external IP address.
11. Verified that the browser displayed "Hello from Cloud VM".

## Output

The deployed webpage displayed:

**Hello from Cloud VM**

## Result

The Google Compute Engine virtual machine was successfully created and configured. Nginx was installed and the custom webpage was successfully hosted and publicly accessible through the VM's external IP address.

## Internship Details

- **Internship:** InternSpark Cloud Computing Internship
- **Candidate Name:** Syed Haseebullah Hussaini
- **Candidate ID:** IS-2026-17285
- **Domain:** Cloud Computing
