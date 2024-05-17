from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

events = []

@app.route('/')
def home():
    return render_template('home.html', events=events)

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        event = {
            'name': request.form['name'],
            'date': request.form['date'],
            'description': request.form['description'],
            'image': request.form['image']
        }
        events.append(event)
        return redirect(url_for('home'))
    return render_template('create_event.html')

@app.route('/event/<int:event_id>')
def event_details(event_id):
    event = events[event_id]
    return render_template('event_details.html', event=event)

if __name__ == '__main__':
    app.run(debug=True)
