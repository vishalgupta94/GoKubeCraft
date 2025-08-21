package main

import (
	"fmt"
	"net/http"
	"time"

	models "gin/basic/models"

	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Print("Golang Basic", time.Now().UTC().Format("2006-01-02T15:04:05.000Z"))

	server := gin.Default()

	server.GET("/events", basicHandler)
	server.POST("/events", createEvents)

	server.Run(":8080")

}

func basicHandler(context *gin.Context) {
	events := models.GetEvents()
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

	event.SaveEvent()

	context.JSON(http.StatusCreated, gin.H{
		"message": "Event Created",
	})

}
