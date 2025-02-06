// Load existing posts when page loads
document.addEventListener('DOMContentLoaded', () => {
    loadPosts();
  });
  
  // Handle form submission
  document.getElementById('postForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const author = document.getElementById('author').value;
    const content = document.getElementById('content').value;
    const imageInput = document.getElementById('imageInput');
    
    // Convert image to Base64 for storage
    const reader = new FileReader();
    if (imageInput.files[0]) {
      reader.readAsDataURL(imageInput.files[0]);
    }
  
    reader.onload = function() {
      // Create post object
      const post = {
        author: author,
        content: content,
        image: reader.result || null,
        date: new Date().toLocaleString()
      };
  
      // Save and display the post
      savePost(post);
      addPostToDOM(post);
      this.reset();
    }.bind(this);
  });
  
  // Save post to localStorage
  function savePost(post) {
    let posts = JSON.parse(localStorage.getItem('posts')) || [];
    posts.unshift(post); // Add new post to top
    localStorage.setItem('posts', JSON.stringify(posts));
  }
  
  // Load posts from localStorage
  function loadPosts() {
    const posts = JSON.parse(localStorage.getItem('posts')) || [];
    posts.forEach(post => addPostToDOM(post));
  }
  
  // Display posts in the DOM
  function addPostToDOM(post) {
    const postsContainer = document.getElementById('postsContainer');
    
    const postElement = document.createElement('div');
    postElement.className = 'post';
    postElement.innerHTML = `
      <div class="post-author">${post.author}</div>
      <div class="post-date">${post.date}</div>
      <div class="post-content">${post.content}</div>
      ${post.image ? `<img src="${post.image}" alt="Post image">` : ''}
    `;
  
    // Add new post to the top of the list
    postsContainer.appendChild(postElement);
  }