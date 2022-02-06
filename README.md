# Trabalho de Redes 2
#### Repositório usado para o trabalho de Redes de Computadores 2, conforme definido nas regras do projeto.

## Alunos - Grupo Tubarão no Fio
- Adriano Souza
- André Balbi
- Vitor Prado

## Descrição do Projeto

Nosso projeto consiste em ressaltar a relevância da utilização de segurança nas redes, por meio de um exemplo prático. 

Para isso, montamos um cenário de uma rede desprotegida, sem segurança, na qual um cliente troca informações sensíveis com um servidor, e depois, um terceiro host, também presente na rede, consegue interceptar e ler os pacotes pertencentes a conexão alheia. 

Dessa forma, nosso objetivo é demonstrar a vulnerabilidade existente em conexões desprotegidas, e consequentemente, evidenciar a importância da utilização de protocolos de segurança nas redes.

## Tecnologias Usadas

- Python
	- requests.py
	- json.py
	- http.py (http.server)
- Git (GitHub)
- Wireshark com Modo Monitor (Kali Linux - Raspberry Pi 3)

## Instalação e Configuração

#### Instalação dos programas Cliente e Servidor
1. Instale Python 3.6+
2. Instale o pacote requests usando pip
> `$ pip install requests`
3. Execute o programa servidor e cliente, respectivamente.

#### Espião
1. Ative o modo monitor no computador
> https://www.youtube.com/watch?v=xmQUVwCuxOk
2. Instale o Wireshark e depois abra-o
> `$ sudo apt-get install wireshark`

> `$ sudo bash` 

> `$ wireshark`
3. Inicie a captura de pacotes, filtrando pelo endereço IPv4 do cliente na rede.
4. Inicie o programa servidor.
5. Inicie o programa cliente.
6. Encerre a captura de pacotes após o cliente encerrar.
7. Encerre o programa servidor.

## Funcionamento da Aplicação

Nossa aplicação gira em torno de uma troca de pacotes feitos de uma maneira insegura.

Então o primeiro passo é desativar a segurança da rede wifi, com o objetivo de deixar que os pacotes transmitidos na rede sejam expostos. Num contexto de segurança WPA2 (padrão nas redes wireless), os pacotes são criptografados. 

Depois, criamos um servidor HTTP simples, cujo propósito é receber e transmitir pacotes de volta.

No nosso exemplo, um usuário está fazendo login no seu serviço bancário. Um login tanto programado de forma insegura quanto feito de maneira sem segurança. Num caso desses, um hacker em potêncial tem acesso praticamente imediato às suas informações.  

Com o cenário de uma rede insegura na qual o usuário está trocando informações com o servidor, o ambiente de demonstração está pronto.

Por fim, utilizamos um Raspberry, capturando pacotes em modo monitor com Wireshark, para detectar e interceptar a conexão alheia, e ler os pacotes. Assim, o Raspberry, que está de fora da conexão entre o usuário e o servidor, conseguiu obter as informações de terceiros.

## Contribuições 

Queremos agradecer ao professor Flávio Seixas por ter emprestado ao grupo um Raspberry Pi 3, no qual é o dispositivo mais prático para se utilizar o modo monitor e realizar o nosso trabalho.












###### versão 4.2 PRODUÇÃO - DOCUMENTAÇÃO COMPLETA ######
