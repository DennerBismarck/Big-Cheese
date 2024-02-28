# Projeto Big Cheese 3000

## 1. Visão Geral

O **Big Cheese 3000** é um sistema de gerenciamento de produtos e vendas, desenvolvido utilizando o framework Django. Este sistema permite o cadastro de produtos, registro de vendas, acompanhamento do pagamento de vendas, e análise de desempenho de vendas.

## 2. Estrutura do Projeto

### 2.1. Models

O projeto possui os seguintes modelos:

- **Produto:**
  - Campos:
    - `pro_desc`: Descrição do produto.
    - `pro_preco`: Preço do produto.

- **Venda:**
  - Campos:
    - `ven_pro`: Relação muitos para muitos com Produto, através do modelo Produtos_Das_Vendas.
    - `ven_precoTotal`: Preço total da venda.
    - `ven_DataHora`: Data e hora da compra.
    - `ven_desc`: Descrição da venda.
    - `ven_pago`: Status do pagamento ("Pagou" ou "Não Pagou").

- **Produtos_Das_Vendas:**
  - Campos:
    - `pdv_pro`: Chave estrangeira para Produto.
    - `pdv_ven`: Chave estrangeira para Venda.
    - `pdv_qtd`: Quantidade comprada.
    - `pdv_PrecoTotalItem`: Valor total do produto na venda.

### 2.2. Views

- **index:**
  - Página inicial exibindo um resumo das estatísticas do sistema.

- **TabelaProdutos:**
  - Página que exibe uma tabela com todos os produtos cadastrados.
  - Permite adicionar, editar e excluir produtos.

- **TabelaVendas:**
  - Página que exibe uma tabela com todas as vendas registradas.
  - Permite registrar novas vendas.

- **CadastrarVenda:**
  - Endpoint para cadastrar uma nova venda.
  - Permite selecionar produtos, definir quantidades e registrar o pagamento.

- **EditarVenda:**
  - Endpoint para editar uma venda existente.
  - Permite alterar produtos, quantidades e informações da venda.

## 3. Funcionalidades

### 3.1. Cadastro de Produtos

- **Adicionar Produto:**
  - Acesse a página "Produtos" e clique em "Adicionar Produto".
  - Preencha os campos necessários e clique em "Salvar".

- **Editar Produto:**
  - Na página "Produtos", clique no ícone de edição ao lado do produto desejado.
  - Faça as alterações desejadas e clique em "Salvar".

- **Excluir Produto:**
  - Na página "Produtos", clique no ícone de exclusão ao lado do produto desejado.
  - Confirme a exclusão.

### 3.2. Registro de Vendas

- **Registrar Venda:**
  - Acesse a página "Compras" e clique em "Registrar Venda".
  - Selecione os produtos, defina as quantidades e informações da venda.
  - Clique em "Salvar" para registrar a venda.

- **Editar Venda:**
  - Na página "Compras", clique no ícone de edição ao lado da venda desejada.
  - Faça as alterações necessárias e clique em "Salvar".

### 3.3. Análise de Desempenho

- **Estatísticas na Página Inicial:**
  - A página inicial exibe o ganho total, compras não pagas e produtos mais vendidos.

## 4. Executando o Projeto Localmente

- **1. Certifique-se de ter o ambiente virtual ativado.**
 - source venv/bin/activate
 - Navegue até o diretório do projeto.
 - cd caminho/do/seu/projeto
- **2. Execute o servidor de desenvolvimento.**
 - python manage.py runserver
 - Abra o navegador e acesse http://localhost:8000/ para visualizar o projeto.
### **5. Considerações Finais**
O Big Cheese 3000 é uma ferramenta poderosa para gerenciamento de produtos e vendas. Sinta-se à vontade para explorar as funcionalidades e personalizar conforme suas necessidades. Em caso de dúvidas ou problemas, consulte a documentação ou entre em contato com os desenvolvedores.
