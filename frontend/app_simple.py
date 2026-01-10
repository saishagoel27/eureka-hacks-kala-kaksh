from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Mock data to simulate a product database
productCatalog = {
    "saree": [
      { "name": "Banarasi Silk Saree", "price": 15999, "artist": "Meera Devi", "description": "Traditional gold zari work on pure silk", "image": "/static/images/saree/saree1.jpg" },
      { "name": "Kanjeevaram Saree", "price": 12999, "artist": "Lakshmi Arts", "description": "South Indian temple border design", "image": "/static/images/saree/saree2.jpg" }
    ],
    "painting": [
      { "name": "Madhubani Painting", "price": 3999, "artist": "Sunita Jha", "description": "Traditional Bihar folk art on handmade paper", "image": "/static/images/painting/madhubani1.jpg" },
      { "name": "Warli Art", "price": 2999, "artist": "Tribal Collective", "description": "Maharashtra tribal art with natural pigments", "image": "/static/images/painting/warli1.jpg" }
    ],
    "jewellery": [
      { "name": "Silver Oxidized Necklace", "price": 2499, "artist": "Jaipur Jewels", "description": "Traditional Rajasthani silver jewelry", "image": "/static/images/jewellery/silver1.jpg" },
      { "name": "Kundan Earrings", "price": 4999, "artist": "Royal Crafts", "description": "Gold-plated kundan with pearls", "image": "/static/images/jewellery/kundan1.jpg" }
    ]
}

@app.route('/api/all-products', methods=['GET'])
def get_all_products():
    all_products = []
    for category in productCatalog.values():
        all_products.extend(category)
    return jsonify({"products": all_products})

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/art_home.html')
def art_home():
    return render_template('art_home.html')

@app.route('/buy_home.html')
def buy_home():
    return render_template('buy_home.html')

@app.route('/seller_upload.html')
def seller_upload():
    return render_template('seller_upload.html')

@app.route('/product_detail.html')
def product_detail():
    return render_template('product_detail.html')

@app.route('/api/products/<category>')
def get_products_by_category(category):
    if category in productCatalog:
        return jsonify(productCatalog[category])
    else:
        return jsonify([])

# Simplified image generation endpoint - returns mock response
@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        data = request.get_json()
        product_type = data.get('product_type', '').lower()
        
        if not product_type:
            return jsonify({"error": "Product type not provided"}), 400

        # Mock response - in a real app, this would call Vertex AI
        mock_image_uri = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtc2l6ZT0iMTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGR5PSIuM2VtIj5Nb2NrIEltYWdlIGZvciB7cHJvZHVjdF90eXBlfTwvdGV4dD48L3N2Zz4="
        
        return jsonify({"image_uri": mock_image_uri})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Failed to generate image. Please try again."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# For Vercel deployment
handler = app