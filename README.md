<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/default.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js"></script>


Welcome to the Django Pet Management System app.
This app keeps the track of pet vaccination.

Prerequisites

Before you begin, make sure you have the following:

Python 3.6 or newer
Django 3.1 or newer
Installation

To install the app, follow these steps:

Clone the repository
Navigate to the root directory of the repository i.e. wisdompets
Run the following command to install the required packages:

<pre><code class="python hljs">pip install -r requirements.txt</code></pre>

Usage

To start the development server, run the following command:

<pre><code class="python hljs">python manage.py runserver</code></pre>

Then, visit http://localhost:8000 in your web browser to view the app.




<script>
  document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('pre code').forEach((block) => {
      hljs.highlightBlock(block);
      const copyButton = document.createElement('button');
      copyButton.classList.add('copy-button');
      copyButton.innerHTML = 'Copy';
      block.parentNode.appendChild(copyButton);
      copyButton.addEventListener('click', () => {
        navigator.clipboard.writeText(block.innerText).then(() => {
          copyButton.innerHTML = 'Copied!';
          setTimeout(() => {
            copyButton.innerHTML = 'Copy';
          }, 1000);
        }, () => {
          copyButton.innerHTML = 'Error';
        });
      });
    });
  });
</script>