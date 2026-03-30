// Enable focus highlight and better editing UX
document.addEventListener("DOMContentLoaded", () => {
    const editableElements = document.querySelectorAll('[contenteditable="true"]');

    editableElements.forEach(el => {
        el.addEventListener("focus", () => {
            el.style.outline = "2px dashed #c9a84c";
        });

        el.addEventListener("blur", () => {
            el.style.outline = "none";
        });
    });
});


// Keyboard shortcuts (basic rich editing)
document.addEventListener("keydown", function (e) {

    // Ctrl + B → Bold
    if (e.ctrlKey && e.key === "b") {
        e.preventDefault();
        document.execCommand("bold");
    }

    // Ctrl + I → Italic
    if (e.ctrlKey && e.key === "i") {
        e.preventDefault();
        document.execCommand("italic");
    }

    // Ctrl + U → Underline
    if (e.ctrlKey && e.key === "u") {
        e.preventDefault();
        document.execCommand("underline");
    }

});


// Prevent unwanted formatting paste
document.addEventListener("paste", function (e) {
    e.preventDefault();

    let text = (e.clipboardData || window.clipboardData).getData("text");
    document.execCommand("insertText", false, text);
});


// Optional: Auto-save to localStorage (so user doesn't lose data)
function autoSave() {
    const resume = document.getElementById("resume");
    if (!resume) return;

    localStorage.setItem("resume_data", resume.innerHTML);
}


// Load saved data
function loadSavedData() {
    const saved = localStorage.getItem("resume_data");
    const resume = document.getElementById("resume");

    if (saved && resume) {
        resume.innerHTML = saved;
    }
}


// Run autosave every 3 seconds
setInterval(autoSave, 3000);


// Load saved content on page load
window.onload = loadSavedData;