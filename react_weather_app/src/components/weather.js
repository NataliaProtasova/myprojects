import React from "react";

const Weather = props => (
         <div className="weather__info">
            {
            props.city &&  <div>
              <p className="weather__key">Location: 
                <span className="weather__value"> {props.city}, {props.country}</span></p>
            <p className="weather__key">Temperature: 
                <span className="weather__value"> {props.temp} </span>
            </p>
            <p className="weather__key">Sunset: 
                <span className="weather__value">{props.sunrise}</span>
            </p>

            </div>
            }
         
            <p className="error">{props.error} </p>
            </div>
    );

export default Weather;