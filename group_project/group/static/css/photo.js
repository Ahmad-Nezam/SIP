let slideIndex = 0;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("slider-image");

    if (n >= slides.length) { slideIndex = 0; }
    if (n < 0) { slideIndex = slides.length - 1; }

    for (i = 0; i < slides.length; i++) {
        slides[i].style.transform = `translateX(-${slideIndex * 100}%)`;
    }
}

function openModal() {
    document.getElementById('photoModal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('photoModal').style.display = 'none';
}


window.onclick = function(event) {
    if (event.target == document.getElementById('photoModal')) {
        closeModal();
    }
}


document.querySelector('.prev').addEventListener('click', function() {
    plusSlides(-1); 
});

document.querySelector('.next').addEventListener('click', function() {
    plusSlides(1); 
});


function initMap() {
    var villaLocation = {
        lat: parseFloat('{{ details.latitude|default:"0" }}'),
        lng: parseFloat('{{ details.longitude|default:"0" }}')
    };

  
    console.log('Latitude:', villaLocation.lat, 'Longitude:', villaLocation.lng);

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: villaLocation
    });

    var marker = new google.maps.Marker({
        position: villaLocation,
        map: map
    });
}
