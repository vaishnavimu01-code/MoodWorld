// script.js


document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("generatorForm");

    if (form) {

        form.addEventListener("submit", function () {

            const button = document.getElementById("generateButton");
            const buttonText = document.getElementById("buttonText");
            const loadingText = document.getElementById("loadingText");

            if (button) {
                button.disabled = true;
            }

            if (buttonText) {
                buttonText.style.display = "none";
            }

            if (loadingText) {
                loadingText.style.display = "inline";
            }

        });

    }

});


function getDescription() {

    const element =
        document.getElementById("descriptionText");

    if (!element) {
        return "";
    }

    return element.innerText.trim();
}


function speakDescription() {

    const description = getDescription();

    if (!description) {
        return;
    }

    if (!("speechSynthesis" in window)) {

        alert(
            "Text-to-Speech is not supported in this browser."
        );

        return;
    }

    window.speechSynthesis.cancel();

    const speech =
        new SpeechSynthesisUtterance(description);

    speech.lang = "en-US";

    speech.rate = 0.9;

    speech.pitch = 1;

    speech.volume = 1;


    speech.onstart = function () {

        const button =
            document.getElementById("listenButton");

        if (button) {
            button.innerHTML = "🔊 Listening...";
        }

    };


    speech.onend = function () {

        const button =
            document.getElementById("listenButton");

        if (button) {
            button.innerHTML = "🔊 Listen";
        }

    };


    speech.onerror = function () {

        const button =
            document.getElementById("listenButton");

        if (button) {
            button.innerHTML = "🔊 Listen";
        }

    };


    window.speechSynthesis.speak(speech);
}


function pauseSpeech() {

    if ("speechSynthesis" in window) {

        if (window.speechSynthesis.speaking) {
            window.speechSynthesis.pause();
        }

    }

}


function resumeSpeech() {

    if ("speechSynthesis" in window) {

        if (window.speechSynthesis.paused) {
            window.speechSynthesis.resume();
        }

    }

}


function stopSpeech() {

    if ("speechSynthesis" in window) {

        window.speechSynthesis.cancel();

        const button =
            document.getElementById("listenButton");

        if (button) {
            button.innerHTML = "🔊 Listen";
        }

    }

}