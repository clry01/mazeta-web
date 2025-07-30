from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/producto/<int:id>')
def producto(id):
    return render_template('producto.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)
