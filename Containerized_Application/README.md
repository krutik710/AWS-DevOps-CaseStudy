# Problem Statement: 
Create an application that will calculate the factorial of a non-negative integer provided by the user and return
the value. You can expose the containerized application via a Load Balancer.

**Implemented Solution:**

Create a Flask application to perform the required action.
Create a separate repo for CICD to push built image to ECR and then to ECS.

**Steps:**
---

**Application **
1. Create Flask application (as its light weight and faster to implement, no concurrency or guicorn or parallel/async operations required)
2. Including 2 endpoints - 1 for dummy landing and taking input, 2nd for getting factorial of passed number
3. Create Dockerfile
---

**Infra**
1. Create ECR repository - 
aws ecr create-repository \
    --repository-name FactorialFlaskApp \
    --region ap-south-1
2. Upload locally built image to repo - first tag image to ecr name and then push
3. Create CFT for deploying ECS service - have used exisiting template from https://templates.cloudonaut.io/en/stable/ecs/ - using the 'Using a dedicated load balancer for the service' version for this demo
4. Use the stack from the above link and modify as per our project requirements
5. Deploy all stacks and ECS will be up and running 

---
**Steps for setting up CICD for Flask App Code -** 
1. Created new repo - https://github.com/krutik710/AWS-DevOps-CaseStudy-ContainerizedApplication
2. Added flask code 
3. Added AWS Access key, Secret key, region to Project Secrets
4. Added task definition of created task in ecs - aws ecs describe-task-definition --task-definition <task-name>:<version> 
5. Configure Github Actions to deploy lambda - .github/workflows/aws.yml 
6. Thus, now we can use this repo as CICD to push code to ecs directly and it handles the deployment for us 
