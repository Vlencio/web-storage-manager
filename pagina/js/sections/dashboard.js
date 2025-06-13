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
            `;
    return linha;
}

function criarLinhaProduto(produto) {
    const linha = document.createElement('tr');
    
    let statusClass, statusText;
    if (produto.quantidade === 0) {
        statusClass = 'text-red-600';
    } else if (produto.quantidade <= 20) {
        statusClass = 'text-yellow-600';
    } else if (produto.quantidade <= 30) {
        statusClass = 'text-blue-600';
    } else {
        statusClass = 'text-green-600';
    }
    
    linha.innerHTML = `
            <td class='px-4 py-2 text-sm text-gray-900'>${produto.nome}</td>
            <td class='px-4 py-2 text-sm ${statusClass} font-medium'>${produto.quantidade}</td>
            `;
    return linha;
}

export default async function dashboard() {
        const resposta = await fetch('http://127.0.0.1:5000/api/dashboard', {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
        });
    
        const dados = await resposta.json();
        document.getElementById('totalVendas').innerHTML = `R$ ${dados[0]}`;
        document.getElementById('totalProdutos').innerHTML = dados[1];
        document.getElementById('totalFornecedores').innerHTML = dados[2];

        const tabela = document.querySelector('#ultimasVendas tbody');

        const vendas = await fetch('http://127.0.0.1:5000/api/consultar_vendas', {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
        });
        
        const dadosVendas = await vendas.json();
        dadosVendas.slice(0, 10).forEach(venda => tabela.appendChild(criarLinha(venda)));

        const estoque = await fetch('http://127.0.0.1:5000/api/consultar_produto', {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
        });

        const tabelaProdutos = document.querySelector('#baixoEstoque tbody');
        const dadosEstoque = await estoque.json();

        dadosEstoque.sort((a, b) => a.quantidade - b.quantidade);
        console.log(dadosEstoque);
        dadosEstoque.slice(0, 10).forEach(produto => tabelaProdutos.appendChild(criarLinhaProduto(produto)));

}

