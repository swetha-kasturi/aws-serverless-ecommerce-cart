# 🛒 Serverless E-Commerce Web Application on AWS

A fully serverless shopping cart web app built with AWS Lambda, API Gateway, DynamoDB, and S3. This app allows users to add, view, and remove items from a shopping cart using a stateless REST API, with a static frontend hosted on S3.

---

## 🚀 Features

- Add to Cart (Lambda + DynamoDB)
- View Cart (Lambda + DynamoDB)
- Remove from Cart (Lambda + DynamoDB)
- Frontend: HTML, CSS, JavaScript
- API Testing via Postman
- Logging with AWS CloudWatch
- Static Hosting via Amazon S3 or GitHub Pages

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: AWS Lambda (Python)
- **Database**: AWS DynamoDB
- **Other AWS Services**: API Gateway, S3, IAM, CloudWatch

---

## 📁 Project Structure

ecommerce-cart/
├── index.html
├── style.css
├── script.js
├── lambda/
│ ├── add_to_cart.py
│ ├── view_cart.py
│ └── remove_from_cart.py
├── events/
│ ├── test_add.json
│ ├── test_view.json
│ └── test_remove.json
├── requirements.txt
└── README.md

---

## 🛠️ Setup Instructions

### *1. Clone the repository*

```bash
git clone https://github.com/your-username/ecommerce-cart.git
cd ecommerce-cart
***2. Setup Python environment for AWS Lambda functions***
cd lambda
pip install -r ../requirements.txt -t .
3. Deploy Lambda Functions
Use the AWS Console to:
Create three Lambda functions (add_to_cart, view_cart, remove_from_cart)
Upload each corresponding .py file
Attach correct IAM role with access to DynamoDB and CloudWatch
4. Create and Configure DynamoDB Table
Table Name: CartTable
Partition Key: userId (String)
Sort Key: productId (String)
5. Setup API Gateway
Create a REST API with three POST methods:
/add → add_to_cart Lambda
/view → view_cart Lambda
/remove → remove_from_cart Lambda
Enable CORS
Deploy API and note the Invoke URL

📬 Test API with Postman
Use these JSON bodies with POST requests:

➕ Add to Cart (/add)
{
  "userId": "user123",
  "productId": "prod567",
  "quantity": 2
}
👀 View Cart (/view)
{
  "userId": "user123"
}
❌ Remove from Cart (/remove)
{
  "userId": "user123",
  "productId": "prod567"
}
