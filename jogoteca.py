# Importantando flask, após ja ter instalado flask pelo terminal
from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome 
        self.categoria=categoria
        self.console=console

# Guardando o app em uma variavel
app = Flask(__name__)

# Criando rota, com função que retorna um texto em html
@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tibia', 'MMORPG', 'PC Windows')
    jogo2 = Jogo('New World', 'MMORPG', 'PC Windows')
    jogo3 = Jogo('Valorant', 'FPS Multijogador', 'PC Windows')
    jogo4 = Jogo('Elden Ring', 'RPG', 'PC Windows')
    jogo4 = Jogo('Palworld', 'Sobrevivencia', 'PC Windows')
    lista = [jogo1,jogo2,jogo3,jogo4]
    return render_template('lista.html', titulo='Jogos', jogos = lista)

# trecho da app
# app.run(host='0.0.0.0', port=8080)
app.run()