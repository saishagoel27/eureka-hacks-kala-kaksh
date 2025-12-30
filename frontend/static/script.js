// This is the function that handles the Google Sign-In response.
// It is called by the Google Identity Services library.
function handleCredentialResponse(response) {
  // For a quick, unsecured demonstration, redirect directly.
  // In a production app, you would send this token to your backend for verification.
  try {
    const decoded = JSON.parse(atob(response.credential.split('.')[1]));
    console.log('User logged in:', decoded);
    // Redirect to the buyer's home page upon successful login
    window.location.href = "buy_home.html";
  } catch (e) {
    console.error('Error decoding JWT token:', e);
    alert('Login failed. Please try again.');
  }
}

// Function to handle the "Register as Artisan" button click.
function navigateToArtisan() {
  alert('Redirecting to Artisan Page');
  // Redirect to the artisan's home page
  window.location.href = 'art_home.html';
}

// Function to handle the "Register as Buyer" button click.
function navigateToBuyer() {
  alert('Redirecting to Buyer Page');
  // Redirect to the buyer's home page
  window.location.href = 'buy_home.html';
}

// This is the main block that runs after the entire HTML document is loaded.
// All code that needs to interact with HTML elements should be inside this.
document.addEventListener('DOMContentLoaded', function() {
  // Attach event listener for the "Register as Artisan" button.
  const artisanBtn = document.getElementById('register-artisan');
  if (artisanBtn) {
    artisanBtn.addEventListener('click', navigateToArtisan);
    console.log("Artisan button listener attached.");
  } else {
    console.error("Artisan button not found!");
  }

  // Attach event listener for the "Register as Buyer" button.
  const buyerBtn = document.getElementById('register-buyer');
  if (buyerBtn) {
    buyerBtn.addEventListener('click', navigateToBuyer);
    console.log("Buyer button listener attached.");
  } else {
    console.error("Buyer button not found!");
  }

  
  // Attach event listener for the "View All Products" button (on a different page).
  // This is a defensive check to prevent errors on the login page.
  const viewAllProductsBtn = document.getElementById('viewAllProductsBtn');
  if (viewAllProductsBtn) {
    viewAllProductsBtn.addEventListener('click', function() {
      window.location.href = '/products';
    });
    console.log("View All Products button listener attached.");
  }

  // Add subtle hover effects to all buttons with the class 'palace-btn'.
  const buttons = document.querySelectorAll('.palace-btn');
  buttons.forEach(button => {
    button.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-2px)';
    });
    button.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });

  // Add subtle floating animation to the motifs.
  const motifs = document.querySelectorAll('.motif');
  motifs.forEach((motif, index) => {
    motif.style.animation = `float ${3 + index * 0.5}s ease-in-out infinite alternate`;
  });
});


// This code creates a dynamic style tag for the CSS animation.
// It's placed outside the DOMContentLoaded event because it doesn't rely on HTML elements.
const style = document.createElement('style');
style.textContent = `
  @keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    100% { transform: translateY(-10px) rotate(2deg); }
  }
`;
document.head.appendChild(style);