document.getElementById("uploadForm").addEventListener("submit", function (e) {
    e.preventDefault();

    let formData = new FormData(this);
    let loading = document.getElementById("loading");
    let resultBox = document.getElementById("result");

    loading.classList.remove("hidden");
    resultBox.innerHTML = "";

    fetch("/optimize", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        loading.classList.add("hidden");

        resultBox.innerHTML = `
            <h3>Optimization Result</h3>
            <p><strong>Selected Features:</strong> ${data.selected_features.join(", ")}</p>
            <p><strong>Accuracy:</strong> ${data.accuracy}</p>
        `;
    })
    .catch(error => {
        loading.classList.add("hidden");
        resultBox.innerHTML = "<p style='color:red;'>Error occurred. Please check dataset.</p>";
    });
});
