  var addButtons = document.getElementsByClassName('add-to-list');
    for ( const addButton of addButtons) {
    // Add a click event listener to the button
        addButton.addEventListener('click', function() {
            // Send a POST request to the backend when the button is clicked
            axios.post('/user-vocabulary/words/', {
                // Add any data you want to send to the backend
                word: addButton.dataset.word,
                page: document.getElementById('not-saved') ? 'word' : 'list'
            })
            .then(function(response) {
                // Handle the response from the backend
                if (response.data.redirect) {
                    location.href = response.data.redirect;
                }
            })
            .catch(function(error) {
                // Handle errors
                console.error('Error:', error);
            });
        });
    }