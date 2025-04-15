const botao = document.getElementById('botao')

if (localStorage.getItem('login') !== "true") {
    window.location.href = "../html/login.html";
}

botao.addEventListener('click', () => {
    localStorage.removeItem('login');
    window.location.href = '../html/login.html';
})