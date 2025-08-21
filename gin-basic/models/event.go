package models

import (
	"fmt"
	"gin/basic/db"
	"time"
)

type Event struct {
	ID          int64
	Name        string    `binding:"required"`
	Description string    `binding:"required"`
	Datetime    time.Time `binding:"required"`
	UserID      int64
}

var events = []Event{}

func (e Event) SaveEvent() error {
	query := `INSERT INTO events(name,description,datetime,userId) values(?,?,?,?)`

	statement, err := db.DB.Prepare(query)

	if err != nil {
		fmt.Println("1", err)
		return err
	}
	defer statement.Close()

	result, err := statement.Exec(e.Name, e.Description, e.Datetime, e.UserID)

	if err != nil {

		return err
	}

	id, err := result.LastInsertId()
	e.ID = id
	events = append(events, e)

	return err

}

func GetEvents() ([]Event, error) {
	query := `SELECT * from events`

	rows, err := db.DB.Query(query)

	if err != nil {
		fmt.Println("1", err)
		return nil, err
	}

	defer rows.Close()
	var events = []Event{}

	for rows.Next() {

		var event Event
		err := rows.Scan(&event.ID, &event.Name, &event.Description, &event.Datetime, &event.UserID)

		if err != nil {
			fmt.Println("2", err)
			return nil, err
		}

		events = append(events, event)
	}

	return events, nil
}
