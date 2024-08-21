document.getElementById('bookingForm').addEventListener('submit', function(event) {
    var startDate = new Date(document.getElementById('startDate').value);
    var endDate = new Date(document.getElementById('endDate').value);

    if (startDate >= endDate) {
        alert('End date must be after the start date.');
        event.preventDefault();
    }
});
