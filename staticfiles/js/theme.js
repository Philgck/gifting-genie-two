function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    
    document.documentElement.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);

    // Update icon and aria-label
    updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
    const themeIcon = document.getElementById("theme-icon");
    const themeButton = document.getElementById("theme-toggle");

    if (theme === "dark") {
        themeIcon.classList.replace("fa-moon", "fa-sun"); // Change to sun icon
        themeButton.setAttribute("aria-label", "Enable Light Mode");
    } else {
        themeIcon.classList.replace("fa-sun", "fa-moon"); // Change to moon icon
        themeButton.setAttribute("aria-label", "Enable Dark Mode");
    }
}

// Apply theme on page load
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-theme", savedTheme);
    
    // Ensure correct icon and aria-label
    updateThemeIcon(savedTheme);
});
