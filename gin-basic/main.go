package main

import (
	"fmt"
	"net/http"
	"time"

	db "gin/basic/db"
	models "gin/basic/models"

	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Println("Golang Basic", time.Now().UTC().Format("2006-01-02T15:04:05.000Z"))

	db.InitDB()
	fmt.Println("Init DB")

	server := gin.Default()

	server.GET("/events", basicHandler)
	server.POST("/events", createEvents)

	server.Run(":8080")

}

func basicHandler(context *gin.Context) {
	events, err := models.GetEvents()
	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"message": "Failed to gets Events",
			"error":   err,
		})
		return
	}
	context.JSON(http.StatusOK, events)
}

func createEvents(context *gin.Context) {
	var event models.Event
	err := context.ShouldBindJSON(&event)

	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{
			"message": "Could not parse request",
		})
		return
	}

	event.ID = 1
	event.UserID = 1

	err = event.SaveEvent()

	if err != nil {
		context.JSON(http.StatusInternalServerError, gin.H{
			"message": "Failed to Save Event",
			"error":   err,
		})
		return
	}

	context.JSON(http.StatusCreated, gin.H{
		"message": "Event Created",
	})

}
