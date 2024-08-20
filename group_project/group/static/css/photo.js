function openModal() {
    document.getElementById("photoModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("photoModal").style.display = "none";
}

// Close the modal when the user clicks anywhere outside of it
window.onclick = function(event) {
    var modal = document.getElementById("photoModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
