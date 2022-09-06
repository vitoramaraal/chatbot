from flask import Flask, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

portuguese_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")


trainer = ListTrainer(portuguese_bot)



trainer.train([
    "Eae",
    "Eae, beleza?",
    "Gostaria de pedir uma pizza",
    "Quantas pizzas?",
    "1",
    "Qual sabor?",
    "Calabresa",
    "Ok, Pedido Realizado !"

])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_response():
    userText = request.args.get("msg")
    return str(portuguese_bot.get_response(userText))


if __name__ == "__main__":
    app.run()