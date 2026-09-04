# Task 3: Create a Serverless Function

## Objective
Create and deploy a serverless HTTP function using Python on Google Cloud and make it publicly accessible through an endpoint.

## Cloud Platform
Google Cloud Platform (GCP)

## Technologies Used
- Google Cloud Run Functions
- Python
- Functions Framework
- Flask
- HTTP / JSON

## Function Configuration
- **Service Name:** internspark-serverless-function
- **Region:** asia-south1
- **Runtime:** Python
- **Entry Point:** hello_http
- **Authentication:** Public access enabled

## Implementation
1. Opened Google Cloud Run.
2. Created a new serverless function.
3. Selected Python as the runtime.
4. Configured the function entry point as `hello_http`.
5. Added the Python code in `main.py`.
6. Enabled public access.
7. Deployed the function.
8. Verified that the deployment completed successfully.
9. Opened the public endpoint and confirmed the JSON response.

## Function Output

    {
      "language": "Python",
      "message": "Hello from InternSpark Serverless Function!",
      "platform": "Google Cloud Run",
      "status": "success"
    }

## Result
The serverless function was successfully deployed and returned the expected JSON response through a public HTTP endpoint.

## Internship Details
- **Internship:** InternSpark Cloud Computing Internship
- **Candidate Name:** Syed Haseebullah Hussaini
- **Candidate ID:** IS-2026-17285
- **Domain:** Cloud Computing
