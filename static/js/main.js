// Wyswietlenie burgera na malym urzadzeniu
document.addEventListener("DOMContentLoaded", () => {
    const burger = document.querySelector('.burger');
    const menu = document.querySelector('.menu');

    burger.addEventListener('click', () => {
        menu.classList.toggle('show');
    });
});

// Wyświetlenie ui Usera
function DisplayUserUi() {
    var userPfp = document.querySelector('.user-pfp');
    var login = document.querySelector('.bx-log-in');
    var logout = document.querySelector('.bx-log-out');
    var settings = document.querySelector('.bx-cog');

    userPfp.classList.toggle('active');

    if (login.classList.contains('show') && logout.classList.contains('show') && settings.classList.contains('show')) {
        settings.classList.remove('show');
        login.classList.remove('show');
        logout.classList.remove('show');
    } else {
        settings.classList.add('show');
        login.classList.add('show');
        logout.classList.add('show');
    }
}

// Zmiana Języka
function switchLanguage(language, button) {

    document.querySelectorAll('.lang').forEach(lang => {
        lang.style.display = 'none';
    });

    document.querySelectorAll(`.lang.${language}`).forEach(lang => {
        lang.style.display = 'block';
    });

    document.querySelectorAll('.language-switcher button').forEach(btn => {
        btn.classList.remove('active');
    });

    if (button) {
        button.classList.add('active');
    } else {
        const defaultButton = document.querySelector(`.language-switcher button[data-lang="${language}"]`);
        if (defaultButton) {
            defaultButton.classList.add('active');
        }
    }
}

// Domyslnie jezyk Polski
document.addEventListener("DOMContentLoaded", () => {
    switchLanguage('pl');
});