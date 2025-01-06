document.addEventListener('DOMContentLoaded', () => {
  const categorySelect = document.getElementById('category-select');
  const quoteDisplay = document.getElementById('quote-display');

  // Fetch and load JSON data
  fetch('./quotes.json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to load quotes JSON.');
      }
      return response.json();
    })
    .then(quotes => {
      populateCategories(quotes); // Populate categories in the dropdown
      setupCategorySelection(quotes); // Handle selection and display quotes
    })
    .catch(error => {
      console.error('Error:', error);
      quoteDisplay.innerHTML = `<p>Error loading quotes: ${error.message}</p>`;
    });

  // Populate dropdown with categories
  function populateCategories(quotes) {
    Object.keys(quotes).forEach(category => {
      const option = document.createElement('option');
      option.value = category; // Use the category name as the value
      option.textContent = category; // Display the category name
      categorySelect.appendChild(option); // Add the option to the dropdown
    });
  }

  // Display quotes for selected category
  function setupCategorySelection(quotes) {
    categorySelect.addEventListener('change', () => {
      const selectedCategory = categorySelect.value;
      const categoryQuotes = quotes[selectedCategory];

      // Clear existing content
      quoteDisplay.innerHTML = '';

      if (categoryQuotes && categoryQuotes.length > 0) {
        // Add numbered quotes to the display
        categoryQuotes.forEach((quote, index) => {
          const quoteElement = document.createElement('div');
          quoteElement.className = 'quote-card'; // Optional styling class
          quoteElement.innerHTML = `<strong>${index + 1}.</strong> ${quote}`;
          quoteElement.style.marginBottom = '10px'; // Add spacing between quotes
          quoteDisplay.appendChild(quoteElement);
        });
      } else {
        quoteDisplay.innerHTML = `<p>No quotes found for "${selectedCategory}".</p>`;
      }
    });
  }
});

