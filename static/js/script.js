document.addEventListener('DOMContentLoaded', () => {
    // Get the navbar element
    const navBar = document.querySelector('.navBar');
    const toc = document.querySelector('#toc');

    // Listen for scroll events
    window.addEventListener('scroll', () => {
        if (window.scrollY > 0) {
            navBar.classList.add('scrolled');
            toc.classList.add("scrolled");
        } else {
            navBar.classList.remove('scrolled');
            toc.classList.remove('scrolled');
        }
    });
});

function toggleDropdown0() { toggleDropdownById(0); }
function toggleDropdown1() { toggleDropdownById(1); }
function toggleDropdown2() { toggleDropdownById(2); }
function toggleDropdown3() { toggleDropdownById(3); }
function toggleDropdown4() { toggleDropdownById(4); }
function toggleDropdown5() { toggleDropdownById(5); }
function toggleDropdown6() { toggleDropdownById(6); }
function toggleDropdown7() { toggleDropdownById(7); }
function toggleDropdown8() { toggleDropdownById(8); }
function toggleDropdown9() { toggleDropdownById(9); }
function toggleDropdown10() { toggleDropdownById(10); }
function toggleDropdown11() { toggleDropdownById(11); }
function toggleDropdown12() { toggleDropdownById(12); }
function toggleDropdown13() { toggleDropdownById(13); }
function toggleDropdown14() { toggleDropdownById(14); }
function toggleDropdown15() { toggleDropdownById(15); }
function toggleDropdown16() { toggleDropdownById(16); }
function toggleDropdown17() { toggleDropdownById(17); }
function toggleDropdown18() { toggleDropdownById(18); }
function toggleDropdown19() { toggleDropdownById(19); }
function toggleDropdown20() { toggleDropdownById(20); }
function toggleDropdown21() { toggleDropdownById(21); }
function toggleDropdown22() { toggleDropdownById(22); }
function toggleDropdown23() { toggleDropdownById(23); }
function toggleDropdown24() { toggleDropdownById(24); }
function toggleDropdown25() { toggleDropdownById(25); }
function toggleDropdown26() { toggleDropdownById(26); }
function toggleDropdown27() { toggleDropdownById(27); }
function toggleDropdown28() { toggleDropdownById(28); }
function toggleDropdown29() { toggleDropdownById(29); }
function toggleDropdown30() { toggleDropdownById(30); }
function toggleDropdown31() { toggleDropdownById(31); }
function toggleDropdown32() { toggleDropdownById(32); }
function toggleDropdown33() { toggleDropdownById(33); }
function toggleDropdown34() { toggleDropdownById(34); }
function toggleDropdown35() { toggleDropdownById(35); }
function toggleDropdown36() { toggleDropdownById(36); }
function toggleDropdown37() { toggleDropdownById(37); }
function toggleDropdown38() { toggleDropdownById(38); }
function toggleDropdown39() { toggleDropdownById(39); }
function toggleDropdown40() { toggleDropdownById(40); }
function toggleDropdown41() { toggleDropdownById(41); }
function toggleDropdown42() { toggleDropdownById(42); }
function toggleDropdown43() { toggleDropdownById(43); }
function toggleDropdown44() { toggleDropdownById(44); }
function toggleDropdown45() { toggleDropdownById(45); }
function toggleDropdown46() { toggleDropdownById(46); }
function toggleDropdown47() { toggleDropdownById(47); }
function toggleDropdown48() { toggleDropdownById(48); }
function toggleDropdown49() { toggleDropdownById(49); }
function toggleDropdown50() { toggleDropdownById(50); }
function toggleDropdown51() { toggleDropdownById(51); }
function toggleDropdown52() { toggleDropdownById(52); }
function toggleDropdown53() { toggleDropdownById(53); }
function toggleDropdown54() { toggleDropdownById(54); }
function toggleDropdown55() { toggleDropdownById(55); }
function toggleDropdown56() { toggleDropdownById(56); }
function toggleDropdown57() { toggleDropdownById(57); }
function toggleDropdown58() { toggleDropdownById(58); }
function toggleDropdown59() { toggleDropdownById(59); }
function toggleDropdown60() { toggleDropdownById(60); }
function toggleDropdown61() { toggleDropdownById(61); }
function toggleDropdown62() { toggleDropdownById(62); }
function toggleDropdown63() { toggleDropdownById(63); }
function toggleDropdown64() { toggleDropdownById(64); }
function toggleDropdown65() { toggleDropdownById(65); }
function toggleDropdown66() { toggleDropdownById(66); }
function toggleDropdown67() { toggleDropdownById(67); }
function toggleDropdown68() { toggleDropdownById(68); }
function toggleDropdown69() { toggleDropdownById(69); }
function toggleDropdown70() { toggleDropdownById(70); }
function toggleDropdown71() { toggleDropdownById(71); }
function toggleDropdown72() { toggleDropdownById(72); }
function toggleDropdown73() { toggleDropdownById(73); }
function toggleDropdown74() { toggleDropdownById(74); }
function toggleDropdown75() { toggleDropdownById(75); }
function toggleDropdown76() { toggleDropdownById(76); }
function toggleDropdown77() { toggleDropdownById(77); }
function toggleDropdown78() { toggleDropdownById(78); }
function toggleDropdown79() { toggleDropdownById(79); }
function toggleDropdown80() { toggleDropdownById(80); }
function toggleDropdown81() { toggleDropdownById(81); }
function toggleDropdown82() { toggleDropdownById(82); }
function toggleDropdown83() { toggleDropdownById(83); }
function toggleDropdown84() { toggleDropdownById(84); }
function toggleDropdown85() { toggleDropdownById(85); }
function toggleDropdown86() { toggleDropdownById(86); }
function toggleDropdown87() { toggleDropdownById(87); }
function toggleDropdown88() { toggleDropdownById(88); }
function toggleDropdown89() { toggleDropdownById(89); }
function toggleDropdown90() { toggleDropdownById(90); }
function toggleDropdown91() { toggleDropdownById(91); }
function toggleDropdown92() { toggleDropdownById(92); }
function toggleDropdown93() { toggleDropdownById(93); }
function toggleDropdown94() { toggleDropdownById(94); }
function toggleDropdown95() { toggleDropdownById(95); }
function toggleDropdown96() { toggleDropdownById(96); }
function toggleDropdown97() { toggleDropdownById(97); }
function toggleDropdown98() { toggleDropdownById(98); }
function toggleDropdown99() { toggleDropdownById(99); }
function toggleDropdown100() { toggleDropdownById(100); }
function toggleDropdown101() { toggleDropdownById(101); }
function toggleDropdown102() { toggleDropdownById(102); }
function toggleDropdown103() { toggleDropdownById(103); }
function toggleDropdown104() { toggleDropdownById(104); }
function toggleDropdown105() { toggleDropdownById(105); }
function toggleDropdown106() { toggleDropdownById(106); }
function toggleDropdown107() { toggleDropdownById(107); }
function toggleDropdown108() { toggleDropdownById(108); }
function toggleDropdown109() { toggleDropdownById(109); }
function toggleDropdown110() { toggleDropdownById(110); }
function toggleDropdown111() { toggleDropdownById(111); }
function toggleDropdown112() { toggleDropdownById(112); }
function toggleDropdown113() { toggleDropdownById(113); }
function toggleDropdown114() { toggleDropdownById(114); }
function toggleDropdown115() { toggleDropdownById(115); }


function toggleDropdownById(id) {
    var content = document.getElementById("dropdown-content" + id);
    var status = document.getElementById("dropdown-status" + id);
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        status.textContent = "▲ ";
    } else {
        content.style.display = "none";
        status.textContent = "➤ ";
    }
}



document.addEventListener("DOMContentLoaded", function() {
    function applyScrollOffset() {
        if (window.location.hash) {
            const target = document.querySelector(window.location.hash);
            if (target) {
                const offset = window.innerHeight * 0.10; // 10% of the viewport height
                window.scrollTo({
                    top: target.offsetTop - offset,
                    behavior: "smooth"
                });
            }
        }
    }

    // Apply offset on page load if there’s a hash
    applyScrollOffset();

    // Apply offset on every hash link click
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function(event) {
            // Prevent default anchor behavior
            event.preventDefault();

            // Update the URL hash without jumping
            const targetHash = this.getAttribute("href");
            history.pushState(null, null, targetHash);

            // Apply the scroll offset
            applyScrollOffset();
        });
    });
});