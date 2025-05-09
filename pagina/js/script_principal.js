import fornecedor, { tabelar_fornecedores } from "./sections/fornecedores.js";
import produtos, { tabelar_produtos } from "./sections/produtos.js";

produtos()
fornecedor()

const links = document.querySelectorAll('[id^="aside"]');
const sections = document.querySelectorAll('main > section');
let isTransitioning = false;

links.forEach(link => {
    if (link.id == 'asideFornecedores') {link.addEventListener('click', () => tabelar_fornecedores())}
    if (link.id == 'asideEstoque') {link.addEventListener('click', () => tabelar_produtos())}
    
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