document.getElementById('formulario').addEventListener('submit', Registrar);

function Registrar(e) {
    var name = document.getElementById('name').value;
    var lastname = document.getElementById('lastname').value;
    var edad = document.getElementById('age').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    let datos = document.getElementById('tabla-cuerpo');

    datos.innerHTML += `<tr><td>${name}</td><td>${lastname}</td><td>${edad}</td><td>${email}</td><td>${password}</td></tr>`
    //para eliminar del formulario
    document.getElementById('formulario').reset();
    //evitar que se recargue el formulario
    e.preventDefault();
}

