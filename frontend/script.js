const BASE_URL = "https://654eqnm8ah.execute-api.ap-south-1.amazonaws.com/prod";

function addToCart() {
  const userId = "user123";
  const productId = "prod567";
  const quantity = 1;

  fetch(`${BASE_URL}/add-to-cart`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ userId, productId, quantity })
  })
  .then(response => response.json())
  .then(data => alert("Added to cart!"))
  .catch(error => alert("Error: " + error));
}

function viewCart() {
  const userId = "user123";

  fetch(`${BASE_URL}/view-cart?userId=${userId}`)
    .then(response => response.json())
    .then(data => {
      alert("Cart Contents: " + JSON.stringify(data));
    })
    .catch(error => alert("Error: " + error));
}

function removeFromCart() {
  const userId = "user123";
  const productId = "prod567";

  fetch(`${BASE_URL}/remove-from-cart`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ userId, productId })
  })
  .then(response => response.json())
  .then(data => alert("Removed from cart"))
  .catch(error => alert("Error: " + error));
}

function updateQuantity() {
  const userId = "user123";
  const productId = document.getElementById("productId").value;
  const quantity = parseInt(document.getElementById("newQuantity").value);

  fetch(`${BASE_URL}/update`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ userId, productId, quantity })
  })
  .then(response => response.json())
  .then(data => alert("Quantity updated!"))
  .catch(error => alert("Error: " + error));
}
