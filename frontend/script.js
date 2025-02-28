async function scanUrl() {
    let urlInput = document.getElementById("urlInput");
    let resultBox = document.getElementById("result-box");
    let resultText = document.getElementById("result");
    let loading = document.getElementById("loading");

    let url = urlInput.value.trim();
    if (!url) {
        resultText.innerText = "⚠️ Please enter a valid URL!";
        resultBox.classList.remove("hidden");
        return;
    }

    loading.classList.remove("hidden");
    resultBox.classList.add("hidden");

    try {
        let response = await fetch(`http://127.0.0.1:8000/scan/?url=${encodeURIComponent(url)}`);
        let data = await response.json();
        loading.classList.add("hidden");
        resultBox.classList.remove("hidden");

        if (data.status.includes("Suspicious")) {
            resultText.innerHTML = `❌ <span class="suspicious">${data.status}</span>`;
        } else {
            resultText.innerHTML = `✅ <span class="safe">${data.status}</span>`;
        }
    } catch (error) {
        resultText.innerText = "⚠️ Error scanning the URL.";
        resultBox.classList.remove("hidden");
    }
}

/* Toggle Dark Mode */
function toggleTheme() {
    document.body.classList.toggle("dark-mode");
}
