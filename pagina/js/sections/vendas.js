function criarLinha(venda) {
    const linha = document.createElement('tr');
    linha.innerHTML = `
            <td class='px-6 py-3 text-left' id="id-venda-${venda.id}">${venda.id}</td>
            <td class='px-6 py-3 text-left' id="id-venda-${venda.id}">${venda.id_produto}</td>
            <td class='px-6 py-3 text-left' id="id-venda-${venda.id}">${venda.nome_produto}</td>
            <td class='px-6 py-3 text-left' id="id-venda-${venda.id}">${venda.quantidade_venda}</td>
            <td class='px-6 py-3 text-left' id="id-venda-${venda.id}">R$${venda.venda_unitaria}</td>
            <td class='px-6 py-3 text-left' id="id-venda-${venda.id}">${venda.data_venda}</td>
            <td class='px-6 py-3 text-left' id="id-venda-${venda.id}">R$${venda.lucro}</td>
            <td class='px-6 py-3 text-left'><button class="botaoEditarVenda font-bold" data-id="${venda.id}">Editar</button></td>
            `;
    return linha;
}

export async function tabelar_vendas(filtros = {}) {
    const tabela = document.querySelector('#tabela-vendas tbody');
    tabela.innerHTML = ''
    if (Object.keys(filtros).length > 0) {
        filtros.forEach(venda => tabela.appendChild(criarLinha(venda)));
    } else {

        const resposta = await fetch('http://127.0.0.1:5000/api/consultar_vendas', {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
        });
        
        const dados = await resposta.json();
        dados.forEach(venda => tabela.appendChild(criarLinha(venda)))
    }

}

async function editar_venda() {
    document.addEventListener('click', async function(e) {
        if (e.target && e.target.classList.contains('botaoEditarVenda')) {
            const id = e.target.getAttribute('data-id');
            const dados = document.querySelectorAll(`#id-venda-${id}`);

            const valores = [];
            dados.forEach(dado => valores.push(dado.textContent.trim()));
            valores[4] = valores[4].replace("R$", '')

            const form = document.getElementById('formVendasEditar') 

            form.classList.remove('hidden');
        
            const inputs = form.querySelectorAll('input');

            
            inputs.forEach((input, index) => {
                input.value = valores[index+3] || '';
            });

            form.addEventListener("submit", async function (e) {
                e.preventDefault();

                const dados = {"id": id};
                inputs.forEach(input => {
                    dados[input.name] = input.value
                });

                await fetch("http://127.0.0.1:5000/api/editar_venda", {
                    method: "PATCH",
                    headers: { "Content-Type": "application/json"},
                    body: JSON.stringify(dados)
                })
            })
        }
    })
}

export default function vendas() {
    
    editar_venda()

    document.getElementById('btnCancelarVendaEditar').addEventListener('click', () => {
        document.getElementById('formVendasEditar').classList.add('hidden');
    })

    document.getElementById('btnAddVendas').addEventListener('click', () => {
        document.getElementById('formVendas').classList.remove('hidden');
    });

    document.getElementById('btnCancelarVenda').addEventListener('click', () => {
        document.getElementById('formVendas').classList.add('hidden');
    });

    document.getElementById('formAdicionarVendas').addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(this);
        const venda = {
            id_produto: formData.get('id_produto'),
            quantidade: formData.get('quantidade'),
            venda_unitaria: formData.get('venda_unitaria'),
            data_venda: formData.get('data_venda')
        };

        fetch('http://127.0.0.1:5000/api/adicionar_venda', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(venda)
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById('formvenda').classList.add('hidden');
        })
        .catch(err => console.error('Erro ao adicionar venda:', err));
    });

    document.getElementById('btnPesquisarVenda').addEventListener('click', () => {
        document.getElementById('divformPesquisarVenda').classList.remove('hidden');
    });

    document.getElementById('btnEnviarPesquisaVenda').addEventListener('click', async function (e) {
                e.preventDefault();
        
                const form = document.getElementById('formPesquisarVenda')
                const formData = new FormData(form);
        
                const dados = {};
                formData.forEach((value, key) => {
                    dados[key] = value;
                });
        
                const resposta = await fetch('http://127.0.0.1:5000/api/consultar_vendas', {
                    method: 'POST',
                    headers: {'Content-Type':'application/json'},
                    body: JSON.stringify(dados)
                });
        
                if (resposta.status === 204) {
                    tabelar_vendas()
                    return;
                }
        
                const dadosJson = await resposta.json();
                tabelar_vendas(dadosJson);
    });

    document.getElementById('btnCancelarPesquisaVenda').addEventListener('click', () => {
        document.getElementById('divformPesquisarVenda').classList.add('hidden');
    });
}

