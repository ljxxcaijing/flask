from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
        return render_template('hello.html', name=name)
   
   '''render_template方法可以渲染模版'''
