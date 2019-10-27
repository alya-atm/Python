from flask import Flask,request,render_template

app1 = Flask(__name__)

@app1.route('/task2',methods=['GET','POST'])
def input_names():
    if request.method =='POST':
        username=request.form.get('username')
        return render_template('print_names.html', method=request.method, name=username.split(','))
    elif request.method =='GET':
        username = request.args.get('username')
        if username == None:
            return render_template('input_names.html')
        else:
            return render_template('print_names.html',method=request.method, name=username.split(','))
    return render_template('input_names.html')

if __name__ == '__main__':
    app1.run()