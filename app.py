from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        templates_directory = os.path.join(current_directory, 'templates')
        index_path = os.path.join(templates_directory, 'index.html')

        if os.path.exists(index_path):
            return render_template('index.html')
      
    except Exception as e:
        return f"Erro interno: {str(e)}"

if __name__ == '__main__':
    app.run()
