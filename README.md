
---

# Serverless Task Management System (AWS)

A **cloud-native, serverless task management backend** built on **Amazon Web Services (AWS)**.
This project demonstrates how to design and implement a **scalable, cost-efficient backend** using fully managed services and **Infrastructure as Code (IaC)**.

The system exposes RESTful APIs to create and retrieve tasks, persists data in DynamoDB, and runs without any always-on servers.

---

## Features

* Serverless backend using **AWS Lambda**
* REST APIs exposed via **Amazon API Gateway**
* Persistent storage with **Amazon DynamoDB (on-demand billing)**
* Input validation with proper HTTP status codes
* Pagination support for scalable reads
* Infrastructure defined using **AWS SAM**
* Environment separation (`dev` / `prod`) via parameterized templates
* Cost-aware design with no idle resources

---

## Architecture

**High-level flow:**

```
Client
  → API Gateway
    → AWS Lambda
      → DynamoDB
```

* All compute is **event-driven**
* Lambdas are **stateless**
* No servers or clusters to provision or manage

---

## AWS Services Used

* **AWS Lambda** – Serverless compute for API handlers
* **Amazon API Gateway** – REST API exposure
* **Amazon DynamoDB** – NoSQL datastore (PAY_PER_REQUEST)
* **AWS IAM** – Least-privilege access control
* **AWS SAM (Serverless Application Model)** – Infrastructure as Code

---

##  API Endpoints

### Create Task

**POST** `/tasks`

**Request Body**

```json
{
  "title": "Finish cloud project"
}
```

**Response**

```json
{
  "message": "Task created",
  "taskId": "uuid"
}
```

---

### Get Tasks (Paginated)

**GET** `/tasks?limit=5&lastKey=<taskId>`

**Response**

```json
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
```

---

## Infrastructure as Code (IaC)

All infrastructure is defined in `template.yaml` using **AWS SAM**.

The template includes:

* DynamoDB table configuration
* Lambda function definitions
* API Gateway routes
* IAM roles with least-privilege permissions
* Environment-based resource separation (`dev` / `prod`)

This allows the entire backend to be **recreated, reviewed, and version-controlled** without manual console setup.

---

## Cost Considerations

This project is designed to minimize AWS costs:

* No EC2 or long-running services
* DynamoDB uses **on-demand billing**
* Lambda runs **only on request**
* CloudWatch log retention can be limited
* Suitable for AWS Free Tier during development

---

## Project Structure

```
.
├── template.yaml      # AWS SAM infrastructure definition
├── create_task.py     # Lambda: POST /tasks
├── get_tasks.py       # Lambda: GET /tasks (paginated)
├── README.md
└── .gitignore
```

---

## Why Serverless?

* Automatic scaling without capacity planning
* Pay-per-use pricing model
* Reduced operational overhead
* Built-in high availability
* Ideal for event-driven backend systems

---

## Future Improvements

* PATCH endpoint to update task status
* Event-driven analytics using DynamoDB Streams
* Authentication and authorization using Amazon Cognito
* Frontend UI hosted on S3 and CloudFront
* CI/CD pipeline for automated deployments

---

## What This Project Demonstrates

* Cloud-native backend architecture
* Serverless application design
* Infrastructure as Code best practices
* Cost-aware engineering decisions
* Real-world backend patterns beyond basic CRUD

---

## Author

Built as a hands-on cloud engineering project to demonstrate **intermediate-level AWS and serverless system design**.

---
