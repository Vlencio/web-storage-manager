const links = document.querySelectorAll('[id^="aside"]');
const sections = document.querySelectorAll('main > section');
let isTransitioning = false;

links.forEach(link => {
    if (link.id == 'asideFornecedores') {
        link.addEventListener('click', tabelar())
    }
    
    link.addEventListener('click', () => {
        if (isTransitioning) return;
        links.forEach(link => link.classList.remove('bg-indigo-500', 'shadow-md'));
        links.forEach(link => link.classList.add('hover:bg-gray-200'));
        link.classList.add('bg-indigo-500', 'shadow-md')
        link.classList.remove('hover:bg-gray-200')
        
        const targetId = 'content' + link.id.replace('aside', '');
        const target = document.getElementById(targetId);
        
        if (!target.classList.contains('hidden')) return;
        isTransitioning = true;

        const current = Array.from(sections).find(sec => !sec.classList.contains('hidden'));

        if (current) {
            current.classList.remove('opacity-100');
            current.classList.add('opacity-0');

            setTimeout(() => {
                current.classList.add('hidden');

                target.classList.remove('hidden');
                target.classList.remove('opacity-0');
                target.classList.add('opacity-100');
                isTransitioning = false;
            }, 300)
        }
    })
})

async function tabelar(filtros = {}) {
    const tabela = document.querySelector('#tabela-fornecedores tbody');
    tabela.innerHTML = ''
    if (Object.keys(filtros).length > 0) {
        tabela.innerHTML = '';

        filtros.forEach(fornecedor => {
            const linha = document.createElement('tr');
            linha.innerHTML = `
            <td class='px-6 py-3 text-left'>${fornecedor.id}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.nome}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.cnpj}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.telefone}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.email}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.endereco}</td>
            `;
            tabela.appendChild(linha);
        })

    } else {

        const resposta = await fetch('http://127.0.0.1:5000/api/consultar_fornecedor', {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
        });
        
        const dados = await resposta.json();
        tabela.innerHTML = '';
        
        dados.forEach(fornecedor => {
            const linha = document.createElement('tr');
            linha.innerHTML = `
            <td class='px-6 py-3 text-left'>${fornecedor.id}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.nome}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.cnpj}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.telefone}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.email}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.endereco}</td>
            `;
            tabela.appendChild(linha);
        })
    }

}

document.getElementById('btnAddFornecedor').addEventListener('click', () => {
    document.getElementById('formFornecedor').classList.remove('hidden');
});
document.getElementById('btnCancelar').addEventListener('click', () => {
    document.getElementById('formFornecedor').classList.add('hidden');
});

document.getElementById('formAdicionar').addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(this);
    const fornecedor = {
        nome: formData.get('nome'),
        cnpj: formData.get('cnpj'),
        telefone: formData.get('telefone'),
        email: formData.get('email'),
        endereço: formData.get('endereco')
    };

    fetch('http://127.0.0.1:5000/api/cadastrar_fornecedor', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(fornecedor)
    })
    .then(res => res.json())
    .then(data => {
        console.log('Fornecedor adicionado:', data);
        document.getElementById('formFornecedor').classList.add('hidden');
    })
    .catch(err => console.error('Erro ao adicionar fornecedor:', err));
});

document.getElementById('btnPesquisar').addEventListener('click', () => {
    document.getElementById('formPesquisar').classList.remove('hidden');
});
document.getElementById('btnCancelarPesquisa').addEventListener('click', () => {
    document.getElementById('formPesquisar').classList.add('hidden');
});

document.getElementById('btnEnviarPesquisa').addEventListener('click', async function (e) {
    e.preventDefault();

    const form = document.getElementById('formPesquisarA')
    const formData = new FormData(form);

    const dados = {};
    formData.forEach((value, key) => {
        dados[key] = value;
    });

    const resposta = await fetch('http://127.0.0.1:5000/api/consultar_fornecedor', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(dados)
    });

    if (resposta.status === 204) {
        console.log('Nenhum conteudo retornado.');
        tabelar()
        return;
    }

    const dadosJson = await resposta.json();
    tabelar(dadosJson);
});