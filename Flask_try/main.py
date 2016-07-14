from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/<id>', methods=['GET', 'POST'])
def indes(id):

    name = request.args.get('name')
    #name = id
    print(request.args)
    print(request.form)
    print(request.files)


    return render_template('index.html', name=name)

#app.run()