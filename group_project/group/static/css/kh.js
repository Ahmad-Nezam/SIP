function move() {
    window.location.href = stationeryUrl;
}

function move3() {
    window.location.href = toysUrl;
} 

document.addEventListener("DOMContentLoaded", function() {
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');

    signUpButton.addEventListener('click', () => {
        container.classList.add("right-panel-active");
    });

    signInButton.addEventListener('click', () => {
        container.classList.remove("right-panel-active");
    });
});