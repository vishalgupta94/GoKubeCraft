package routes

import (
	"gin/basic/models"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)


func RegisterRouter(server *gin.Engine){
	server.GET("/events", basicHandler)
	server.GET("/events/:id", getById)
	server.POST("/events", createEvents)
	server.PUT("/events/:id", updateEvent)
	server.DELETE("/events/:id", DeleteEvent)
}

func DeleteEvent(context *gin.Context){
	id := context.Param("id")
 
	eventId, err := strconv.ParseInt(id, 10, 64)

	if err != nil {
		context.JSON(http.StatusBadRequest,gin.H{
			"message": "Could not parse id",
			"err": err,
		})
		return
    }

	_, err = models.GetEventById(eventId)

	if err != nil {
		 context.JSON(http.StatusBadRequest,gin.H{
		  "message": "Could not get event from database",
		  "err": err,
		 })
		 return
	}

   err = models.DeleteEvent(eventId)

   if err != nil {
		context.JSON(http.StatusBadRequest,gin.H{
		"message": "Could not delete from database",
		"err": err,
		})
		return
   }

   context.JSON(http.StatusOK, gin.H{
	 "message": "Event Deleted",
	})

}

func updateEvent(context *gin.Context){
	id := context.Param("id")
 
	eventId, err := strconv.ParseInt(id, 10, 64)

	if err != nil {
		context.JSON(http.StatusBadRequest,gin.H{
			"message": "Could not parse id",
			"err": err,
		})
		return
   }

   _, err = models.GetEventById(eventId)

   if err != nil {
		context.JSON(http.StatusBadRequest,gin.H{
		 "message": "Could not get event from database",
		 "err": err,
		})
		return
   }
   var updatedEvent models.Event

   err = context.ShouldBindJSON(&updatedEvent)

   if err != nil {
		context.JSON(http.StatusBadRequest,gin.H{
		"message": "Could not parse event ",
		"err": err,
		})
	   return
	}
    
	updatedEvent.ID = eventId

    err = models.UpdateEvent(updatedEvent)

	if err != nil {
		context.JSON(http.StatusBadRequest, gin.H{
			"message": "Could not parse event ",
			"err": err,
		})
	   return
	}

	context.JSON(http.StatusCreated, gin.H{
		"message": "Event Updated",
	})



}

func getById(context *gin.Context){
	id := context.Param("id")
 
	eventId, err := strconv.ParseInt(id, 10, 64)
 
	if err != nil {
		 context.JSON(http.StatusBadRequest,gin.H{
			 "message": "Could not parse id",
			 "err": err,
		 })
		 return
	}
	event, err := models.GetEventById(eventId)
 
	if err != nil {
		 context.JSON(http.StatusBadRequest,gin.H{
			 "message": "Could not get event from database",
			 "err": err,
		 })
		 return
	}
 
	context.JSON(http.StatusOK, event)
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