from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticket = request.form.get('ticket')
        if not ticket or not ticket.isdigit() or len(ticket) != 6:
            flash('Enter correct ticket!')
            return redirect(url_for('index'))
        
        first_half = sum(map(int, ticket[:3]))
        second_half = sum(map(int, ticket[3:]))
        is_lucky = first_half == second_half
        
        return render_template('result.html', is_lucky=is_lucky)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
