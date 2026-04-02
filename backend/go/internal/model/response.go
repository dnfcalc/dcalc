package model

type Envelope struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
	Data    any    `json:"data"`
}

func Success(data any) Envelope {
	return Envelope{Code: 200, Message: "Success", Data: data}
}

func Error(code int, message string, data any) Envelope {
	return Envelope{Code: code, Message: message, Data: data}
}
