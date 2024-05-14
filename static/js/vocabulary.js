  var addButtons = document.getElementsByClassName('add-to-list');
  var addRoute = document.getElementById('word_add_route');
  console.log(addButtons)
    for ( const addButton of addButtons) {
    // Add a click event listener to the button
        addButton.addEventListener('click', function() {
        console.log(addButton)
            // Send a POST request to the backend when the button is clicked
            axios.post(addRoute.value, {
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


  var removeButtons = document.getElementsByClassName('remove-from-list');
  var removeRoute = document.getElementById('word_add_route');
  for ( const removeButton of removeButtons) {
        removeButton.addEventListener('click', function() {
            axios.delete(addRoute.value, { data: {
                word: removeButton.dataset.word,
                page: document.getElementById('word_heading') ? 'word' : 'list'
            }})
            .then(function(response) {
                if (response.data.redirect) {
                    location.href = response.data.redirect;
                } else {
                    removeButton.parentElement.parentElement.remove();
                }
            })
            .catch(function(error) {
                console.error('Error:', error);
            });
        });
    }

