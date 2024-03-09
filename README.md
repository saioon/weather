Projeto REST de Temperaturas
Este é um projeto Django que utiliza o Django REST Framework para fornecer informações de temperatura de várias fontes.
Funcionalidades:
Consulta de Temperatura: Os usuários podem consultar a temperatura atual de uma determinada localidade. Essa Api pode ser implementada/ consumida nos mais diversos seguimentos.
Histórico de Consultas: Registra todas as consultas de temperatura feitas pelos usuários.
Pré-requisitos
Python 3.x
Django
Django REST Framework
Instalação
Clone o repositório:
git clone https://github.com/saioon/weather
Instale as dependências:
pip install -r requirements.txt
Execute as migrações do banco de dados:
python manage.py migrate
Inicie o servidor de desenvolvimento:
python manage.py runserver
Utilização:
Consultar a temperatura atual
Para consultar a temperatura atual de uma localidade, envie uma requisição GET para a seguinte URL:
GET /api/temperatura/?cidade={nome_da_cidade}
Histórico de Consultas
O histórico de consultas pode ser acessado através da seguinte URL:
GET /api/historico/
Autores: Seu Nome (@saioon)
Licença: Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE.md para obter detalhes.
