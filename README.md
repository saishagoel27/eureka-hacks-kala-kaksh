# 🎨 Kala Kaksh - AI-Powered Artisan Marketplace

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Platform-4285F4.svg)](https://cloud.google.com)
[![Vertex AI](https://img.shields.io/badge/Vertex%20AI-Enabled-orange.svg)](https://cloud.google.com/vertex-ai)
[![Imagen AI](https://img.shields.io/badge/Imagen%20AI-3.0-red.svg)](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


</div>

## 🌟 Overview

**Kala Kaksh** is a revolutionary platform that bridges the gap between traditional Indian artisans and modern buyers through the power of AI. Our platform combines authentic handcrafted treasures with cutting-edge technology, offering AI-generated room visualizations powered by Google's Vertex AI and Imagen 3.0.

*"Where tradition meets technology, shaping the majestic future of artisan shopping"*

## 🏛️ Project Architecture

For better understanding of the complete project implementation, please check our backend repository that handles core functionalities:

**🔗 Backend Repository**: [Kala-Kaksh](https://github.com/saishagoel27/Kala-Kaksh)
- Database management and API endpoints
- Product catalog and inventory management
> This repository focuses on the AI-powered frontend features, while the backend repository contains the core marketplace functionalities.

## ✨ Key Features

### 🎭 For Artisans
- **Digital Showcase**: Create beautiful profiles to display your craft and story
- **Product Management**: Easily add and manage your handcrafted products
- **AI Enhancement**: Leverage Vertex AI to enhance product descriptions
- **Collaboration Network**: Connect with fellow artisans for partnerships
- **Story Telling**: Share your artistic journey and cultural heritage

### 🛍️ For Buyers
- **AI Room Generation**: Visualize products in custom-generated rooms using Imagen 3.0
- **Curated Discovery**: Browse authentic handcrafted items by category
- **Artisan Stories**: Learn about the makers behind each product
- **Smart Shopping**: Cart management and purchase history
- **Personalized Experience**: Save preferences and wishlist items

### 🤖 AI-Powered Features
- **Real-time Image Generation**: Generate custom room designs
- **Enhanced Descriptions**: AI-powered product and story enhancement
- **Visual Commerce**: See how products look in beautifully designed spaces

## 📸 Screenshots

### Artisan Dashboard - Collaboration Network
![WhatsApp Image 2025-09-21 at 22 38 37_68c8b558](https://github.com/user-attachments/assets/3c0a66bf-2dfd-4a11-a27d-6b467979adb6)

*Connect with fellow artisans and build meaningful partnerships*

### AI-Generated Room Visualization
![WhatsApp Image 2025-09-21 at 22 28 12_de1da27e](https://github.com/user-attachments/assets/946c7e1b-c504-4d6b-b300-bea11adbb866)

*Custom room generated with traditional Indian handicrafts using Google Imagen*

### Buyer Shopping Experience
![WhatsApp Image 2025-09-21 at 22 26 05_b34c5939](https://github.com/user-attachments/assets/7734a196-8773-4512-b1fe-522b188ef291)

*Discover authentic handcrafted products by category*

### Product Gallery with AI Visualization
![WhatsApp Image 2025-09-21 at 22 25 33_d90ecec4](https://github.com/user-attachments/assets/8a413423-2683-47a3-934b-68e7a81abe64)

*Browse pottery and ceramics in AI-generated traditional settings*

### Welcome Experience
![WhatsApp Image 2025-09-21 at 22 26 26_63be6328](https://github.com/user-attachments/assets/21e66031-900a-4d3a-8789-eb79f67bfe6b)

*Beautiful introduction to the world of Indian handicrafts*

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Cloud Project with Vertex AI enabled
- Flask development environment

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/kala-kaksh.git
   cd kala-kaksh
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Google Cloud**
   ```bash
   # Set up your Google Cloud credentials
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
   ```

5. **Update configuration**
   Edit [`app.py`](Kala-kaksh_genai/app.py) and update:
   ```python
   PROJECT_ID = "your-google-cloud-project-id"
   LOCATION = "your-preferred-location"  # e.g., "asia-south1"
   ```

6. **Run the application**
   ```bash
   cd Kala-kaksh_genai
   python app.py
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 🏗️ Project Structure

```
Kala-kaksh_genai/
├── app.py                  # Main Flask application
├── generate_images.py      # AI image generation utility
├── static/                 # Static assets
│   ├── style.css          # Main stylesheet
│   ├── script.js          # Client-side JavaScript
│   └── images/            # Product images
│       ├── jewellery/
│       ├── painting/
│       └── saree/
└── templates/             # HTML templates
    ├── login.html         # Authentication page
    ├── art_home.html      # Artisan dashboard
    ├── buy_home.html      # Buyer dashboard
    ├── loading.html       # AI generation loading page
    └── product_detail.html # Product gallery
```

## 🔧 Technical Stack

### Backend
- **Flask**: Web framework for Python
- **Google Vertex AI**: AI/ML platform for image generation
- **Imagen 3.0**: State-of-the-art image generation model

### Frontend
- **HTML5 & CSS3**: Modern web standards
- **JavaScript (ES6+)**: Interactive functionality
- **Responsive Design**: Mobile-first approach

### AI Integration
- **Vertex AI SDK**: Google Cloud AI platform integration
- **Real-time Generation**: Dynamic image creation
- **Base64 Encoding**: Efficient image data transfer

## 🎨 Key Pages & Functionality

### Authentication System
- Google Sign-In integration
- Role-based access (Artisan/Buyer)
- Secure session management

### Artisan Features
- **Story Creation**: [`art_home.html`](Kala-kaksh_genai/templates/art_home.html)
- **Product Management**: Add, edit, and showcase products
- **AI Enhancement**: Improve descriptions with Vertex AI
- **Collaboration**: Connect with other artisans

### Buyer Features
- **Product Discovery**: [`buy_home.html`](Kala-kaksh_genai/templates/buy_home.html)
- **AI Room Generation**: Visualize products in custom spaces
- **Shopping Cart**: Manage purchases and wishlist
- **Artisan Profiles**: Learn about creators

### AI Integration
- **Image Generation**: [`/api/generate-realtime`](Kala-kaksh_genai/app.py) endpoint
- **Custom Prompts**: Dynamic room generation based on product types
- **Real-time Processing**: Live image generation and display

## 🌐 Product Categories

- **🥻 Handwoven Sarees**: Traditional silk and cotton sarees
- **🎨 Paintings & Art**: Miniature paintings, folk art, contemporary pieces
- **💎 Handcrafted Jewelry**: Silver, brass, and traditional jewelry
- **🏺 Pottery & Ceramics**: Terracotta, blue pottery, ceramic crafts
- **🥓 Handwoven Rugs**: Traditional carpets, dhurries, floor coverings

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- **Artisan Community**: For preserving traditional crafts and inspiring this platform
- **Google Cloud**: For providing cutting-edge AI capabilities through Vertex AI
- **Flask Community**: For the robust web framework
- **Open Source Contributors**: For making this project possible

<div align="center">
  <p><strong>Made with ❤️ for preserving traditional Indian craftsmanship</strong></p>
  <p><em>"Connecting hearts through hands, bridging tradition with technology"</em></p>
</div>
