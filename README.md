```bash
grpcurl -v -plaintext -import-path ./protos --proto ./protos/snakes.proto -d '{ "id": 3 }' localhost:50052 snakes.SnakesService/GetSnake
```
