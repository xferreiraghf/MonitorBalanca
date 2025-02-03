# Monitoramento de Hosts e Serviços

Este projeto é uma aplicação Django que monitora o status de máquinas e serviços específicos. Ele verifica se as máquinas estão ativas e se um serviço específico (uma aplicação de balança que roda na porta 5000) está em execução.

![image](https://github.com/user-attachments/assets/a529eb9d-41b1-4283-a541-b645ca98b5f2)

---

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

1. **`views.py`**:  
   Contém a lógica principal para monitorar os hosts. A função `monitor_hosts` coleta os dados dos hosts cadastrados no banco de dados e verifica se estão ativos e se o serviço na porta 5000 está rodando. Os resultados são passados para um template HTML.

2. **`utils.py`**:  
   Contém funções utilitárias para realizar o ping em hosts e verificar se uma porta específica está aberta. As funções são compatíveis com sistemas Windows e Unix.

3. **`urls.py`**:  
   Define a URL da aplicação, mapeando a rota `/monitor/` para a função `monitor_hosts` no `views.py`.

4. **`models.py`**:  
   Define o modelo `Host`, que armazena informações como nome, empresa, sistema operacional, endereço IP e porta do serviço (padrão 5000).

5. **`admin.py`**:  
   Configura a interface de administração do Django para o modelo `Host`, permitindo a adição, edição e exclusão de hosts diretamente pelo painel admin.

6. **`monitor.html`**:  
   Template HTML que exibe os resultados do monitoramento em uma tabela interativa. A tabela permite ordenar os dados por coluna e destaca o status das máquinas e serviços com cores específicas.

---

## Funcionalidades

- **Monitoramento de Hosts**:  
  Verifica se as máquinas estão ativas através de um comando de ping.

- **Verificação de Serviço**:  
  Confirma se o serviço na porta 5000 está rodando, utilizando uma conexão de socket.

- **Interface de Administração**:  
  Permite gerenciar os hosts monitorados diretamente pelo painel admin do Django.

- **Visualização dos Resultados**:  
  Exibe os resultados em uma tabela HTML com design moderno e responsivo. O status das máquinas e serviços é destacado com cores:
  - **Máquina Online**: Verde.
  - **Máquina Offline**: Vermelho.
  - **Serviço Rodando**: Azul.
  - **Serviço Parado**: Laranja.

---

## Como Usar

1. **Configuração do Ambiente**:
   - Instale o Django e configure o banco de dados no arquivo `settings.py`.

2. **Adicionar Hosts**:
   - Acesse o painel de administração do Django (`/admin/`) e adicione os hosts que deseja monitorar.

3. **Acessar a Página de Monitoramento**:
   - Navegue até `/monitor/` para visualizar o status dos hosts e serviços.

---

## Requisitos

- Python 3.x
- Django
- Acesso ao banco de dados configurado no `settings.py`

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias.

---

## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
