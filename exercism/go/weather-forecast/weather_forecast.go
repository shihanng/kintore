// Package weather contains logic that forecast the current weather
// condition of various cities in Goblinocus.
package weather

// CurrentCondition stores the current condition of the forcast.
var CurrentCondition string

// CurrentLocation stores the current location of the forcast.
var CurrentLocation string

// Forecast stores current location and current condition and
// returns the forecast.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
