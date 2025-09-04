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


func DeleteEvent(id int64) error {
	query := "Delete from events where id = ? "

	statement, err := db.DB.Prepare(query)

	if err != nil {
		fmt.Println("delete", err)
		return err
	}

	_, err = statement.Exec(id)

    return err
}

func UpdateEvent(event Event)  error{
	query := "update events SET name = ? ,description = ? ,datetime = ? where id = ?"

	statement, err := db.DB.Prepare(query)

	if err != nil {
		fmt.Println("1", err)
		return err
	}

	_, err = statement.Exec(event.Name,event.Description,event.Datetime,event.ID)

    return err
}

func GetEventById(id int64) (*Event,error){
	query := "Select * FROM events WHERE id = ?";

	row := db.DB.QueryRow(query, id)
    
	var event Event;

    err := row.Scan(&event.ID,&event.Name,&event.Description,&event.Datetime,&event.UserID)

	if err!= nil {
	  print("1 Error",err)
	  return nil, err
	}

    return &event, nil

}

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
