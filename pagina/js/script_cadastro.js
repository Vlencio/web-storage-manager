const forms = document.getElementById("forms");

forms.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const usuario = document.getElementById("usuario").value;
    const senha = document.getElementById("senha").value;

    const res = await fetch("http://127.0.0.1:5000/api/cadastrar", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'email': email, 'usuario': usuario, 'senha':senha})
    });

})