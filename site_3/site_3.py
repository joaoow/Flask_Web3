from flask import Flask
app = Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas = '<h2>Olá, programadores!</h2>'
    link = '<p><a href="user/Usuário">Clique aqui</a></p>'
    return boas_vindas + link

@app.route('/user/')
@app.route('/user/<nome>')
def user(nome="Usuário"):
    personalizar = f'<h2>Olá, {nome}!</h2>'
    instrucao = '<p>Altere o nome no <em> endereço do browser</em> \ e recarregue a página.</p>'
    return personalizar + instrucao

if __name__ == '__main__':
    app.run(debug=True)
    
