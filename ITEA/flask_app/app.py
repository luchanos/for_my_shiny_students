from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
cars = [
    {'model': 'BMW',
     'price': 12000},
    {'model': 'audi',
     'price': 13000}
]


@app.route('/cars')
def get_cars():
    return render_template('get_cars.html', cars=cars)


@app.route('/add_car', methods=['GET', 'POST'])
def add_cars():
    print(request.form)
    # print(request)
    # print(dir(request))
    if request.method == 'POST':
        cars.append(request.form)
        # return render_template('get_cars.html', cars=cars)  # первый способ перенаправиться
        # return redirect('/cars')  # трушный редирект, можно указать что угодно, хоть гугл
        return redirect(url_for('get_cars'))  # самый трушный редирект
    return render_template('add_car.html')


app.run(debug=True)
