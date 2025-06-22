function RunEmotionAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    fetch("/emotionDetector", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `textToAnalyze=${encodeURIComponent(textToAnalyze)}`
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("system_response").innerText = data;
    })
    .catch(error => {
        document.getElementById("system_response").innerText = "Error: " + error;
    });
}
