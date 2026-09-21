# TechBairro: Cadastro de Cliente (Atividade 16)

Gabarito da atividade 16: uma aplicação desktop de cadastro de clientes feita em Python com Tkinter, usando Programação Orientada a Objetos.

## O que o projeto demonstra

A classe `Cliente` representa um cliente com nome, telefone, e-mail e endereço, e oferece os métodos `resumo()` e `iniciais()`. A classe `GerenciadorClientes` guarda a lista de clientes e expõe as operações de CRUD: `adicionar` e `listar` já estão implementadas, enquanto `atualizar` e `remover` ficam como próximos passos da atividade.

A interface possui formulário com validação de campos vazios, telefone somente numérico e e-mail em formato básico, mensagens de status coloridas, contador de clientes cadastrados e uma janela de consulta com lista e barra de rolagem.

## Como executar

Requer Python 3 com Tkinter (já incluído na instalação padrão do Python no Windows e no macOS).

```bash
python main.py
```

No Linux, caso o Tkinter não esteja instalado: `sudo apt install python3-tk`.

## Estrutura

`main.py` contém todo o código da aplicação.
