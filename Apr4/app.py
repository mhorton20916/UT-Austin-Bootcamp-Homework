from flask import Flask, jsonify
import pandas as pd
import datetime as dt
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, Column, Integer, String, Float, MetaData
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

engine = create_engine("sqlite:///hawaii.sqlite")
#metadata = MetaData()
#metadata.reflect(engine)

Base = automap_base()

Base.prepare(engine, reflect=True)

Station = Base.classes.station
Measurement = Base.classes.measurement
session=Session(bind=engine)
conn=engine.connect()






app = Flask(__name__)

@app.route('/')
def welcome():
    '''Return all available routes'''
    return (
        f'Available Routes<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/YYYY-mm-dd<br/>'
        f'/api/v1.0/YYYY-mm-dd/YYYY-mm-dd<br/>'
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    '''Return precipitation for all dates over the last year'''
    last_12_months = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>(dt.datetime.now()-dt.timedelta(days=365)))
    last_12_months_df = pd.read_sql(last_12_months.statement,last_12_months.session.bind)

    for index, row in last_12_months_df.iterrows():
        last_12_months_df.set_value(index, 'date', row['date'].strftime('%Y-%m-%d').split(' ')[0])
    last_12_months_df.set_index('date',inplace=True)
    temp_dict = last_12_months_df.to_dict()['prcp']
    new_dict = {}
    for item in temp_dict.keys():
        new_dict[item.strftime('%Y-%m-%d')] = temp_dict[item]
    return jsonify(new_dict)

@app.route('/api/v1.0/stations')
def stations():
    '''Return a list of stations'''
    stations = session.query(Station.name).all()
    stations_list = list(np.ravel(stations))
    return jsonify(stations_list)

@app.route('/api/v1.0/tobs')
def tobs():
    '''Return all temperature observations over the last year'''
    recent_temp_obs = session.query(Measurement.tobs).filter(Measurement.date>(dt.datetime.now()-dt.timedelta(days=365)))
    recent_temp_obs_df = pd.read_sql(recent_temp_obs.statement,recent_temp_obs.session.bind)
    temp_dict = recent_temp_obs_df.to_dict()['tobs']
    new_dict = {}
    for item in temp_dict.keys():
        new_dict[int(item)] = int(temp_dict[item])
    return jsonify(new_dict)

@app.route('/api/v1.0/<start>/<end>')
def calc_temps(start,end):
    '''Return min, avg, and max temperature from <start> to <end>'''
    start_datetime = dt.datetime.strptime(start,'%Y-%m-%d')
    end_datetime = dt.datetime.strptime(end,'%Y-%m-%d')
    temp_q = session.query(Measurement.tobs).filter(Measurement.date>start_datetime,Measurement.date<end_datetime)
    temp_df = pd.read_sql(temp_q.statement,temp_q.session.bind)
    print(temp_df.head())
    max_temp = int(temp_df['tobs'].max())
    min_temp = int(temp_df['tobs'].min())
    avg_temp = float(temp_df['tobs'].mean())
    temp_dict = {}
    temp_dict['max_temp'] = max_temp
    temp_dict['min_temp'] = min_temp
    temp_dict['avg_temp'] = avg_temp
    return jsonify(temp_dict)
    
@app.route('/api/v1.0/<start>')
def calc_temps_no_end(start):
    '''Return min, avg, and max temperature from <start> onward'''
    start_datetime = dt.datetime.strptime(start,'%Y-%m-%d')
    end_datetime = dt.datetime.now()
    temp_q = session.query(Measurement.tobs).filter(Measurement.date>start_datetime,Measurement.date<end_datetime)
    temp_df = pd.read_sql(temp_q.statement,temp_q.session.bind)
    print(temp_df.head())
    max_temp = int(temp_df['tobs'].max())
    min_temp = int(temp_df['tobs'].min())
    avg_temp = float(temp_df['tobs'].mean())
    temp_dict = {}
    temp_dict['max_temp'] = max_temp
    temp_dict['min_temp'] = min_temp
    temp_dict['avg_temp'] = avg_temp
    return jsonify(temp_dict)


if __name__ == '__main__':
    app.run(debug=True)
