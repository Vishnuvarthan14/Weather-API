from flask import Flask,render_template,request,url_for
from weather import main as get_data

app=Flask(__name__)

@app.route('/' ,methods=['GET','POST'])
def load():
    data=None
    if request.method == 'POST':
        city= request.form['cityName']
        state= request.form['stateName']
        country= request.form['countryName']
        data=get_data(city,state,country)
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)

