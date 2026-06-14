// Show loading spinner on form submit
document.querySelector("form").addEventListener("submit", function (e) {
    const input = document.querySelector("input[name='city']").value.trim();
    if (!input) return; // Let server-side validation handle it

    const btn = document.querySelector("button[type='submit']");
    btn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status"></span>';
    btn.disabled = true;
});

// Auto-capitalize first letter of city input
document.querySelector("input[name='city']").addEventListener("input", function () {
    const val = this.value;
    if (val.length === 1) {
        this.value = val.toUpperCase();
    }
});
