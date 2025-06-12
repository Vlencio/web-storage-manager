function criarLinha(fornecedor) {
    const linha = document.createElement('tr');
    linha.innerHTML = `
            <td class='px-6 py-3 text-left'>${fornecedor.id}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.nome}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.cnpj}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.telefone}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.email}</td>
            <td class='px-6 py-3 text-left'>${fornecedor.endereco}</td>
            `;
    return linha;
}

export async function tabelar_fornecedores(filtros = {}) {
    const tabela = document.querySelector('#tabela-fornecedores tbody');
    tabela.innerHTML = ''
    if (Object.keys(filtros).length > 0) {
        filtros.forEach(fornecedor => tabela.appendChild(criarLinha(fornecedor)));

    } else {

        const resposta = await fetch('http://127.0.0.1:5000/api/consultar_fornecedor', {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
        });
        
        const dados = await resposta.json();
        tabela.innerHTML = '';
        dados.forEach(fornecedor => tabela.appendChild(criarLinha(fornecedor)))
    }

}

export default function fornecedor() {
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
            tabelar_fornecedores()
            return;
        }

        const dadosJson = await resposta.json();
        tabelar_fornecedores(dadosJson);
    });

}