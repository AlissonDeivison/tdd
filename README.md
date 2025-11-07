# Projeto TDD em Python — Conta Bancária Simples

## Descrição
- Tema: Conta Bancária Simples
- Projeto: operações de depósito, saque e consulta de saldo, implementadas com TDD em Python.
- Ferramenta de teste: `pytest`
- Como executar os testes: com o venv ativado, rode `pytest` (ou `pytest -q`).

### Requisitos do sistema
- Implementar uma conta bancária simplificada, com operações básicas de depósito e saque.
- A conta deve iniciar com saldo inicial zero; permitir depósitos, saques válidos e consulta do saldo atual.
- Não é permitido sacar valores maiores que o saldo disponível, nem realizar operações com valores menores ou iguais a zero.

---

## Pré-requisitos
- Python 3.x instalado e disponível no `PATH`.
- PowerShell ou CMD.

---

## Configuração (Windows)

### 1) Criar o ambiente virtual
```powershell
python -m venv venv
```

### 2) Ativar o ambiente virtual
- PowerShell:
```powershell
./venv/Scripts/Activate.ps1
```
Se aparecer erro de execução de script:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
./venv/Scripts/Activate.ps1
```

- CMD:
```bat
venv\Scripts\activate.bat
```

### 3) Instalar dependências
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4) Desativar o ambiente virtual
```powershell
deactivate
```

---

## Executar testes
Com o venv ativado:
```powershell
pytest
```

Comandos úteis:
- Saída enxuta:
```powershell
pytest -q
```
- Verbose:
```powershell
pytest -vv
```
- Parar no primeiro erro:
```powershell
pytest -x
```
- Rodar arquivo específico:
```powershell
pytest tests/test_exemplo.py -q
```
- Filtrar por nome de teste:
```powershell
pytest -k nome_do_teste -q
```

Sem ativar o venv (executável direto):
```powershell
./venv/Scripts/pytest.exe -q
```

---

## Estrutura do projeto
```
.
├── requirements.txt   # contém 'pytest'
└── tests/             # seus testes vão aqui
    └── test_exemplo.py
```

---

## Gestão de dependências
- Instalar novo pacote:
```powershell
pip install <pacote>
```
- Atualizar `requirements.txt` com o que está instalado:
```powershell
pip freeze > requirements.txt
```
- Atualizar todos os pacotes listados:
```powershell
pip install -U -r requirements.txt
```

---

## Dicas e problemas comuns
- Sempre ative o venv antes de usar `pip` e `pytest`.
- Se o PowerShell bloquear scripts, use `Set-ExecutionPolicy` conforme mostrado.
- Para remover e recriar o venv:
```powershell
Remove-Item -Recurse -Force venv
python -m venv venv
```

---
Pronto! Com isso você inicia o ciclo de TDD: escrever um teste que falha, implementar o código mínimo para passar, refatorar e repetir.

## Pré-requisitos
- Python 3.x instalado e disponível no `PATH`.
- PowerShell ou CMD.

## Setup rápido (Windows)

### 1) Criar o ambiente virtual
```powershell
python -m venv venv
```

### 2) Ativar o ambiente virtual
- PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```
Se aparecer erro de execução de script, rode:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\venv\Scripts\Activate.ps1
```

- CMD:
```bat
venv\Scripts\activate.bat
```

### 3) Atualizar o `pip` e instalar dependências
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4) Desativar o ambiente virtual
```powershell
deactivate
```

## Executar testes com Pytest
Com o venv ativado:
```powershell
pytest
```

Comandos úteis:
- Saída enxuta:
```powershell
pytest -q
```
- Mais detalhes (verbose):
```powershell
pytest -vv
```
- Parar no primeiro erro:
```powershell
pytest -x
```
- Rodar arquivo específico:
```powershell
pytest tests/test_exemplo.py -q
```
- Filtrar por nome de teste:
```powershell
pytest -k nome_do_teste -q
```

Sem ativar o venv (chamando executáveis diretamente):
```powershell
.\venv\Scripts\pytest.exe -q
```

## Gestão de dependências
- Instalar novo pacote:
```powershell
pip install <pacote>
```
- Atualizar `requirements.txt` com o que está instalado no venv:
```powershell
pip freeze > requirements.txt
```
- Atualizar todos os pacotes listados:
```powershell
pip install -U -r requirements.txt
```

## Estrutura mínima sugerida
```
.
├── requirements.txt   # contém 'pytest'
└── tests/             # seus testes vão aqui
    └── test_exemplo.py
```

## Dicas
- Sempre ative o venv antes de rodar comandos (`pip`, `pytest`, etc.).
- Se o PowerShell bloquear scripts, use o comando de `Set-ExecutionPolicy` mostrado acima.
- Para remover e recriar o venv:
```powershell
Remove-Item -Recurse -Force venv
python -m venv venv
```

---
Pronto! Com isso você consegue iniciar o ciclo de TDD: escrever um teste que falha, implementar o código mínimo para passar, refatorar e repetir.