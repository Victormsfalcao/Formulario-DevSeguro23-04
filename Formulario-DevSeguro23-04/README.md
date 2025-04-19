# 📋 Formulário com Validação, RBAC e ABAC

Este projeto é um formulário web desenvolvido com **HTML**, **JavaScript**, **Python (Flask)** e **Docker**. Ele realiza validação de campos tanto no cliente quanto no servidor e implementa dois métodos de controle de acesso: **RBAC** (Role-Based Access Control) e **ABAC** (Attribute-Based Access Control).

No lado do cliente, as validações são feitas com JavaScript:  
- **Nome**: deve conter no mínimo 3 caracteres.  
- **E-mail**: deve estar em um formato válido (ex: nome@dominio.com).  
- **Senha**: precisa ter pelo menos 8 caracteres, com ao menos uma letra maiúscula e um número.  

Essas mesmas regras são reforçadas no servidor usando expressões regulares em Python.

Além da validação, o back-end aplica controle de acesso com base em regras definidas no código:  
- Pelo **RBAC**, apenas usuários com o papel de `"usuario"` ou `"admin"` têm permissão para acessar o recurso de cadastro.  
- Pelo **ABAC**, é exigido que o usuário tenha **idade mínima de 18 anos** para concluir o cadastro.  

O projeto é containerizado com Docker, facilitando a execução em qualquer sistema com Docker instalado. Para rodar localmente:

```bash
# 1. Entre na pasta do projeto
cd formulario-autorizacao

# 2. Construa a imagem Docker
docker build -t formulario-app .

# 3. Rode o container
docker run -p 5000:5000 formulario-app
```

Depois, basta acessar [http://localhost:5000](http://localhost:5000) no navegador para utilizar o formulário.

Este projeto foi desenvolvido com fins acadêmicos para demonstrar, de forma prática, como implementar validações, autenticação e autorização (RBAC e ABAC), além de empacotar tudo com Docker.
