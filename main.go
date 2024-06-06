package main

import (
	"fmt"
	"net/http"
	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()

	r.HandleFunc("/{p}", func(w http.ResponseWriter, r *http.Request) {
		vars := mux.Vars(r)
		p := vars["p"]
		fmt.Fprintln(w, p)
	})

	http.ListenAndServe(":5000", r)
}
