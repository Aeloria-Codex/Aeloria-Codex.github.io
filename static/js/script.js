document.addEventListener('DOMContentLoaded', () => {
    // Get the navbar element
    const navBar = document.querySelector('.navBar');

    // Listen for scroll events
    window.addEventListener('scroll', () => {
        if (window.scrollY > 0) {
            navBar.classList.add('scrolled');
        } else {
            navBar.classList.remove('scrolled');
        }
    });
});

function toggleDropdown() {
    var content = document.getElementById("dropdown-content");
    var status = document.getElementById("dropdown-status");
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        status.textContent = "▲ "
    } else {
        content.style.display = "none";
        status.textContent = "➤ "
    }
}

function toggleDropdown1() {
    var content = document.getElementById("dropdown-content1");
    var status = document.getElementById("dropdown-status1");
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        status.textContent = "▲ "
    } else {
        content.style.display = "none";
        status.textContent = "➤ "
    }
}
function toggleDropdown2() {
    var content = document.getElementById("dropdown-content2");
    var status = document.getElementById("dropdown-status2");
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        status.textContent = "▲ "
    } else {
        content.style.display = "none";
        status.textContent = "➤ "
    }
}
function toggleDropdown3() {
    var content = document.getElementById("dropdown-content3");
    var status = document.getElementById("dropdown-status3");
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        status.textContent = "▲ "
    } else {
        content.style.display = "none";
        status.textContent = "➤ "
    }
}
function toggleDropdown4() {
    var content = document.getElementById("dropdown-content4");
    var status = document.getElementById("dropdown-status4");
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        status.textContent = "▲ "
    } else {
        content.style.display = "none";
        status.textContent = "➤ "
    }
}
function toggleDropdown5() {
    var content = document.getElementById("dropdown-content5");
    var status = document.getElementById("dropdown-status5");
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        status.textContent = "▲ "
    } else {
        content.style.display = "none";
        status.textContent = "➤ "
    }
}
function toggleDropdown6() {
    var content = document.getElementById("dropdown-content6");
    var status = document.getElementById("dropdown-status6");
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        status.textContent = "▲ "
    } else {
        content.style.display = "none";
        status.textContent = "➤ "
    }
}
function toggleDropdown7() {
    var content = document.getElementById("dropdown-content7");
    var status = document.getElementById("dropdown-status7");
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        status.textContent = "▲ "
    } else {
        content.style.display = "none";
        status.textContent = "➤ "
    }
}