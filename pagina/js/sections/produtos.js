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
            dados.forEach(dado => valores.push(dado.textContent.trim()));

            const [dia, mes, ano] = valores[4].split('/');
            const data = `${ano}-${mes.padStart(2, '0')}-${dia.padStart(2, '0')}`;
            
            valores[4] = data

            const form = document.getElementById('formProdutoEditar') 

            form.classList.remove('hidden');
        
            const inputs = form.querySelectorAll('input');

            inputs.forEach((input, index) => {
                input.value = valores[index+1] || '';
            });



            form.addEventListener("submit", async function (e) {
                e.preventDefault();

                const dados = {"id": id};
                inputs.forEach(input => {
                    dados[input.name] = input.value
                });


                await fetch("http://127.0.0.1:5000/api/editar_produto", {
                    method: "PATCH",
                    headers: { "Content-Type": "application/json"},
                    body: JSON.stringify(dados)
                })
            })
        }
    })
}

export default function produtos() {
    editar_produto()
    
    document.getElementById('btnAddProduto').addEventListener('click', () => {
        document.getElementById('formProduto').classList.remove('hidden');
    });

    document.getElementById('formAdicionarProduto').addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(this);
        const produto = {
            nome: formData.get('nome'),
            quantidade: formData.get('quantidade'),
            ativo: formData.get('ativo'),
            data_recebimento: formData.get('data_recebimento'),
            id_fornecedor: formData.get('id_fornecedor')
        };

        fetch('http://127.0.0.1:5000/api/cadastrar_produto', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(produto)
        })
        .then(res => res.json())
        .then(data => {
            console.log('Produto adicionado:', data);
            document.getElementById('formProduto').classList.add('hidden');
        })
        .catch(err => console.error('Erro ao adicionar produto:', err));
    });

    document.getElementById('btnCancelarProduto').addEventListener('click', () => {
        document.getElementById('formProduto').classList.add('hidden');
    });

    document.getElementById('btnPesquisarProduto').addEventListener('click', () => {
        document.getElementById('divformPesquisarProduto').classList.remove('hidden');
    }
    )

    document.getElementById('btnCancelarPesquisaProduto').addEventListener('click', () => {
        document.getElementById('divformPesquisarProduto').classList.add('hidden');
    });

    document.getElementById('btnCancelarProdutoEditar').addEventListener('click', () => {
        document.getElementById('formProdutoEditar').classList.add('hidden');
    });

    document.getElementById('formAdicionarProduto').addEventListener('submit', async function (e) {
        e.preventDefault();
        
    })

    document.getElementById('btnEnviarPesquisaProduto').addEventListener('click', async function (e) {
            e.preventDefault();
    
            const form = document.getElementById('formPesquisarProduto')
            const formData = new FormData(form);
    
            const dados = {};
            formData.forEach((value, key) => {
                dados[key] = value;
            });
    
            const resposta = await fetch('http://127.0.0.1:5000/api/consultar_produto', {
                method: 'POST',
                headers: {'Content-Type':'application/json'},
                body: JSON.stringify(dados)
            });
    
            if (resposta.status === 204) {
                tabelar_produtos()
                return;
            }
    
            const dadosJson = await resposta.json();
            tabelar_produtos(dadosJson);
        });
}

