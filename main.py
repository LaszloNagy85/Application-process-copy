# coding=utf-8
import data_manager
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors-with-best-first-name')
def route_mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_mentor_names_by_first_name('Imre')

    return render_template('mentor_names.html', data=mentor_names)


@app.route('/mentors_first_last_names')
def route_first_last_names():
    names = data_manager.get_first_last_names()
    return render_template('mentor_names.html', data=names)


@app.route('/mentors_miskolc_nick_names')
def route_miskolc_nick_names():
    nicks = data_manager.get_miskolc_nicks('Miskolc')
    return render_template('mentor_names.html', data=nicks)


@app.route('/applicant_carol_data')
def route_get_carol_applicant_data():
    carol_data = data_manager.get_carol_applicant_data('Carol')[0]
    return render_template("applicant_data.html", data=carol_data)


@app.route('/applicant_hat_owners_data')
def route_get_hat_owner_applicant_data():
    hat_owner_data = data_manager.get_hat_owner_applicant_data('%@adipiscingenimmi.edu')[0]
    return render_template('applicant_data.html', data=hat_owner_data)


@app.route('/add_new_applicant')
def route_add_new_applicant():
    new_applicant_data = data_manager.insert_new_applicant('Markus', 'Schaffarzyk', '003620/725-2666',
                                                           'djnovus@groovecoverage.com', '54823')
    return render_template('mentor_names.html', data=new_applicant_data)


@app.route('/update_phone_number')
def route_update_and_show():
    updated_data = data_manager.update_data('Jemima', 'Foreman', '003670/223-7459')
    return render_template('mentor_names.html', data=updated_data)


@app.route('/delete_applicants_from_mauriseu')
def route_delete_and_show_all():
    remaining_applicants = data_manager.delete_applicants_mauriseu('%mauriseu.net')
    return render_template('mentor_names.html', data=remaining_applicants)


if __name__ == '__main__':
    app.run(
        port=8000,
        debug=False,
    )
