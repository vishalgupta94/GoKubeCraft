package main

import (
	"fmt"
	db "gin/basic/db"
	router "gin/basic/routes"
	"time"

	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Println("Golang Basic", time.Now().UTC().Format("2006-01-02T15:04:05.000Z"))

	db.InitDB()
	fmt.Println("Init DB")

	server := gin.Default()
	router.RegisterRouter(server)

	server.Run(":8080")

}


