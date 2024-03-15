<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../static/style.css">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        header {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 20px 0;
        }

        .cart-container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            border: 1px solid #ccc;
        }

        .cart-item {
            margin-bottom: 10px;
        }

        .cart-item img {
            width: 50px;
            height: auto;
            margin-right: 10px;
        }

        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 20px 0;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
    <title>Handlekurv</title>
</head>
<body>
    <header>
        <h1>Handlekurv</h1>
    </header>

    <div class="cart-container" id="cartContainer">
        <!-- Handlekurvinnholdet vil bli lagt til her dynamisk ved hjelp av JavaScript -->
    </div>

    <footer>
        <p>&copy; 2024 Nettbutikk</p>
    </footer>

    <script>
        // Simulerer handlekurvdata
        var cartItems = [
            {
                name: "IdeaPad Slim 3 14i",
                image: "../Bilder/lenovo.webp",
                price: 6419,
                quantity: 1
            }
            // Legg til flere handlekurv-elementer etter behov
        ];

        // Funksjon for å vise handlekurven
        function displayCart() {
            var cartContainer = document.getElementById("cartContainer");
            cartContainer.innerHTML = "";

            cartItems.forEach(function(item) {
                var cartItemDiv = document.createElement("div");
                cartItemDiv.classList.add("cart-item");

                var image = document.createElement("img");
                image.src = item.image;
                var name = document.createTextNode(item.name);
                var price = document.createTextNode("Pris: " + item.price + " kr");
                var quantity = document.createTextNode("Antall: " + item.quantity);

                cartItemDiv.appendChild(image);
                cartItemDiv.appendChild(name);
                cartItemDiv.appendChild(document.createElement("br"));
                cartItemDiv.appendChild(price);
                cartItemDiv.appendChild(document.createElement("br"));
                cartItemDiv.appendChild(quantity);

                cartContainer.appendChild(cartItemDiv);
            });
        }

        // Vis handlekurven ved lasting av siden
        displayCart();
    </script>
</body>
</html>
