


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
