function criarLinha(produto) {
    const linha = document.createElement('tr');
    linha.innerHTML = `
            <td class='px-6 py-3 text-left' id="id-produto-${produto.id}">${produto.id}</td>
            <td class='px-6 py-3 text-left' id="id-produto-${produto.id}">${produto.nome}</td>
            <td class='px-6 py-3 text-left' id="id-produto-${produto.id}">${produto.quantidade}</td>
            <td class='px-6 py-3 text-left' id="id-produto-${produto.id}">${produto.ativo ? 'Sim': 'Não'}</td>
            <td class='px-6 py-3 text-left' id="id-produto-${produto.id}">${produto.data_recebimento}</td>
            <td class='px-6 py-3 text-left' id="id-produto-${produto.id}">${produto.id_fornecedor}</td>
            <td class='px-6 py-3 text-left'><button class="botaoEditar font-bold" data-id="${produto.id}">Editar</button></td>
            `;
    return linha;
}

export async function tabelar_produtos(filtros = {}) {
    const tabela = document.querySelector('#tabela_produtos tbody');
    tabela.innerHTML = ''
    if (Object.keys(filtros).length > 0) {
        filtros.forEach(produto => tabela.appendChild(criarLinha(produto)));

    } else {

        const resposta = await fetch('http://127.0.0.1:5000/api/consultar_produto', {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
        });
        
        const dados = await resposta.json();
        dados.forEach(produto => tabela.appendChild(criarLinha(produto)))
    }

}

async function editar_produto() {
    document.addEventListener('click', async function(e) {
        if (e.target && e.target.classList.contains('botaoEditar')) {
            const id = e.target.getAttribute('data-id');
            const dados = document.querySelectorAll(`#id-produto-${id}`);
            const valores = [];
            
            dados.forEach(dado => valores.push(dado.textContent))
            const btn = document.getElementById('btnAddProduto').click(valores)

            
        }
    })
}

async function formproduto(parametros = undefined) {
    
    document.getElementById('btnAddProduto').addEventListener('click', () => {
        document.getElementById('formProduto').classList.remove('hidden');
        if (parametros) {
            
        }
    });

}

export default function produtos() {
    editar_produto()
    
    document.getElementById('btnAddProduto').addEventListener('click', formproduto);

    document.getElementById('btnCancelarProduto').addEventListener('click', () => {
        document.getElementById('formProduto').classList.add('hidden');
    });

    document.getElementById('formAdicionarProduto').addEventListener('submit', async function (e) {
        e.preventDefault();
        
    })
}

