# Serverless Task Management System (AWS)

## Overview
This project is a **cloud-native, serverless task management backend** built using Amazon Web Services (AWS).  
It demonstrates how to design, implement, and reason about scalable backend systems using **managed cloud services** with **minimal operational cost**.

The system exposes RESTful APIs to create and retrieve tasks, persists data in DynamoDB, and is fully described using **Infrastructure as Code (IaC)**.

---

## Key Features
- Serverless backend using AWS Lambda
- REST APIs exposed via API Gateway
- Data persistence using DynamoDB (on-demand billing)
- Input validation with proper HTTP status codes
- Pagination support for scalable data access
- Infrastructure defined using AWS SAM (IaC)
- Environment separation (dev / prod) through parameterized templates
- Cost-aware design with no always-on resources

---

## Architecture
**High-level flow:**

Client  
→ API Gateway  
→ AWS Lambda  
→ DynamoDB  

All compute is event-driven and stateless. No servers are provisioned or managed manually.

---

## AWS Services Used
- **AWS Lambda** – Stateless serverless compute
- **Amazon API Gateway** – REST API exposure
- **Amazon DynamoDB** – NoSQL data storage (PAY_PER_REQUEST)
- **AWS IAM** – Least-privilege access control
- **AWS SAM (Serverless Application Model)** – Infrastructure as Code

---

## API Endpoints

### Create Task
**POST** `/tasks`

**Request Body**
```json
{
  "title": "Finish cloud project"
}

Response

{
  "message": "Task created",
  "taskId": "uuid"
}

Get Tasks (Paginated)

GET /tasks?limit=5&lastKey=<taskId>

Response

{
  "items": [
    {
      "taskId": "uuid",
      "title": "Finish cloud project",
      "status": "TODO",
      "createdAt": "2026-01-30T10:15:00Z"
    }
  ],
  "nextKey": "uuid"
}

## Infrastructure as Code (IaC)

The entire backend infrastructure is defined in `template.yaml` using **AWS SAM**.

The template describes:
- DynamoDB table configuration  
- Lambda function definitions  
- API Gateway routes  
- IAM permissions with least privilege  
- Environment-based resource separation (`dev` / `prod`)  

This allows the system to be **recreated, reviewed, and version-controlled** without manual console configuration.

---

## Cost Considerations

This project is designed to minimize cloud costs:
- No EC2 or long-running services  
- DynamoDB uses on-demand billing  
- Lambda executes only on request  
- CloudWatch log retention can be limited  
- Fits within AWS Free Tier for development and testing  

---

## Folder Structure

.
├── template.yaml # Infrastructure as Code (AWS SAM)
├── create_task.py # Lambda: POST /tasks
├── get_tasks.py # Lambda: GET /tasks (paginated)
├── README.md
└── .gitignore


---

## Why Serverless?

- Automatic scaling without capacity planning  
- Pay-per-use pricing model  
- Reduced operational overhead  
- Built-in high availability  
- Ideal for event-driven backend systems  

---

## Future Improvements

- PATCH endpoint to update task status  
- Event-driven analytics using DynamoDB Streams  
- Authentication and authorization using Amazon Cognito  
- Frontend UI hosted on S3 and CloudFront  
- CI/CD pipeline for automated deployments  

---

## What This Project Demonstrates

- Cloud-native backend architecture  
- Serverless application design  
- Infrastructure as Code principles  
- Cost-aware engineering decisions  
- Real-world backend patterns beyond basic CRUD  

---

## Author

Built as a hands-on cloud engineering project to demonstrate **intermediate-level AWS and serverless system design**.
