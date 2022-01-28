# Trabalho de Redes 2
#### Repositório que será usado para o trabalho de Redes 2, conforme definido nas regras do projeto.

## Alunos
- Adriano Souza
- André Balbi
- Vitor Prado

## Tecnologias Usadas

- Python
	- requests.py
	- json.py
	- http.py (http.server)
- Git (GitHub)
- Wireshark com Modo Monitor (Kali Linux - Raspberry Pi 3)

## Funcionamento da Aplicação

Nossa aplicação gira em torno de uma troca de pacotes feitos de uma maneira insegura.
Nosso objetivo é demonstrar a importância tanto de criptografia quanto de segurança e controle na rede.

No nosso trabalho, desativamos a segurança da rede wifi, com o objetivo de deixar que os pacotes transmitidos na rede fossem expostos. Num contexto de segurança WPA2 (padrão nas redes wireless), os pacotes são criptografados. 

Depois, criamos um servidor HTTP simples, cujo propósito é receber e transmitir pacotes de volta.

No nosso exemplo, um usuário está fazendo login no seu serviço bancário. Um login tanto programado de forma insegura quanto feito de maneira sem segurança. Num caso desses, um hacker em potêncial tem acesso praticamente imediato às suas informações.  












###### versão 4.1 PRODUÇÃO - APRESENTAÇÃO
