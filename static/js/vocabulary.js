  var addButtons = document.getElementsByClassName('add-to-list');
    for ( const addButton of addButtons) {
    // Add a click event listener to the button
        addButton.addEventListener('click', function() {
            // Send a POST request to the backend when the button is clicked
            axios.post('/user-vocabulary/words/actions/', {
                // Add any data you want to send to the backend
                word: addButton.dataset.word
            })
            .then(function(response) {
                // Handle the response from the backend
                console.log(response.data);
            })
            .catch(function(error) {
                // Handle errors
                console.error('Error:', error);
            });
        });
    }