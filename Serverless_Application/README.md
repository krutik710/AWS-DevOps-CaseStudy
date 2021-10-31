# Problem Statement: 
Develop a lambda function which will work as a CSV importer into a data storage. Lambda
function will be triggered when a CSV file is uploaded to S3 and will write it’s contents to a data
storage.

**Implemented Solution:**

A CFT to deploy lambda and enable triggers on S3 upload for execution. 
Uploaded CSV data will be processed and stored in DynamoDB.
Create a separate repo for CICD to push Lambda code.

Note: Primary S3 bucket and DB will not be included in CFT and Python3 will be used throughout the repo as primary coding language (as I'm quite familiar to it)

**Steps:**
---

**Initial Resource Setup**
1. Create S3 bucket - for storing lambda artifacts 
(added my name as prefix to ensure no conflicts in creation)
2. Create DynamoDB with on demand provisioning 
(as its not going to be actively used)
3. The resources can be generated using resource_generator.py in this directory 
4. Download required dependencies
5. Configure AWS in local system
6. Run the script by specifying required parameters (find more details in script)
---

**Creating Infra for Lambda, S3 Bucket, IAM role and triggers**
3. Creating lambda from console to test code before using CFT
4. Zip lambda code and upload to S3 with correct versioning which can be specified in CFT input
5. Create CFT stack and deploy serverless_cft.yml to boot up lambda function, role that needs to be attached with the lambda, S3 bucket with attached trigger specific to csv put operation 

---
**Steps for setting up CICD for Lambda Code -** 
1. Created new repo - https://github.com/krutik710/AWS-DevOps-CaseStudy-ServerlessApplication
2. Added lambda code
3. Added AWS Access key and Secret key to Project Secrets
4. Configure Github Actions to deploy lambda - .github/workflows/lambda.yml 
5. Thus, now we can use this repo as CICD to push code to lambda directly 
