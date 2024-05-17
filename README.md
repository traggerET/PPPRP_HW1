### Запуск и результат: 
В одном терминале выполнить:  
minikube start   
./run.sh  
Запустить сервис в другом терминале:  
minikube service timer  
Команда выведет адрес, через который можно будет дергать эндпоинты приложения 

Чтобы Получить statistics.txt, нужно выполнить kubectl get pods, найти имя нужного пода и запустить:  
kubectl cp stats-7564bfccfe-bt35q:statistics.txt ./statistics.txt 

