function downloadPDF() {
    const resume = document.getElementById("resume");

    if (!resume) {
        alert("Resume content not found!");
        return;
    }

    const htmlContent = resume.innerHTML;

    fetch("/download", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ html: htmlContent })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to generate PDF");
        }
        return response.blob();
    })
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "my_resume.pdf";
        document.body.appendChild(a);
        a.click();
        a.remove();
        window.URL.revokeObjectURL(url);
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error generating PDF. Check server or WeasyPrint setup.");
    });
}