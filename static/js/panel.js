// Change theme
function darkMode(){
    document.body.classList.toggle('dark-mode-variables');
}

// Display extra ui
function DisplayNotesPanel(panelId) {
    var panel = document.getElementById(panelId);
    if (panel.classList.contains('show')) {
        panel.classList.remove('show');
    } else {
        panel.classList.add('show');
    }
}

// Display User ui
function DisplayUserUi(){
    var settings = document.querySelector('.bxs-cog');
    var profile = document.querySelector('.bxs-user-circle');
    if(settings.classList.contains('show') && profile.classList.contains('show')){
        settings.classList.remove('show')
        profile.classList.remove('show')
    }else{
        settings.classList.add('show')
        profile.classList.add('show')
    }
}


// Pagination
let containerElm = null;

function switchToPage(evt) {
    const { target } = evt;
    if (!target.classList.contains("btn")) {
        return;
    }

    const clickedBtn = target;
    if (clickedBtn.classList.contains("active")) {
        return;
    }

    const activeBtn = containerElm.querySelector(".btn.active");
    activeBtn?.classList.remove("active");
    clickedBtn.classList.add("active");

    const targetPageId = clickedBtn.getAttribute("data-target");

    const pages = document.querySelectorAll(".container");
    pages.forEach((page) => page.classList.add("hidden"));

    const targetPage = document.getElementById(targetPageId);
    if (targetPage) {
        targetPage.classList.remove("hidden");
    }
}

document.addEventListener("DOMContentLoaded", () => {
    containerElm = document.getElementById("container");
    containerElm.addEventListener("click", switchToPage);
});