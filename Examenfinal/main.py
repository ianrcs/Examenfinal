from flask import Flask, render_template, request

app = Flask(__name__)


# Ejercicio 1
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


@app.route('/calcular_descuento', methods=['POST'])
def calcular_descuento():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    tarros = int(request.form['tarros'])

    precio_por_tarro = 9000
    total_sin_descuento = tarros * precio_por_tarro

    if 18 <= edad <= 30:
        descuento_porcentaje = 15
    elif edad > 30:
        descuento_porcentaje = 25
    else:
        descuento_porcentaje = 0

    descuento = (descuento_porcentaje / 100) * total_sin_descuento
    total_con_descuento = total_sin_descuento - descuento

    resultado = {
        'nombre': nombre,
        'total_sin_descuento': total_sin_descuento,
        'descuento': descuento,
        'total_con_descuento': total_con_descuento
    }

    return render_template('ejercicio1.html', resultado=resultado)


# Ejercicio 2
# Usuarios registrados
usuarios_registrados = {
    'juan': 'admin',
    'pepe': 'user'
}


@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


@app.route('/verificar_usuario', methods=['POST'])
def verificar_usuario():
    usuario_ingresado = request.form['usuario']
    password_ingresado = request.form['password']

    mensaje = None

    if usuario_ingresado in usuarios_registrados and usuarios_registrados[usuario_ingresado] == password_ingresado:
        mensaje = f"Bienvenido {'administrador' if usuario_ingresado == 'juan' else 'usuario'} {usuario_ingresado}"
    else:
        mensaje = "Usuario o contraseña incorrectos."

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)