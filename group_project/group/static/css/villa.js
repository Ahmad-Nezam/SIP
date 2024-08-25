function filterVillas() {
    var selectedRoom = $('#room-filter').val();
    
    $('.villa-card').each(function() {
        var villaRooms = $(this).data('rooms');
        if (selectedRoom === '' || villaRooms == selectedRoom) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}

$(document).ready(function() {
  
    filterVillas();

  
    $('#filter-form').on('submit', function(event) {
        event.preventDefault(); 
        filterVillas();
    });
});



document.getElementById('commentForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const comment = document.getElementById('comment').value;

    // Example API call (replace with your API endpoint)
    fetch('https://your-api-endpoint.com/send-email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            comment: comment
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Your comment has been sent successfully!');
        } else {
            alert('There was an error sending your comment. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('There was an error sending your comment. Please try again.');
    });
});


fetch('/api/send-comment', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        email: email,
        comment: comment
    }),
})
