document.getElementById('uploadForm').onsubmit = async function (e) {
    e.preventDefault();
    const file = document.getElementById('photo').files[0];
    const statusDiv = document.getElementById('uploadStatus');

    if (!file) {
        statusDiv.textContent = "Please select a photo to upload!";
        statusDiv.style.color = "red";
        return;
    }

    statusDiv.textContent = "Uploading...";

    const backendUrl = "http://<BACKEND_URL>/upload"; // Placeholder - will be replaced by Jenkins


    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch(backendUrl, {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error("Upload failed: " + response.statusText);
        }

        const result = await response.json();
        statusDiv.textContent = result.message;
        statusDiv.style.color = "green";
    } catch (error) {
        statusDiv.textContent = "Error: " + error.message;
        statusDiv.style.color = "red";
    }
};
