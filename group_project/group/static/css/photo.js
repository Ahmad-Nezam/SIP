let slideIndex = 0;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function showSlides(n) {
    let slides = document.getElementsByClassName("slider-image");

    if (n >= slides.length) {
        slideIndex = 0;
    }
    if (n < 0) {
        slideIndex = slides.length - 1;
    }

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    slides[slideIndex].style.display = "block"; 
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
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: { lat: -33.8688, lng: 151.2093 },
        mapTypeControl: true,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
            mapTypeIds: ["roadmap", "terrain"],
        },
    });
}

window.initMap = initMap;

