document.addEventListener('DOMContentLoaded', function() {
const videos = document.querySelectorAll('video');
const playButton = document.getElementById('playSequential');

playButton.addEventListener('click', () => {
    let index = 0;

    const playNext = () => {
        if (index < videos.length) {
            const current = videos[index];
            current.currentTime = 0; // Start from beginning
            current.play();

            // When this video ends, play the next one
            current.onended = () => {
                index++;
                playNext();
            };
        }
    };

    playNext();
    });
})