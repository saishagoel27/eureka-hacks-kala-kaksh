from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import base64
import os

app = Flask(__name__)
CORS(app)  # This will enable cross-origin requests

# Replace with your Google Cloud Project ID and location
PROJECT_ID = "dark-geography-472317-i7"
LOCATION = "asia-south1"

# Mock data to simulate a product database
productCatalog = {
    "saree": [
      { "name": "Banarasi Silk Saree", "price": 15999, "artist": "Meera Devi", "description": "Traditional gold zari work on pure silk", "image": r"C:\Users\DELL\Desktop\KK\static\images\saree\saree1.jpg" },
      { "name": "Kanjeevaram Saree", "price": 12999, "artist": "Lakshmi Arts", "description": "South Indian temple border design", "image": r"C:\Users\DELL\Desktop\KK\static\images\saree\saree2.jpg" }
    ],
    "painting": [
      { "name": "Madhubani Painting", "price": 3999, "artist": "Sunita Jha", "description": "Traditional Bihar folk art on handmade paper", "image": r"C:\Users\DELL\Desktop\KK\static\images\painting\madhubani1.jpg" },
      { "name": "Warli Art", "price": 2999, "artist": "Tribal Collective", "description": "Maharashtra tribal art with natural pigments", "image": r"C:\Users\DELL\Desktop\KK\static\images\painting\warli1.jpg" }
    ],
    "jewellery": [
      { "name": "Silver Oxidized Necklace", "price": 2499, "artist": "Jaipur Jewels", "description": "Traditional Rajasthani silver jewelry", "image": r"C:\Users\DELL\Desktop\KK\static\images\jewellery\silver1.jpg" },
      { "name": "Kundan Earrings", "price": 4999, "artist": "Royal Crafts", "description": "Gold-plated kundan with pearls", "image": r"C:\Users\DELL\Desktop\KK\static\images\jewellery\kundan1.jpg" }
    ]
}


# Add this new route to your Flask app
@app.route('/api/all-products', methods=['GET'])
def get_all_products():
    all_products = []
    # Loop through the mock product catalog to get all products
    for category in productCatalog.values():
        all_products.extend(category)
    
    return jsonify({"products": all_products})

vertexai.init(project=PROJECT_ID, location=LOCATION)
model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

# Add a route to serve your login page
@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/product_detail.html')
def view_all_products():
    # You can fetch products from a database here and pass them to the template
    # products = get_all_products_from_db()
    # return render_template('product_detail.html', products=products)
    return render_template('product_detail.html')

# Add a route to serve your buyer page
@app.route('/buy_home.html')
def buy_home():
    return render_template('buy_home.html')

@app.route('/loading.html')
def loading():
    return render_template('loading.html')
# Add a route to serve your artisan page
@app.route('/art_home.html')
def art_home():
    return render_template('art_home.html')

@app.route('/api/generate-realtime', methods=['POST'])
def generate_realtime_image():
    try:
        data = request.json
        product_type = data.get('product')

        if not product_type:
            return jsonify({"error": "Product type not provided"}), 400

        # Construct a dynamic and detailed prompt
        prompt = f"A cozy Indian aesthetic room with a handwoven {product_type} as the centerpiece. The image should be professionally shot, well-lit, and showcase traditional Indian craftsmanship."
        
        print(f"Generating image for prompt: '{prompt}'...")

        # Call the Vertex AI API to generate a single image
        images_result = model.generate_images(prompt=prompt, number_of_images=3)
        
        # Get the bytes data from the generated image
        image_bytes = images_result[0]._image_bytes
        
        # Encode the bytes into a Base64 string
        base64_encoded_image = base64.b64encode(image_bytes).decode('utf-8')

        # Create a data URI to be used directly in the <img> tag
        image_uri = f"data:image/jpeg;base64,{base64_encoded_image}"

        return jsonify({"image_uri": image_uri})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Failed to generate image. Please try again."}), 500

if __name__ == '__main__':
    # Running on 0.0.0.0 makes the server accessible on your network
    app.run(debug=True, host='0.0.0.0', port=5000)