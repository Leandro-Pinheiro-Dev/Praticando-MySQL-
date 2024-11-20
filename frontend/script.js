document.getElementById('formUsuario').addEventListener('submit', async function(event) {
    event.preventDefault();

    const usuarioData = {
        usuario: document.getElementById('usuario').value,
        email: document.getElementById('email').value,
        telefone: document.getElementById('telefone').value,
        endereco: document.getElementById('endereco').value,
        cidade: document.getElementById('cidade').value,
        estado: document.getElementById('estado').value,
        cep: document.getElementById('cep').value,
        justificativa: document.getElementById('justificativa').value
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/cadastrar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'  // Adicionando cabeçalho
            },
            body: new URLSearchParams(usuarioData),
        });

        const result = await response.text();
        if (response.ok) {
            displayMessage('Usuário cadastrado com sucesso!', 'success');
        } else {
            displayMessage(`Erro: ${result}`, 'error');
        }
    } catch (error) {
        displayMessage(`Erro: ${error}`, 'error');
    }
});

function displayMessage(message, type) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', type);
    messageDiv.textContent = message;
    document.body.appendChild(messageDiv);
}
