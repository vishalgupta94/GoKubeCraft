package models

import "time"

type Event struct {
	ID          int
	Name        string    `binding:"required"`
	Description string    `binding:"required"`
	Datetime    time.Time `binding:"required"`
	UserID      int
}

var events = []Event{}

func (e Event) SaveEvent() {
	events = append(events, e)
}

func GetEvents() []Event {
	return events
}
