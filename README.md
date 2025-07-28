# 🛒 Serverless E-Commerce Web Application on AWS

A fully serverless shopping cart web app built with AWS Lambda, API Gateway, DynamoDB, and S3. This app allows users to add, view, remove items, and update quantity from a shopping cart using a stateless REST API, with a static frontend hosted on S3.

---

## 🚀 Features

- Add to Cart (Lambda + DynamoDB)
- View Cart (Lambda + DynamoDB)
- Remove from Cart (Lambda + DynamoDB)
- Update Quantity (Lambda + DynamoDB)
- Frontend: HTML, CSS, JavaScript
- API Testing via Postman
- Logging with AWS CloudWatch
- Static Hosting via Amazon S3 or GitHub Pages

---

## 🧰 Tech Stack

| Frontend           | Backend              | Database          | Other AWS Services  |
|--------------------|----------------------|-------------------|---------------------|
| HTML, CSS,         | AWS Lambda (Python)  | AWS DynamoDB      | API Gateway, S3,    |
| JavaScript         |                      |                   | IAM, CloudWatch     |

---

## 📁 Project Structure

ecommerce-cart/
├── index.html
├── style.css
├── script.js
├── lambda/
│ ├── add_to_cart.py
│ ├── view_cart.py
│ ├── remove_from_cart.py
│ └── update_quantity.py
├── events/
│ ├── test_add.json
│ ├── test_view.json
│ ├── test_remove.json
│ └── test_update.json
├── requirements.txt
└── README.md

---

## 🛠️ Setup Instructions

### *1. Clone the repository*

git clone https://github.com/swetha-kasturi/aws-serverless-ecommerce-cart.git   
cd aws-serverless-ecommerce-cart
### *2. Setup Python environment for AWS Lambda functions*
cd lambda  
pip install -r ../requirements.txt -t .
### *3. Deploy Lambda Functions (via AWS Console or CLI)*
Create four Lambda functions:  
- add_to_cart  
- view_cart  
- remove_from_cart  
- update_quantity
  
Upload each corresponding .py file and attach IAM roles with permissions for:  
DynamoDB: PutItem, GetItem, UpdateItem, DeleteItem, Query  
CloudWatch Logs
### *4. Create and Configure DynamoDB Table*
- Table Name: CartTable  
- Partition Key: userId (String)  
- Sort Key: productId (String)  
### *5. Setup API Gateway*
Create a REST API with the following endpoints:

|Path	Method	|Lambda Function  | 
|-------------|-----------------|
|/add	POST	  |add_to_cart      |
|/view	POST	|view_cart        |
|/remove	POST|	remove_from_cart| 
|/update	POST|update_quantity  |

- Enable CORS on each method.  
- Deploy the API and note the Invoke URL.
### *6. Test Using Postman*
- Use the deployed API Gateway endpoint. 
- Set method to POST or GET. 
- In POST requests, use raw JSON body with    
Content-Type: application/json.

📬 Test API with Postman
Set Headers:
Content-Type: application/json

Use these JSON bodies with POST requests:

#### - ➕ Add to Cart (/add)
{
  "userId": "user123",
  "productId": "prod567",
  "quantity": 2
}
#### 👀 View Cart (/view)
{
  "userId": "user123"
}
#### ❌ Remove from Cart (/remove)
{
  "userId": "user123",
  "productId": "prod567"
}
#### 🔁 Update Quantity (/update)
{
  "userId": "user123",
  "productId": "prod567",
  "quantity": 3
}

🔗 Live URLs  
🛒 Frontend (S3 Hosted)  
   Visit App  

🧪 Lambda Test URLs (API Gateway Endpoints)  
#### Add to Cart:
https://654eqnm8ah.execute-api.ap-south-1.amazonaws.com/prod/add-to-cart

#### View Cart:
https://654eqnm8ah.execute-api.ap-south-1.amazonaws.com/prod/view-cart

#### Remove from Cart:
https://654eqnm8ah.execute-api.ap-south-1.amazonaws.com/prod/remove-from-cart

#### Update Quantity:
https://654eqnm8ah.execute-api.ap-south-1.amazonaws.com/prod/update
